# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class DealStatus(BaseModel):
    """
    DealStatus
    """  # noqa: E501

    id: Optional[StrictInt] = None
    school_id: StrictInt
    auto_renew: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source_note: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    deal_status_type_id: Optional[StrictInt] = None
    deal_type_id: StrictInt
    __properties: ClassVar[List[str]] = [
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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DealStatus from a JSON string"""
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
        """Create an instance of DealStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
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
