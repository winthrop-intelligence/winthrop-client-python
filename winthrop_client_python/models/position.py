# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist
from winthrop_client_python.models.coach import Coach
from winthrop_client_python.models.school import School
from winthrop_client_python.models.sport import Sport


class Position(BaseModel):
    """
    Position
    """

    id: Optional[StrictInt] = None
    season_id: Optional[StrictInt] = None
    coach_id: Optional[StrictInt] = None
    start_on: Optional[date] = None
    end_on: Optional[date] = None
    partial_season: Optional[StrictBool] = None
    compensation_id: Optional[StrictInt] = None
    coach_apr: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    name_display: Optional[StrictStr] = None
    departing: Optional[StrictBool] = None
    departing_set_at: Optional[datetime] = None
    coach: Optional[Coach] = None
    sport: Optional[Sport] = None
    school: Optional[School] = None
    position_types: Optional[conlist(StrictStr)] = None
    __properties = [
        "id",
        "season_id",
        "coach_id",
        "start_on",
        "end_on",
        "partial_season",
        "compensation_id",
        "coach_apr",
        "title",
        "name_display",
        "departing",
        "departing_set_at",
        "coach",
        "sport",
        "school",
        "position_types",
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
    def from_json(cls, json_str: str) -> Position:
        """Create an instance of Position from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of coach
        if self.coach:
            _dict["coach"] = self.coach.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sport
        if self.sport:
            _dict["sport"] = self.sport.to_dict()
        # override the default output from pydantic by calling `to_dict()` of school
        if self.school:
            _dict["school"] = self.school.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Position:
        """Create an instance of Position from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Position.parse_obj(obj)

        _obj = Position.parse_obj(
            {
                "id": obj.get("id"),
                "season_id": obj.get("season_id"),
                "coach_id": obj.get("coach_id"),
                "start_on": obj.get("start_on"),
                "end_on": obj.get("end_on"),
                "partial_season": obj.get("partial_season"),
                "compensation_id": obj.get("compensation_id"),
                "coach_apr": obj.get("coach_apr"),
                "title": obj.get("title"),
                "name_display": obj.get("name_display"),
                "departing": obj.get("departing"),
                "departing_set_at": obj.get("departing_set_at"),
                "coach": Coach.from_dict(obj.get("coach"))
                if obj.get("coach") is not None
                else None,
                "sport": Sport.from_dict(obj.get("sport"))
                if obj.get("sport") is not None
                else None,
                "school": School.from_dict(obj.get("school"))
                if obj.get("school") is not None
                else None,
                "position_types": obj.get("position_types"),
            }
        )
        return _obj
