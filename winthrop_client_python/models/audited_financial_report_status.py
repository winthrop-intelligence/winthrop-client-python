# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator


class AuditedFinancialReportStatus(BaseModel):
    """
    AuditedFinancialReportStatus
    """

    id: Optional[StrictInt] = None
    school_id: StrictInt = Field(...)
    year: StrictInt = Field(...)
    status: Optional[StrictStr] = Field(
        None,
        description="The status of the audited financial report. Available means the report is in the system. Missing means the report is not in the system. Not Available means the report is not required for the year.",
    )
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties = ["id", "school_id", "year", "status", "created_at", "updated_at"]

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("Available", "Missing", "Not Available"):
            raise ValueError(
                "must be one of enum values ('Available', 'Missing', 'Not Available')"
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
    def from_json(cls, json_str: str) -> AuditedFinancialReportStatus:
        """Create an instance of AuditedFinancialReportStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditedFinancialReportStatus:
        """Create an instance of AuditedFinancialReportStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditedFinancialReportStatus.parse_obj(obj)

        _obj = AuditedFinancialReportStatus.parse_obj(
            {
                "id": obj.get("id"),
                "school_id": obj.get("school_id"),
                "year": obj.get("year"),
                "status": obj.get("status"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
