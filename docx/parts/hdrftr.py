# encoding: utf-8

"""Header and footer part objects"""

from __future__ import absolute_import, division, print_function, unicode_literals

from docx.opc.part import XmlPart


class FooterPart(XmlPart):
    """Definition of a section footer."""


class HeaderPart(XmlPart):
    """Definition of a section header."""
