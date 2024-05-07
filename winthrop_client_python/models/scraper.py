# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from winthrop_client_python.models.scraper_arg_def import ScraperArgDef
from typing import Optional, Set
from typing_extensions import Self


class Scraper(BaseModel):
    """
    Scraper
    """  # noqa: E501

    name: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    argument_defs: Optional[List[ScraperArgDef]] = Field(
        default=None, alias="argumentDefs"
    )
    __properties: ClassVar[List[str]] = ["name", "title", "argumentDefs"]

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
        """Create an instance of Scraper from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in argument_defs (list)
        _items = []
        if self.argument_defs:
            for _item in self.argument_defs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["argumentDefs"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Scraper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "title": obj.get("title"),
                "argumentDefs": [
                    ScraperArgDef.from_dict(_item) for _item in obj["argumentDefs"]
                ]
                if obj.get("argumentDefs") is not None
                else None,
            }
        )
        return _obj
