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
from winthrop_client_python.models.requested_item import RequestedItem  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestRequestedItem(unittest.TestCase):
    """RequestedItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RequestedItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RequestedItem`
        """
        model = winthrop_client_python.models.requested_item.RequestedItem()  # noqa: E501
        if include_optional :
            return RequestedItem(
                id = 1, 
                foia_request_id = 2, 
                requestable_id = 3, 
                requestable_type = 'DealStatus', 
                received = False, 
                created_at = '2019-01-01T00:00Z', 
                updated_at = '2019-01-01T00:00Z', 
                coach_id = 4, 
                status = 'pending'
            )
        else :
            return RequestedItem(
                foia_request_id = 2,
                requestable_id = 3,
                requestable_type = 'DealStatus',
        )
        """

    def testRequestedItem(self):
        """Test RequestedItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
