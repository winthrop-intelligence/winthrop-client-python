# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.avatar import Avatar  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestAvatar(unittest.TestCase):
    """Avatar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Avatar
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Avatar`
        """
        model = winthrop_client_python.models.avatar.Avatar()  # noqa: E501
        if include_optional :
            return Avatar(
                original_url = 'https://winthrop-development.s3.amazonaws.com/logos/original/1836339699/Alabama_Crimson_Tide.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2AOM4MHPY54WAI5M%2F20230628%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230628T205207Z&X-Amz-Expires=10&X-Amz-SignedHeaders=host&X-Amz-Signature=048b817de488c6f8517b260f3494555236ee7593720d7a7695a43e7e320f262c', 
                medium_url = 'https://winthrop-development.s3.amazonaws.com/logos/medium/1836339699/Alabama_Crimson_Tide.gif', 
                small_url = 'https://winthrop-development.s3.amazonaws.com/logos/small/1836339699/Alabama_Crimson_Tide.gif'
            )
        else :
            return Avatar(
        )
        """

    def testAvatar(self):
        """Test Avatar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
