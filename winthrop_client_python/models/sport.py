# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, validator


class Sport(BaseModel):
    """
    Sport
    """

    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    name_aka: Optional[StrictStr] = None
    name_display: Optional[StrictStr] = None
    gender_code: Optional[StrictStr] = None
    emerging: Optional[StrictBool] = None
    meet_sport: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties = [
        "id",
        "name",
        "name_aka",
        "name_display",
        "gender_code",
        "emerging",
        "meet_sport",
        "created_at",
        "updated_at",
    ]

    @validator("gender_code")
    def gender_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("M", "W"):
            raise ValueError("must be one of enum values ('M', 'W')")
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
    def from_json(cls, json_str: str) -> Sport:
        """Create an instance of Sport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Sport:
        """Create an instance of Sport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Sport.parse_obj(obj)

        _obj = Sport.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "name_aka": obj.get("name_aka"),
                "name_display": obj.get("name_display"),
                "gender_code": obj.get("gender_code"),
                "emerging": obj.get("emerging"),
                "meet_sport": obj.get("meet_sport"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
