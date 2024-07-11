# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.19.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class Contract(BaseModel):
    """
    Contract
    """  # noqa: E501

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
    __properties: ClassVar[List[str]] = [
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

    @field_validator("contractable_type")
    def contractable_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["Coach", "Person"]):
            raise ValueError("must be one of enum values ('Coach', 'Person')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Contract from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Contract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
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
