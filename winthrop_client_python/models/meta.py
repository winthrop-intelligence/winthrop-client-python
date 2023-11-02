# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt


class Meta(BaseModel):
    """
    Meta
    """

    current_page: Optional[StrictInt] = None
    total_pages: Optional[StrictInt] = None
    total_entries: Optional[StrictInt] = None
    next_page: Optional[StrictInt] = None
    previous_page: Optional[StrictInt] = None
    __properties = [
        "current_page",
        "total_pages",
        "total_entries",
        "next_page",
        "previous_page",
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
    def from_json(cls, json_str: str) -> Meta:
        """Create an instance of Meta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Meta:
        """Create an instance of Meta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Meta.parse_obj(obj)

        _obj = Meta.parse_obj(
            {
                "current_page": obj.get("current_page"),
                "total_pages": obj.get("total_pages"),
                "total_entries": obj.get("total_entries"),
                "next_page": obj.get("next_page"),
                "previous_page": obj.get("previous_page"),
            }
        )
        return _obj
