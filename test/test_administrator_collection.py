# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.administrator_collection import (
    AdministratorCollection,
)  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestAdministratorCollection(unittest.TestCase):
    """AdministratorCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdministratorCollection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AdministratorCollection`
        """
        model = winthrop_client_python.models.administrator_collection.AdministratorCollection()  # noqa: E501
        if include_optional :
            return AdministratorCollection(
                data = [
                    winthrop_client_python.models.administrator.Administrator(
                        id = 1, 
                        coach_id = 1, 
                        coach_first_name = 'John', 
                        coach_last_name = 'Doe', 
                        coach_name = 'John Doe', 
                        season_id = 1, 
                        position_id = 1, 
                        school_id = 1, 
                        conference_id = 1, 
                        division_id = 1, 
                        geo_division_id = 1, 
                        compensation_id = 1, 
                        contract_id = 1, 
                        year = 2019, 
                        position_title = 'This is a position title', 
                        school_name = 'This is a school name', 
                        school_short_name = 'This is a school short name', 
                        state = 'This is a state', 
                        usnwr_ranking = 1, 
                        directors_cup_ranking = 1, 
                        compensation_cents = 10000, 
                        compensation_base_salary_cents = 10000, 
                        compensation_type = 'yearly', 
                        compensation_outside_income_cents = 10000, 
                        compensation_deferred_comp_cents = 10000, 
                        compensation_one_time_bonus_cents = 10000, 
                        compensation_contingent_bonus_comp_cents = 10000, 
                        compensation_buyout_terms = 'This is a compensation buyout terms', 
                        compensation_num_cars = 1, 
                        compensation_car_stipend_cents = 10000, 
                        compensation_country_club_dues_cents = 10000, 
                        compensation_country_club_membership_paid = False, 
                        compensation_media_link = 'This is a compensation media link', 
                        contract_starts_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        contract_expires_on = 'Mon Dec 31 18:00:00 CST 2018', 
                        diversity = False, 
                        gender = 'M', 
                        alma_mater_id = 2, 
                        private = False, 
                        sport_id = 2089953594, 
                        coli = 11.09, )
                    ], 
                meta = winthrop_client_python.models.meta.Meta(
                    current_page = 2, 
                    total_pages = 7, 
                    total_entries = 654, 
                    next_page = 3, 
                    previous_page = 1, )
            )
        else :
            return AdministratorCollection(
        )
        """

    def testAdministratorCollection(self):
        """Test AdministratorCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()