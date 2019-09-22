#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
# Copyright 2019-2020 Eloy García Almadén <eloy.garcia.pca@gmail.com>
#
# This file is part of kayordomo.
#
# This program is free software: you can redistribute it and / or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from http.server import BaseHTTPRequestHandler, HTTPServer
from systemd.journal import JournaldLogHandler
from urllib.parse import urlparse, parse_qs
import addon.alfa
import logging
import util.settings
import util.util

# Constants
STATUS_200 = 200


class KayordomoRequestHandler(BaseHTTPRequestHandler):
    """This service will handle every request pointed to kayordomo.

    Class inherited from BaseHTTPRequestHandler (HTTP handler)
    """
    # Constructor
    def __init__(self, request, client_address, server):
        # Switcher to redirect the flow of the application depending on
        # the entry point of the URL received
        self.__action_dispatcher = {
            'alfaSearch': self.alfaSearch
        }

        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        """Receives the request and send a response.

        """
        # Sending response
        # Building status code
        self.send_response(STATUS_200)

        # Building headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Sending message back to client
        message = "OK"

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        # Getting action
        action = self.path.replace('/', '')
        action = action.split('?')[0]

        # Getting parameters
        query_components = parse_qs(urlparse(self.path).query)
        search_terms = query_components['terms']
        sanitized_terms = util.util.sanitize(search_terms[0])

        # Redirecting the action
        function = self.__action_dispatcher.get(action, self.alfaSearch)
        function(sanitized_terms)

        return

    # noinspection PyMethodMayBeStatic
    def alfaSearch(self, search_terms):
        """Runs a search invoking Kodi Alfa addon.

        Arguments:
            search_terms (string): The terms selected to perform the search using Alfa addon.
        """
        alfa_addon = addon.alfa.AlfaAddon()
        alfa_addon.search_globally(search_terms)


if __name__ == '__main__':
    # Get an instance of the logger object this module will use
    logger = logging.getLogger(__name__)

    # instantiate the JournaldLogHandler to hook into systemd
    journald_handler = JournaldLogHandler()

    # set a formatter to include the level name
    journald_handler.setFormatter(logging.Formatter(
        '[%(levelname)s] %(message)s'
    ))

    # add the journald handler to the current logger
    logger.addHandler(journald_handler)

    # optionally set the logging level
    logger.setLevel(logging.INFO)

    # Configuring the application
    logger.info("Configuring Kayordomo. Please wait...")
    print("Configuring Kayordomo. Please wait...")

    kayordomo_configurator = util.util.ConfigManager()
    kayordomo_configurator.configure()

    logger.info("Starting server...")
    print("Starting server...")

    # Setting server
    server_address = (util.settings.server_ip, int(util.settings.server_port))
    httpd = HTTPServer(server_address, KayordomoRequestHandler)

    logger.info("Running server on {server_ip} and port {server_port}".format(server_ip=util.settings.server_ip,
                                                                              server_port=util.settings.server_port))
    print("Running server on {server_ip} and port {server_port}".format(server_ip=util.settings.server_ip,
                                                                        server_port=util.settings.server_port))

    # Running server
    httpd.serve_forever()
