# encoding: utf-8

"""Custom element classes related to headers and footers"""

from __future__ import absolute_import, division, print_function, unicode_literals

from docx.oxml.xmlchemy import BaseOxmlElement


class CT_HdrFtr(BaseOxmlElement):
    """`w:hdr` and `w:ftr`, the root element for header and footer part respectively"""
