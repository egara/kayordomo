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

import addon.alfa
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, unquote

# Constants
SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8083
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

        # Redirecting the action
        function = self.__action_dispatcher.get(action, self.alfaSearch)
        function(unquote(search_terms[0]))

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
    print('Starting server...')

    # Setting server
    server_address = (SERVER_ADDRESS, SERVER_PORT)
    httpd = HTTPServer(server_address, KayordomoRequestHandler)
    print('Running server...')
    # Running server
    httpd.serve_forever()