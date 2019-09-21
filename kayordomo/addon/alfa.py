#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
# Copyright 2018-2019 Eloy García Almadén <eloy.garcia.pca@gmail.com>
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

"""This module gathers all the global attributes, methods and classes needed for managing Kodi alfa addon.

"""
import base64
import requests
import util.settings

# Global module constants

# Global module attributes


class AlfaAddon:
    """Manages all the actions available for Kodi Alfa addon.

    """
    # Constructor
    def __init__(self):
        # Logger
        pass
        # self.__logger = util.utils.Logger(self.__class__.__name__).get()

    # noinspection PyMethodMayBeStatic
    def search_globally(self, search_terms):
        """Performs a global search (including films and tv shows on all the available channels).

        Arguments:
            search_terms (string): terms used for performing the search.

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
            "title": "Borrar b\\u00fasquedas guardadas"
        }
    ], 
    "extra": \"""" + search_terms + """\", 
    "fanart": "", 
    "infoLabels": {}, 
    "thumbnail": "/home/user/.kodi/addons/plugin.video.alfa/resources/media/themes/default/thumb_search.png", 
    "title": "    \\\"""" + search_terms + """\\\"", 
    "totalItems": 0
}"""
        test_encoded = base64.b64encode(test.encode('utf-8'))

        # Test CURL
        print("Executing curl")
        headers = {'Content-type': 'application/json', }
        data = '{"jsonrpc": "2.0","method": "Addons.ExecuteAddon","params": {"wait": false,"addonid": "plugin.video.alfa","params": ["' + test_encoded.decode('ascii') + '%3D"]},"id": 2}'
        print(data)
        response = requests.post("http://{kodi_address}:{kodi_port}/jsonrpc".format(
            kodi_address=util.settings.kodi_address,kodi_port=util.settings.kodi_port), headers=headers, data=data)
        print(response)
