# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Compensation(BaseModel):
    """
    Compensation
    """

    id: Optional[StrictInt] = None
    bonus_comp_cents: Optional[StrictInt] = None
    deferred_comp_cents: Optional[StrictInt] = None
    talent_fee: Optional[StrictInt] = None
    num_cars: Optional[StrictInt] = None
    country_club_dues_cents: Optional[StrictInt] = None
    coach_id: Optional[StrictInt] = None
    buyout_terms: Optional[StrictStr] = None
    executed_on: Optional[datetime] = None
    expires_on: Optional[datetime] = None
    start_on: Optional[datetime] = None
    end_on: Optional[datetime] = None
    average_yearly_comp_cents: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    outside_income_cents: Optional[StrictInt] = None
    one_time_bonus_cents: Optional[StrictInt] = None
    comment: Optional[StrictStr] = None
    car_stipend_cents: Optional[StrictInt] = None
    country_club_membership_paid: Optional[StrictBool] = None
    base_salary_cents: Optional[StrictInt] = None
    bonus_has_contingents: Optional[StrictBool] = None
    calculated_guaranteed_comp_cents: Optional[StrictInt] = None
    contingent_bonus_comp_cents: Optional[StrictInt] = None
    noncontingent_bonus_comp_cents: Optional[StrictInt] = None
    compensation_type: Optional[StrictStr] = None
    media_link: Optional[StrictStr] = None
    contract_status_id: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    school_id: Optional[StrictInt] = None
    __properties = [
        "id",
        "bonus_comp_cents",
        "deferred_comp_cents",
        "talent_fee",
        "num_cars",
        "country_club_dues_cents",
        "coach_id",
        "buyout_terms",
        "executed_on",
        "expires_on",
        "start_on",
        "end_on",
        "average_yearly_comp_cents",
        "created_at",
        "updated_at",
        "outside_income_cents",
        "one_time_bonus_cents",
        "comment",
        "car_stipend_cents",
        "country_club_membership_paid",
        "base_salary_cents",
        "bonus_has_contingents",
        "calculated_guaranteed_comp_cents",
        "contingent_bonus_comp_cents",
        "noncontingent_bonus_comp_cents",
        "compensation_type",
        "media_link",
        "contract_status_id",
        "year",
        "school_id",
    ]

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
    def from_json(cls, json_str: str) -> Compensation:
        """Create an instance of Compensation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Compensation:
        """Create an instance of Compensation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Compensation.parse_obj(obj)

        _obj = Compensation.parse_obj(
            {
                "id": obj.get("id"),
                "bonus_comp_cents": obj.get("bonus_comp_cents"),
                "deferred_comp_cents": obj.get("deferred_comp_cents"),
                "talent_fee": obj.get("talent_fee"),
                "num_cars": obj.get("num_cars"),
                "country_club_dues_cents": obj.get("country_club_dues_cents"),
                "coach_id": obj.get("coach_id"),
                "buyout_terms": obj.get("buyout_terms"),
                "executed_on": obj.get("executed_on"),
                "expires_on": obj.get("expires_on"),
                "start_on": obj.get("start_on"),
                "end_on": obj.get("end_on"),
                "average_yearly_comp_cents": obj.get("average_yearly_comp_cents"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "outside_income_cents": obj.get("outside_income_cents"),
                "one_time_bonus_cents": obj.get("one_time_bonus_cents"),
                "comment": obj.get("comment"),
                "car_stipend_cents": obj.get("car_stipend_cents"),
                "country_club_membership_paid": obj.get("country_club_membership_paid"),
                "base_salary_cents": obj.get("base_salary_cents"),
                "bonus_has_contingents": obj.get("bonus_has_contingents"),
                "calculated_guaranteed_comp_cents": obj.get(
                    "calculated_guaranteed_comp_cents"
                ),
                "contingent_bonus_comp_cents": obj.get("contingent_bonus_comp_cents"),
                "noncontingent_bonus_comp_cents": obj.get(
                    "noncontingent_bonus_comp_cents"
                ),
                "compensation_type": obj.get("compensation_type"),
                "media_link": obj.get("media_link"),
                "contract_status_id": obj.get("contract_status_id"),
                "year": obj.get("year"),
                "school_id": obj.get("school_id"),
            }
        )
        return _obj
