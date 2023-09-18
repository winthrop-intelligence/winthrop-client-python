# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.season import Season  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestSeason(unittest.TestCase):
    """Season unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Season
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Season`
        """
        model = winthrop_client_python.models.season.Season()  # noqa: E501
        if include_optional :
            return Season(
                id = 1, 
                name = '2019-2020', 
                description = '2019-2020', 
                school_id = 2, 
                sport_id = 3, 
                year = 2019, 
                wins = 4, 
                losses = 5, 
                conference_wins = 6, 
                conference_losses = 7, 
                apr = 8, 
                created_at = '2019-01-01T00:00Z', 
                updated_at = '2019-01-01T00:00Z', 
                win_percent = 0.5, 
                ties = 9, 
                rpi = 10, 
                prev_rpi = 11, 
                conference_position = 12, 
                conference_num_positions = 13, 
                coach_apr = 14, 
                attendance = 15, 
                conference_ties = 16, 
                recruit_ranking = 17, 
                offensive_efficiency = 18.0, 
                defensive_efficiency = 19.0, 
                sos_ranking = 20, 
                sos = 21.0, 
                home_wins = 22, 
                home_losses = 23, 
                home_win_percent = 0.5, 
                asr = 24
            )
        else :
            return Season(
        )
        """

    def testSeason(self):
        """Test Season"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
