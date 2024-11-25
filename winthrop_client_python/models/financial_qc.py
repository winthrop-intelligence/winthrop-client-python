# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.26.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class FinancialQc(BaseModel):
    """
    FinancialQc
    """  # noqa: E501

    school_id: Optional[StrictInt] = None
    school_name: Optional[StrictStr] = None
    ncca_pdf: Optional[StrictBool] = None
    audited_pdf: Optional[StrictBool] = None
    nca_csv: Optional[StrictBool] = None
    school_info_csv: Optional[StrictBool] = None
    sport_stats_csv: Optional[StrictBool] = None
    year: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        "school_id",
        "school_name",
        "ncca_pdf",
        "audited_pdf",
        "nca_csv",
        "school_info_csv",
        "sport_stats_csv",
        "year",
    ]

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
        """Create an instance of FinancialQc from a JSON string"""
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
        """Create an instance of FinancialQc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "school_id": obj.get("school_id"),
                "school_name": obj.get("school_name"),
                "ncca_pdf": obj.get("ncca_pdf"),
                "audited_pdf": obj.get("audited_pdf"),
                "nca_csv": obj.get("nca_csv"),
                "school_info_csv": obj.get("school_info_csv"),
                "sport_stats_csv": obj.get("sport_stats_csv"),
                "year": obj.get("year"),
            }
        )
        return _obj
