# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.23.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.link_collection1 import LinkCollection1


class TestLinkCollection1(unittest.TestCase):
    """LinkCollection1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkCollection1:
        """Test LinkCollection1
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LinkCollection1`
        """
        model = LinkCollection1()
        if include_optional:
            return LinkCollection1(
                data = [
                    winthrop_client_python.models.tag.Tag(
                        name = 'tag1', )
                    ]
            )
        else:
            return LinkCollection1(
        )
        """

    def testLinkCollection1(self):
        """Test LinkCollection1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()