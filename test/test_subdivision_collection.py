# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.subdivision_collection import SubdivisionCollection


class TestSubdivisionCollection(unittest.TestCase):
    """SubdivisionCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubdivisionCollection:
        """Test SubdivisionCollection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SubdivisionCollection`
        """
        model = SubdivisionCollection()
        if include_optional:
            return SubdivisionCollection(
                data = [
                    winthrop_client_python.models.subdivision.Subdivision(
                        id = 56, 
                        name = '', 
                        name_display = '', 
                        division_id = 56, )
                    ],
                meta = winthrop_client_python.models.meta.Meta(
                    current_page = 2, 
                    total_pages = 7, 
                    total_entries = 654, 
                    next_page = 3, 
                    previous_page = 1, )
            )
        else:
            return SubdivisionCollection(
        )
        """

    def testSubdivisionCollection(self):
        """Test SubdivisionCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
