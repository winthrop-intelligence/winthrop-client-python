# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.deal_status import DealStatus  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestDealStatus(unittest.TestCase):
    """DealStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DealStatus
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DealStatus`
        """
        model = winthrop_client_python.models.deal_status.DealStatus()  # noqa: E501
        if include_optional :
            return DealStatus(
                id = 1, 
                school_id = 2, 
                auto_renew = False, 
                created_at = '2019-01-01T00:00Z', 
                updated_at = '2019-01-01T00:00Z', 
                source_note = 'This is a note', 
                note = 'This is a note', 
                deal_status_type_id = 3, 
                deal_type_id = 4
            )
        else :
            return DealStatus(
                school_id = 2,
                deal_type_id = 4,
        )
        """

    def testDealStatus(self):
        """Test DealStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
