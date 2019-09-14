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

import requests
import base64
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
        self.__action_switcher = {
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
        function = self.__action_switcher.get(action, self.alfaSearch)
        function(unquote(search_terms[0]))

        return

    def alfaSearch(self, search_terms):
        """Runs a search invoking Kodi Alfa addon.

        Arguments:
            search_terms (string): The terms selected to perform the search using Alfa addon.
        """
        print("Searching " + search_terms + " in Alpha addon. Please wait...")
        test = """{
    "action": "do_search", 
    "category": \"""" + search_terms + """\", 
    "channel": "search", 
    "context": [
        {
            "action": "setting_channel", 
            "channel": "search", 
            "from_action": "do_search", 
            "from_channel": "search", 
            "title": "Elegir canales incluidos"
        }, 
        {
            "action": "clear_saved_searches", 
            "channel": "search", 
            "from_action": "do_search", 
            "from_channel": "search", 
            "title": "Borrar b\u00fasquedas guardadas"
        }
    ], 
    "extra": \"""" + search_terms + """"\", 
    "fanart": "", 
    "infoLabels": {}, 
    "thumbnail": "/home/user/.kodi/addons/plugin.video.alfa/resources/media/themes/default/thumb_search.png", 
    "title": "    \"""" + search_terms + """"\", 
    "totalItems": 0
}"""
        test_encoded = base64.b64encode(test.encode('utf-8'))
        print(test_encoded)

        # Test CURL
        print('Executing curl')
        headers = {'Content-type': 'application/json',}
        data = '{"jsonrpc": "2.0","method": "Addons.ExecuteAddon","params": {"wait": false,"addonid": "plugin.video.alfa","params": ["' + test_encoded.decode('ascii') +'%3D"]},"id": 2}'
        print(data)
        response = requests.post('http://localhost:8080/jsonrpc', headers=headers, data=data)
        print(response)


if __name__ == '__main__':
    print('Starting server...')

    # Setting server
    server_address = (SERVER_ADDRESS, SERVER_PORT)
    httpd = HTTPServer(server_address, KayordomoRequestHandler)
    print('Running server...')
    # Running server
    httpd.serve_forever()