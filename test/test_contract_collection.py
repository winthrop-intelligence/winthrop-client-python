# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.contract_collection import (
    ContractCollection,
)  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestContractCollection(unittest.TestCase):
    """ContractCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractCollection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractCollection`
        """
        model = winthrop_client_python.models.contract_collection.ContractCollection()  # noqa: E501
        if include_optional :
            return ContractCollection(
                data = [
                    winthrop_client_python.models.contract.Contract(
                        id = 1, 
                        executed_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        expires_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        start_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        end_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        at_will = False, 
                        verified = False, 
                        contractable_type = 'Coach', 
                        contractable_id = 1, 
                        raw_contract_id = 1, 
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
        else :
            return ContractCollection(
        )
        """

    def testContractCollection(self):
        """Test ContractCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
