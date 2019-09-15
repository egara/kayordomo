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
import unidecode as unidecode


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
