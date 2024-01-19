# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RequestedItem(BaseModel):
    """
    RequestedItem
    """  # noqa: E501

    id: Optional[StrictInt] = None
    foia_request_id: StrictInt
    requestable_id: StrictInt
    requestable_type: StrictStr
    received: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    coach_id: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "foia_request_id",
        "requestable_id",
        "requestable_type",
        "received",
        "created_at",
        "updated_at",
        "coach_id",
        "status",
    ]

    @field_validator("requestable_type")
    def requestable_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "DealStatus",
            "Game",
            "Compensation",
            "IncomeReport",
            "NcaaFinancialReportStatus",
            "AuditedFinancialReportStatus",
        ):
            raise ValueError(
                "must be one of enum values ('DealStatus', 'Game', 'Compensation', 'IncomeReport', 'NcaaFinancialReportStatus', 'AuditedFinancialReportStatus')"
            )
        return value

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("pending", "not_available", "received"):
            raise ValueError(
                "must be one of enum values ('pending', 'not_available', 'received')"
            )
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RequestedItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RequestedItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "foia_request_id": obj.get("foia_request_id"),
                "requestable_id": obj.get("requestable_id"),
                "requestable_type": obj.get("requestable_type"),
                "received": obj.get("received"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "coach_id": obj.get("coach_id"),
                "status": obj.get("status"),
            }
        )
        return _obj
