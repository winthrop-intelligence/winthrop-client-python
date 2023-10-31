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
from pydantic import BaseModel, StrictBool, StrictInt


class NcaaFinancialReportStatus(BaseModel):
    """
    NcaaFinancialReportStatus
    """

    id: Optional[StrictInt] = None
    school_id: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    available: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties = ["id", "school_id", "year", "available", "created_at", "updated_at"]

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
    def from_json(cls, json_str: str) -> NcaaFinancialReportStatus:
        """Create an instance of NcaaFinancialReportStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NcaaFinancialReportStatus:
        """Create an instance of NcaaFinancialReportStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NcaaFinancialReportStatus.parse_obj(obj)

        _obj = NcaaFinancialReportStatus.parse_obj(
            {
                "id": obj.get("id"),
                "school_id": obj.get("school_id"),
                "year": obj.get("year"),
                "available": obj.get("available"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
