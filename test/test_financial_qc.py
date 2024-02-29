# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.financial_qc import FinancialQc


class TestFinancialQc(unittest.TestCase):
    """FinancialQc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialQc:
        """Test FinancialQc
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FinancialQc`
        """
        model = FinancialQc()
        if include_optional:
            return FinancialQc(
                school_id = 1,
                school_name = 'Example School',
                ncca_pdf = True,
                audited_pdf = False,
                nca_csv = True,
                school_info_csv = False,
                sport_stats_csv = True,
                year = 2024
            )
        else:
            return FinancialQc(
        )
        """

    def testFinancialQc(self):
        """Test FinancialQc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
