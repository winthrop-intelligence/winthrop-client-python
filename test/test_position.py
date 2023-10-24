# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import winthrop_client_python
from winthrop_client_python.models.position import Position  # noqa: E501
from winthrop_client_python.rest import ApiException


class TestPosition(unittest.TestCase):
    """Position unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Position
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Position`
        """
        model = winthrop_client_python.models.position.Position()  # noqa: E501
        if include_optional :
            return Position(
                id = 1, 
                season_id = 2, 
                coach_id = 3, 
                start_on = 'Mon Dec 31 18:00:00 CST 2018', 
                end_on = 'Mon Dec 31 18:00:00 CST 2018', 
                partial_season = False, 
                compensation_id = 4, 
                coach_apr = 5, 
                title = 'This is a title', 
                departing = False, 
                departing_set_at = '2019-01-01T00:00Z', 
                coach = winthrop_client_python.models.coach.Coach(
                    id = 1, 
                    first_name = 'John', 
                    last_name = 'Doe', 
                    email = 'jdoe@alabama.edu', 
                    phone = '555-555-5555', 
                    leader = False, 
                    bio = 'https://rolltide.com/staff-directory/greg-byrne/519', ), 
                sport = winthrop_client_python.models.sport.Sport(
                    id = 1, 
                    name = 'BOWLING', 
                    name_aka = 'bowling', 
                    name_display = 'Bowling', 
                    gender_code = 'M', 
                    emerging = False, 
                    meet_sport = False, 
                    created_at = '2019-01-01T00:00Z', 
                    updated_at = '2019-01-01T00:00Z', ), 
                school = winthrop_client_python.models.school.School(
                    id = 1, 
                    name = 'University of Alabama', 
                    short_name = 'Alabama', 
                    location = 'Tuscaloosa, AL', 
                    created_at = '2019-01-01T00:00Z', 
                    updated_at = '2019-01-01T00:00Z', 
                    city = 'Tuscaloosa', 
                    nickname = 'Crimson Tide', 
                    external_url = 'http://www.rolltide.com', 
                    colors = 'Crimson, White', 
                    state = 'AL', 
                    primary_conference_id = 1, 
                    cost_of_living_index_city_code = '01-46220-900', 
                    current_directors_cup_ranking = 27, 
                    current_usnwr_ranking = 153, 
                    private = False, 
                    school_classification_id = 18, 
                    logo_updated_at = '2019-01-01T00:00Z', 
                    youtube_search_name = 'University of Alabama', 
                    latitude = 33.2098, 
                    longitude = -87.5692, 
                    address_1 = '739 University Blvd', 
                    address_2 = 'Box 870158', 
                    zip_code = '35487', 
                    logo = winthrop_client_python.models.school_logo.SchoolLogo(
                        original_url = 'https://winthrop-development.s3.amazonaws.com/logos/original/1836339699/Alabama_Crimson_Tide.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2AOM4MHPY54WAI5M%2F20230628%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230628T205207Z&X-Amz-Expires=10&X-Amz-SignedHeaders=host&X-Amz-Signature=048b817de488c6f8517b260f3494555236ee7593720d7a7695a43e7e320f262c', 
                        medium_url = 'https://winthrop-development.s3.amazonaws.com/logos/medium/1836339699/Alabama_Crimson_Tide.gif', 
                        small_url = 'https://winthrop-development.s3.amazonaws.com/logos/small/1836339699/Alabama_Crimson_Tide.gif', ), 
                    athletic_director = winthrop_client_python.models.coach.Coach(
                        id = 1, 
                        first_name = 'John', 
                        last_name = 'Doe', 
                        email = 'jdoe@alabama.edu', 
                        phone = '555-555-5555', 
                        leader = False, 
                        bio = 'https://rolltide.com/staff-directory/greg-byrne/519', ), )
            )
        else :
            return Position(
        )
        """

    def testPosition(self):
        """Test Position"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()