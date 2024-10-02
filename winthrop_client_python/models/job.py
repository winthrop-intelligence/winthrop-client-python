# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.23.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from winthrop_client_python.models.job_department import JobDepartment
from winthrop_client_python.models.job_school import JobSchool
from winthrop_client_python.models.job_sport import JobSport
from typing import Optional, Set
from typing_extensions import Self


class Job(BaseModel):
    """
    Job
    """  # noqa: E501

    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    job_url: Optional[StrictStr] = None
    posted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    school: Optional[JobSchool] = None
    departments: Optional[List[JobDepartment]] = None
    sports: Optional[List[JobSport]] = None
    __properties: ClassVar[List[str]] = [
        "title",
        "description",
        "job_url",
        "posted_at",
        "created_at",
        "school",
        "departments",
        "sports",
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
        """Create an instance of Job from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of school
        if self.school:
            _dict["school"] = self.school.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in departments (list)
        _items = []
        if self.departments:
            for _item in self.departments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["departments"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sports (list)
        _items = []
        if self.sports:
            for _item in self.sports:
                if _item:
                    _items.append(_item.to_dict())
            _dict["sports"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "title": obj.get("title"),
                "description": obj.get("description"),
                "job_url": obj.get("job_url"),
                "posted_at": obj.get("posted_at"),
                "created_at": obj.get("created_at"),
                "school": (
                    JobSchool.from_dict(obj["school"])
                    if obj.get("school") is not None
                    else None
                ),
                "departments": (
                    [JobDepartment.from_dict(_item) for _item in obj["departments"]]
                    if obj.get("departments") is not None
                    else None
                ),
                "sports": (
                    [JobSport.from_dict(_item) for _item in obj["sports"]]
                    if obj.get("sports") is not None
                    else None
                ),
            }
        )
        return _obj
