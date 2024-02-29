# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.contact_collection import ContactCollection


class TestContactCollection(unittest.TestCase):
    """ContactCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactCollection:
        """Test ContactCollection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContactCollection`
        """
        model = ContactCollection()
        if include_optional:
            return ContactCollection(
                data = [
                    winthrop_client_python.models.contact.Contact(
                        id = 1, 
                        school_id = 2, 
                        coach_id = 3, 
                        sport_id = 4, 
                        created_at = '2019-01-01T00:00Z', 
                        updated_at = '2019-01-01T00:00Z', )
                    ],
                meta = winthrop_client_python.models.meta.Meta(
                    current_page = 2, 
                    total_pages = 7, 
                    total_entries = 654, 
                    next_page = 3, 
                    previous_page = 1, )
            )
        else:
            return ContactCollection(
        )
        """

    def testContactCollection(self):
        """Test ContactCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()