# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.26.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.verify_user_intercollegiate_access200_response import (
    VerifyUserIntercollegiateAccess200Response,
)


class TestVerifyUserIntercollegiateAccess200Response(unittest.TestCase):
    """VerifyUserIntercollegiateAccess200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> VerifyUserIntercollegiateAccess200Response:
        """Test VerifyUserIntercollegiateAccess200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VerifyUserIntercollegiateAccess200Response`
        """
        model = VerifyUserIntercollegiateAccess200Response()
        if include_optional:
            return VerifyUserIntercollegiateAccess200Response(
                access_granted = True
            )
        else:
            return VerifyUserIntercollegiateAccess200Response(
        )
        """

    def testVerifyUserIntercollegiateAccess200Response(self):
        """Test VerifyUserIntercollegiateAccess200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
