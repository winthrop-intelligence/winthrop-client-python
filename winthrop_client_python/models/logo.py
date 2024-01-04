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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class Logo(BaseModel):
    """
    Logo
    """

    original_url: Optional[StrictStr] = Field(
        None, description="Signed, expiring url for the original logo image"
    )
    medium_url: Optional[StrictStr] = Field(
        None, description="Signed, expiring url for the medium logo image"
    )
    small_url: Optional[StrictStr] = Field(
        None, description="Signed, expiring url for the small logo image"
    )
    __properties = ["original_url", "medium_url", "small_url"]

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
    def from_json(cls, json_str: str) -> Logo:
        """Create an instance of Logo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Logo:
        """Create an instance of Logo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Logo.parse_obj(obj)

        _obj = Logo.parse_obj(
            {
                "original_url": obj.get("original_url"),
                "medium_url": obj.get("medium_url"),
                "small_url": obj.get("small_url"),
            }
        )
        return _obj
