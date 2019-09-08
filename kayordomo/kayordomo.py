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
from http.server import BaseHTTPRequestHandler, HTTPServer

# Constants
SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8083
STATUS_200 = 200


class KayordomoRequestHandler(BaseHTTPRequestHandler):
    """This service will handle every request pointed to kayordomo.

    Class inherited from BaseHTTPRequestHandler (HTTP handler)
    """
    def do_GET(self):
        """Initializes the Graphic User Interface.

        """
        # Send response status code
        self.send_response(STATUS_200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        # Test CURL
        print('Executing curl')
        # headers = {'Content-type': 'application/json',}
        # data = '{"jsonrpc": "2.0","method": "Addons.ExecuteAddon","params": {"wait": false,"addonid": "plugin.video.alfa","params": ["ewogICAgImFjdGlvbiI6ICJkb19zZWFyY2giLCAKICAgICJjYXRlZ29yeSI6ICJsb3MgMTAwIiwgCiAgICAiY2hhbm5lbCI6ICJzZWFyY2giLCAKICAgICJjb250ZXh0IjogWwogICAgICAgIHsKICAgICAgICAgICAgImFjdGlvbiI6ICJzZXR0aW5nX2NoYW5uZWwiLCAKICAgICAgICAgICAgImNoYW5uZWwiOiAic2VhcmNoIiwgCiAgICAgICAgICAgICJmcm9tX2FjdGlvbiI6ICJkb19zZWFyY2giLCAKICAgICAgICAgICAgImZyb21fY2hhbm5lbCI6ICJzZWFyY2giLCAKICAgICAgICAgICAgInRpdGxlIjogIkVsZWdpciBjYW5hbGVzIGluY2x1aWRvcyIKICAgICAgICB9LCAKICAgICAgICB7CiAgICAgICAgICAgICJhY3Rpb24iOiAiY2xlYXJfc2F2ZWRfc2VhcmNoZXMiLCAKICAgICAgICAgICAgImNoYW5uZWwiOiAic2VhcmNoIiwgCiAgICAgICAgICAgICJmcm9tX2FjdGlvbiI6ICJkb19zZWFyY2giLCAKICAgICAgICAgICAgImZyb21fY2hhbm5lbCI6ICJzZWFyY2giLCAKICAgICAgICAgICAgInRpdGxlIjogIkJvcnJhciBiXHUwMGZhc3F1ZWRhcyBndWFyZGFkYXMiCiAgICAgICAgfQogICAgXSwgCiAgICAiZXh0cmEiOiAibG9zIDEwMCIsIAogICAgImZhbmFydCI6ICIiLCAKICAgICJpbmZvTGFiZWxzIjoge30sIAogICAgInRodW1ibmFpbCI6ICIvaG9tZS91c2VyLy5rb2RpL2FkZG9ucy9wbHVnaW4udmlkZW8uYWxmYS9yZXNvdXJjZXMvbWVkaWEvdGhlbWVzL2RlZmF1bHQvdGh1bWJfc2VhcmNoLnBuZyIsIAogICAgInRpdGxlIjogIiAgICBcImxvcyAxMDBcIiIsIAogICAgInRvdGFsSXRlbXMiOiAwCn0%3D"]},"id": 2}'
        # response = requests.post('http://localhost:8080/jsonrpc', headers=headers, data=data)
        # print(response)

        return


if __name__ == '__main__':
    print('Starting server...')

    # Setting server
    server_address = (SERVER_ADDRESS, SERVER_PORT)
    httpd = HTTPServer(server_address, KayordomoRequestHandler)
    print('Running server...')
    # Running server
    httpd.serve_forever()