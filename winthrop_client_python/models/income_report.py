# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class IncomeReport(BaseModel):
    """
    IncomeReport
    """

    id: Optional[StrictInt] = None
    coach_id: StrictInt = Field(...)
    raw_contract_id: Optional[StrictInt] = None
    year: StrictInt = Field(...)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    notes: Optional[StrictStr] = None
    contract_status_id: Optional[StrictInt] = None
    __properties = [
        "id",
        "coach_id",
        "raw_contract_id",
        "year",
        "created_at",
        "updated_at",
        "notes",
        "contract_status_id",
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
    def from_json(cls, json_str: str) -> IncomeReport:
        """Create an instance of IncomeReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncomeReport:
        """Create an instance of IncomeReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IncomeReport.parse_obj(obj)

        _obj = IncomeReport.parse_obj(
            {
                "id": obj.get("id"),
                "coach_id": obj.get("coach_id"),
                "raw_contract_id": obj.get("raw_contract_id"),
                "year": obj.get("year"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "notes": obj.get("notes"),
                "contract_status_id": obj.get("contract_status_id"),
            }
        )
        return _obj
