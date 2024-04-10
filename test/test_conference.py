# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.conference import Conference


class TestConference(unittest.TestCase):
    """Conference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Conference:
        """Test Conference
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Conference`
        """
        model = Conference()
        if include_optional:
            return Conference(
                id = 56,
                name = '',
                name_display = '',
                nickname = '',
                headquarters = '',
                founded = 56,
                division_id = 56,
                ord = 56,
                created_at = '2019-01-01T00:00Z',
                updated_at = '2019-01-01T00:00Z',
                external_url = ''
            )
        else:
            return Conference(
        )
        """

    def testConference(self):
        """Test Conference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
