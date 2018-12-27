# encoding: utf-8

"""Unit test suite for the docx.parts.hdrftr module"""

from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from docx.opc.constants import CONTENT_TYPE as CT, RELATIONSHIP_TYPE as RT
from docx.opc.part import PartFactory
from docx.package import Package
from docx.parts.hdrftr import FooterPart, HeaderPart

from ..unitutil.mock import instance_mock, method_mock


class DescribeFooterPart(object):

    def it_is_used_by_loader_to_construct_footer_part(
        self, package_, FooterPart_load_, footer_part_
    ):
        partname = "footer1.xml"
        content_type = CT.WML_FOOTER
        reltype = RT.FOOTER
        blob = "<w:ftr/>"
        FooterPart_load_.return_value = footer_part_

        part = PartFactory(partname, content_type, reltype, blob, package_)

        FooterPart_load_.assert_called_once_with(partname, content_type, blob, package_)
        assert part is footer_part_

    # fixture components ---------------------------------------------

    @pytest.fixture
    def FooterPart_load_(self, request):
        return method_mock(request, FooterPart, "load")

    @pytest.fixture
    def footer_part_(self, request):
        return instance_mock(request, FooterPart)

    @pytest.fixture
    def package_(self, request):
        return instance_mock(request, Package)


class DescribeHeaderPart(object):

    def it_is_used_by_loader_to_construct_header_part(
        self, package_, HeaderPart_load_, header_part_
    ):
        partname = "header1.xml"
        content_type = CT.WML_HEADER
        reltype = RT.HEADER
        blob = "<w:hdr/>"
        HeaderPart_load_.return_value = header_part_

        part = PartFactory(partname, content_type, reltype, blob, package_)

        HeaderPart_load_.assert_called_once_with(partname, content_type, blob, package_)
        assert part is header_part_

    # fixture components ---------------------------------------------

    @pytest.fixture
    def HeaderPart_load_(self, request):
        return method_mock(request, HeaderPart, "load")

    @pytest.fixture
    def header_part_(self, request):
        return instance_mock(request, HeaderPart)

    @pytest.fixture
    def package_(self, request):
        return instance_mock(request, Package)
