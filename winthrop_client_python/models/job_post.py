# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from winthrop_client_python.models.category import Category


class JobPost(BaseModel):
    """
    JobPost
    """

    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    uid: StrictStr = Field(...)
    work_type: Optional[StrictStr] = None
    description: StrictStr = Field(...)
    description_md: Optional[StrictStr] = None
    salary: Optional[StrictStr] = None
    school_id: StrictInt = Field(...)
    expired: Optional[StrictBool] = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    categories: Optional[conlist(Category)] = None
    __properties = [
        "id",
        "title",
        "link",
        "uid",
        "work_type",
        "description",
        "description_md",
        "salary",
        "school_id",
        "expired",
        "created_at",
        "updated_at",
        "categories",
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
    def from_json(cls, json_str: str) -> JobPost:
        """Create an instance of JobPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict["categories"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobPost:
        """Create an instance of JobPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobPost.parse_obj(obj)

        _obj = JobPost.parse_obj(
            {
                "id": obj.get("id"),
                "title": obj.get("title"),
                "link": obj.get("link"),
                "uid": obj.get("uid"),
                "work_type": obj.get("work_type"),
                "description": obj.get("description"),
                "description_md": obj.get("description_md"),
                "salary": obj.get("salary"),
                "school_id": obj.get("school_id"),
                "expired": obj.get("expired")
                if obj.get("expired") is not None
                else False,
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "categories": [
                    Category.from_dict(_item) for _item in obj.get("categories")
                ]
                if obj.get("categories") is not None
                else None,
            }
        )
        return _obj
