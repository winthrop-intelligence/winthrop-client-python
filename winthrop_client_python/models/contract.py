# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, validator


class Contract(BaseModel):
    """
    Contract
    """

    id: Optional[StrictInt] = None
    executed_on: Optional[date] = None
    expires_on: Optional[date] = None
    start_on: Optional[date] = None
    end_on: Optional[date] = None
    at_will: Optional[StrictBool] = None
    verified: Optional[StrictBool] = None
    contractable_type: Optional[StrictStr] = None
    contractable_id: Optional[StrictInt] = None
    raw_contract_id: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties = [
        "id",
        "executed_on",
        "expires_on",
        "start_on",
        "end_on",
        "at_will",
        "verified",
        "contractable_type",
        "contractable_id",
        "raw_contract_id",
        "created_at",
        "updated_at",
    ]

    @validator("contractable_type")
    def contractable_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("Coach", "Person"):
            raise ValueError("must be one of enum values ('Coach', 'Person')")
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
    def from_json(cls, json_str: str) -> Contract:
        """Create an instance of Contract from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Contract:
        """Create an instance of Contract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Contract.parse_obj(obj)

        _obj = Contract.parse_obj(
            {
                "id": obj.get("id"),
                "executed_on": obj.get("executed_on"),
                "expires_on": obj.get("expires_on"),
                "start_on": obj.get("start_on"),
                "end_on": obj.get("end_on"),
                "at_will": obj.get("at_will"),
                "verified": obj.get("verified"),
                "contractable_type": obj.get("contractable_type"),
                "contractable_id": obj.get("contractable_id"),
                "raw_contract_id": obj.get("raw_contract_id"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
