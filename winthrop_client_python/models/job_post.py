# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.17.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from winthrop_client_python.models.category import Category
from typing import Optional, Set
from typing_extensions import Self


class JobPost(BaseModel):
    """
    JobPost
    """  # noqa: E501

    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    uid: StrictStr
    work_type: Optional[StrictStr] = None
    description: StrictStr
    description_md: Optional[StrictStr] = None
    salary_summary: Optional[StrictStr] = None
    annual_salary: Optional[float] = None
    pay_period: Optional[StrictStr] = None
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    school_id: StrictInt
    required_years_of_experience: Optional[StrictInt] = None
    expired: Optional[StrictBool] = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    categories: Optional[List[Category]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "title",
        "link",
        "uid",
        "work_type",
        "description",
        "description_md",
        "salary_summary",
        "annual_salary",
        "pay_period",
        "min_salary",
        "max_salary",
        "school_id",
        "required_years_of_experience",
        "expired",
        "created_at",
        "updated_at",
        "categories",
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
        """Create an instance of JobPost from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict["categories"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "title": obj.get("title"),
                "link": obj.get("link"),
                "uid": obj.get("uid"),
                "work_type": obj.get("work_type"),
                "description": obj.get("description"),
                "description_md": obj.get("description_md"),
                "salary_summary": obj.get("salary_summary"),
                "annual_salary": obj.get("annual_salary"),
                "pay_period": obj.get("pay_period"),
                "min_salary": obj.get("min_salary"),
                "max_salary": obj.get("max_salary"),
                "school_id": obj.get("school_id"),
                "required_years_of_experience": obj.get("required_years_of_experience"),
                "expired": (
                    obj.get("expired") if obj.get("expired") is not None else False
                ),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "categories": (
                    [Category.from_dict(_item) for _item in obj["categories"]]
                    if obj.get("categories") is not None
                    else None
                ),
            }
        )
        return _obj
