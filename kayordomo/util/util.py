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

"""This module gathers all the utilities used in kayordomo.

"""
from urllib.parse import urlparse, parse_qs, unquote
import os
import sys
import unidecode as unidecode
import util.settings


def sanitize(text):
    """Sanitize the text.

    This method URL decodes any text and substitute any accented character by a similar one.

    Arguments:
        text (string): The text to sanitize.

    Returns:
        string: text sanitized.
    """
    url_decoded_text = unquote(text)
    unaccented_text = unidecode.unidecode(url_decoded_text)
    return unaccented_text


class ConfigManager:
    """Manages the configuration.

    """
    # Constants

    # Constructor
    def __init__(self):
        # Setting global values related to the application
        # Getting current working directory
        util.settings.application_path = os.getcwd()

    # noinspection PyMethodMayBeStatic
    def configure(self):
        """Configures the application.

        """
        # Creating a properties manager to manage all the application properties
        print("Creating PropertiesManager...")
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()

        util.settings.properties_manager = util.settings.PropertiesManager()

        # Retrieving configuration...
        print("Retrieving user's configuration from kayordomo.yaml file and loading it in memory...")
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()

        # Server IP address
        util.settings.server_ip = util.settings.properties_manager.get_property('server_ip')
        print("Server IP address: {server_ip}".format(server_ip=util.settings.server_ip))
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()

        # Server port
        util.settings.server_port = util.settings.properties_manager.get_property('server_port')
        print("Server port: {server_port}".format(server_port=util.settings.server_port))
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()

        # Kodi IP address
        util.settings.kodi_ip = util.settings.properties_manager.get_property('kodi_ip')
        print("Kodi IP address: {kodi_ip}".format(kodi_ip=util.settings.kodi_ip))
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()

        # Server port
        util.settings.kodi_port = util.settings.properties_manager.get_property('kodi_port')
        print("Kodi port: {kodi_port}".format(kodi_port=util.settings.kodi_port))
        # Flushing stdout in order to display the messages on systemd journal
        sys.stdout.flush()
