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
from winthrop_client_python.models.income_report_collection import (
    IncomeReportCollection,
)  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestIncomeReportCollection(unittest.TestCase):
    """IncomeReportCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IncomeReportCollection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `IncomeReportCollection`
        """
        model = winthrop_client_python.models.income_report_collection.IncomeReportCollection()  # noqa: E501
        if include_optional :
            return IncomeReportCollection(
                data = [
                    winthrop_client_python.models.income_report.IncomeReport(
                        id = 1, 
                        coach_id = 2, 
                        raw_contract_id = 3, 
                        year = 2020, 
                        created_at = '2019-01-01T00:00Z', 
                        updated_at = '2019-01-01T00:00Z', 
                        notes = 'This is a note', 
                        contract_status_id = 5, )
                    ], 
                meta = winthrop_client_python.models.meta.Meta(
                    current_page = 1, 
                    total_pages = 7, 
                    total_entries = 654, 
                    next_page = 2, 
                    previous_page = '', )
            )
        else :
            return IncomeReportCollection(
        )
        """

    def testIncomeReportCollection(self):
        """Test IncomeReportCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
