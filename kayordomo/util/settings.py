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

"""This module gathers all the global attributes, methods and classes needed for application settings.

"""
from systemd.journal import JournaldLogHandler
import logging
import os
import yaml

# Global module constants
CONF_FILE = "kayordomo.yaml"

# Global module attributes
# Application work directory
application_path = ""
# Server IP address
server_ip = ""
# Server port
server_port = ""
# Kodi address
kodi_ip = ""
# Kodi port
kodi_port = ""
# Properties Manager
properties_manager = None


class PropertiesManager:
    """Manages the user properties for the application.

    If no user settings are loaded yet, then the yaml file kayordomo.yaml will be
    read and parsed in self.__user_settings dictionary.

    The keys of the dictionary will be the properties name in the yaml file. The values will be the values
    in the yaml file for every property.
    """
    # Constructor
    def __init__(self):
        # Getting an instance of the logger object this module will use
        self.__logger = logging.getLogger(self.__class__.__name__)

        # Instantiating the JournaldLogHandler to hook into systemd
        journald_handler = JournaldLogHandler()

        # Setting a formatter to include the level name
        journald_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(message)s'
        ))

        # Adding the journald handler to the current logger
        self.__logger.addHandler(journald_handler)

        # Setting the logging level
        self.__logger.setLevel(logging.INFO)

        # Setting global values related to the application
        self.__conf_file_path = '{application_path}/{conf_file}'.format(application_path=application_path,
                                                                        conf_file=CONF_FILE)
        self.__logger.info("Configuration file should be located at {conf_file_path}".format(
            conf_file_path=self.__conf_file_path))
        print("Configuration file should be located at {conf_file_path}".format(conf_file_path=self.__conf_file_path))

        self.__user_settings = []
        # Reading configuration file (kayordomo.yaml)
        if os.path.exists(self.__conf_file_path):
            conf_file = open(self.__conf_file_path)
            self.__user_settings = yaml.load(conf_file, Loader=yaml.FullLoader)

            conf_file.close()
        else:
            self.__logger.info("Warning: There is no configuration file...")
            print("Warning: There is no configuration file...")

    def get_property(self, kayordomo_property):
        """Gets the value of a property.

        Arguments:
            kayordomo_property (string): Property to get its value.

        Returns:
            string: The value of the property. 0 if the property was not found.
        """
        value = ""
        if len(self.__user_settings) > 0:
            value = self.__user_settings.get(kayordomo_property, 0)
        return value
