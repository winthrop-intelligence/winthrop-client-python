# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class DealStatus(BaseModel):
    """
    DealStatus
    """

    id: Optional[StrictInt] = None
    school_id: StrictInt = Field(...)
    auto_renew: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source_note: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    deal_status_type_id: Optional[StrictInt] = None
    deal_type_id: StrictInt = Field(...)
    __properties = [
        "id",
        "school_id",
        "auto_renew",
        "created_at",
        "updated_at",
        "source_note",
        "note",
        "deal_status_type_id",
        "deal_type_id",
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
    def from_json(cls, json_str: str) -> DealStatus:
        """Create an instance of DealStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DealStatus:
        """Create an instance of DealStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DealStatus.parse_obj(obj)

        _obj = DealStatus.parse_obj(
            {
                "id": obj.get("id"),
                "school_id": obj.get("school_id"),
                "auto_renew": obj.get("auto_renew"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "source_note": obj.get("source_note"),
                "note": obj.get("note"),
                "deal_status_type_id": obj.get("deal_status_type_id"),
                "deal_type_id": obj.get("deal_type_id"),
            }
        )
        return _obj
