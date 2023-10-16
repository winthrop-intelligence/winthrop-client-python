# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, validator


class Administrator(BaseModel):
    """
    Administrator
    """

    id: Optional[StrictInt] = None
    coach_id: Optional[StrictInt] = None
    coach_first_name: Optional[StrictStr] = None
    coach_last_name: Optional[StrictStr] = None
    coach_name: Optional[StrictStr] = None
    season_id: Optional[StrictInt] = None
    position_id: Optional[StrictInt] = None
    school_id: Optional[StrictInt] = None
    conference_id: Optional[StrictInt] = None
    division_id: Optional[StrictInt] = None
    geo_division_id: Optional[StrictInt] = None
    compensation_id: Optional[StrictInt] = None
    contract_id: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    position_title: Optional[StrictStr] = None
    school_name: Optional[StrictStr] = None
    school_short_name: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    usnwr_ranking: Optional[StrictInt] = None
    directors_cup_ranking: Optional[StrictInt] = None
    compensation_cents: Optional[StrictInt] = None
    compensation_base_salary_cents: Optional[StrictInt] = None
    compensation_type: Optional[StrictStr] = None
    compensation_outside_income_cents: Optional[StrictInt] = None
    compensation_deferred_comp_cents: Optional[StrictInt] = None
    compensation_one_time_bonus_cents: Optional[StrictInt] = None
    compensation_contingent_bonus_comp_cents: Optional[StrictInt] = None
    compensation_buyout_terms: Optional[StrictStr] = None
    compensation_num_cars: Optional[StrictInt] = None
    compensation_car_stipend_cents: Optional[StrictInt] = None
    compensation_country_club_dues_cents: Optional[StrictInt] = None
    compensation_country_club_membership_paid: Optional[StrictBool] = None
    compensation_media_link: Optional[StrictStr] = None
    contract_starts_on: Optional[date] = None
    contract_expires_on: Optional[date] = None
    diversity: Optional[StrictBool] = None
    gender: Optional[StrictStr] = None
    alma_mater_id: Optional[StrictInt] = None
    private: Optional[StrictBool] = None
    sport_id: Optional[StrictInt] = None
    coli: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = [
        "id",
        "coach_id",
        "coach_first_name",
        "coach_last_name",
        "coach_name",
        "season_id",
        "position_id",
        "school_id",
        "conference_id",
        "division_id",
        "geo_division_id",
        "compensation_id",
        "contract_id",
        "year",
        "position_title",
        "school_name",
        "school_short_name",
        "state",
        "usnwr_ranking",
        "directors_cup_ranking",
        "compensation_cents",
        "compensation_base_salary_cents",
        "compensation_type",
        "compensation_outside_income_cents",
        "compensation_deferred_comp_cents",
        "compensation_one_time_bonus_cents",
        "compensation_contingent_bonus_comp_cents",
        "compensation_buyout_terms",
        "compensation_num_cars",
        "compensation_car_stipend_cents",
        "compensation_country_club_dues_cents",
        "compensation_country_club_membership_paid",
        "compensation_media_link",
        "contract_starts_on",
        "contract_expires_on",
        "diversity",
        "gender",
        "alma_mater_id",
        "private",
        "sport_id",
        "coli",
    ]

    @validator("compensation_type")
    def compensation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("yearly", "hourly", "990"):
            raise ValueError("must be one of enum values ('yearly', 'hourly', '990')")
        return value

    @validator("gender")
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("M", "F", ""):
            raise ValueError("must be one of enum values ('M', 'F', '')")
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Administrator:
        """Create an instance of Administrator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Administrator:
        """Create an instance of Administrator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Administrator.parse_obj(obj)

        _obj = Administrator.parse_obj(
            {
                "id": obj.get("id"),
                "coach_id": obj.get("coach_id"),
                "coach_first_name": obj.get("coach_first_name"),
                "coach_last_name": obj.get("coach_last_name"),
                "coach_name": obj.get("coach_name"),
                "season_id": obj.get("season_id"),
                "position_id": obj.get("position_id"),
                "school_id": obj.get("school_id"),
                "conference_id": obj.get("conference_id"),
                "division_id": obj.get("division_id"),
                "geo_division_id": obj.get("geo_division_id"),
                "compensation_id": obj.get("compensation_id"),
                "contract_id": obj.get("contract_id"),
                "year": obj.get("year"),
                "position_title": obj.get("position_title"),
                "school_name": obj.get("school_name"),
                "school_short_name": obj.get("school_short_name"),
                "state": obj.get("state"),
                "usnwr_ranking": obj.get("usnwr_ranking"),
                "directors_cup_ranking": obj.get("directors_cup_ranking"),
                "compensation_cents": obj.get("compensation_cents"),
                "compensation_base_salary_cents": obj.get(
                    "compensation_base_salary_cents"
                ),
                "compensation_type": obj.get("compensation_type"),
                "compensation_outside_income_cents": obj.get(
                    "compensation_outside_income_cents"
                ),
                "compensation_deferred_comp_cents": obj.get(
                    "compensation_deferred_comp_cents"
                ),
                "compensation_one_time_bonus_cents": obj.get(
                    "compensation_one_time_bonus_cents"
                ),
                "compensation_contingent_bonus_comp_cents": obj.get(
                    "compensation_contingent_bonus_comp_cents"
                ),
                "compensation_buyout_terms": obj.get("compensation_buyout_terms"),
                "compensation_num_cars": obj.get("compensation_num_cars"),
                "compensation_car_stipend_cents": obj.get(
                    "compensation_car_stipend_cents"
                ),
                "compensation_country_club_dues_cents": obj.get(
                    "compensation_country_club_dues_cents"
                ),
                "compensation_country_club_membership_paid": obj.get(
                    "compensation_country_club_membership_paid"
                ),
                "compensation_media_link": obj.get("compensation_media_link"),
                "contract_starts_on": obj.get("contract_starts_on"),
                "contract_expires_on": obj.get("contract_expires_on"),
                "diversity": obj.get("diversity"),
                "gender": obj.get("gender"),
                "alma_mater_id": obj.get("alma_mater_id"),
                "private": obj.get("private"),
                "sport_id": obj.get("sport_id"),
                "coli": obj.get("coli"),
            }
        )
        return _obj
