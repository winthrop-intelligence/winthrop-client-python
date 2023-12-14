# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr, validator


class User(BaseModel):
    """
    User
    """

    id: Optional[StrictInt] = None
    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    __properties = [
        "id",
        "email",
        "first_name",
        "last_name",
        "created_at",
        "updated_at",
        "state",
        "title",
    ]

    @validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("created", "suspended", "active", "pending"):
            raise ValueError(
                "must be one of enum values ('created', 'suspended', 'active', 'pending')"
            )
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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj(
            {
                "id": obj.get("id"),
                "email": obj.get("email"),
                "first_name": obj.get("first_name"),
                "last_name": obj.get("last_name"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "state": obj.get("state"),
                "title": obj.get("title"),
            }
        )
        return _obj
