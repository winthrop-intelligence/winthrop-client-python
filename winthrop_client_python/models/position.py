# coding: utf-8

"""
Winthrop Intelligence Internal API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.29.0
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
from winthrop_client_python.models.coach import Coach
from winthrop_client_python.models.position_type import PositionType
from winthrop_client_python.models.school import School
from winthrop_client_python.models.sport import Sport
from typing import Optional, Set
from typing_extensions import Self


class Position(BaseModel):
    """
    Position
    """  # noqa: E501

    id: Optional[StrictInt] = None
    season_id: Optional[StrictInt] = None
    coach_id: Optional[StrictInt] = None
    start_on: Optional[date] = None
    end_on: Optional[date] = None
    partial_season: Optional[StrictBool] = None
    compensation_id: Optional[StrictInt] = None
    coach_apr: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    name_display: Optional[StrictStr] = None
    departing: Optional[StrictBool] = None
    departing_set_at: Optional[datetime] = None
    creation_reason: Optional[StrictStr] = None
    creation_reason_updated_at: Optional[datetime] = None
    coach: Optional[Coach] = None
    sport: Optional[Sport] = None
    school: Optional[School] = None
    article_link: Optional[StrictStr] = None
    article_title: Optional[StrictStr] = None
    article_description: Optional[StrictStr] = None
    article_site_name: Optional[StrictStr] = None
    article_publish_time: Optional[StrictStr] = None
    article_image_url: Optional[StrictStr] = None
    position_types: Optional[List[PositionType]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "season_id",
        "coach_id",
        "start_on",
        "end_on",
        "partial_season",
        "compensation_id",
        "coach_apr",
        "title",
        "name_display",
        "departing",
        "departing_set_at",
        "creation_reason",
        "creation_reason_updated_at",
        "coach",
        "sport",
        "school",
        "article_link",
        "article_title",
        "article_description",
        "article_site_name",
        "article_publish_time",
        "article_image_url",
        "position_types",
    ]

    @field_validator("creation_reason")
    def creation_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["renewed", "new_hire", "promotion", "extension", "null"]):
            raise ValueError(
                "must be one of enum values ('renewed', 'new_hire', 'promotion', 'extension', 'null')"
            )
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
        """Create an instance of Position from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of coach
        if self.coach:
            _dict["coach"] = self.coach.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sport
        if self.sport:
            _dict["sport"] = self.sport.to_dict()
        # override the default output from pydantic by calling `to_dict()` of school
        if self.school:
            _dict["school"] = self.school.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in position_types (list)
        _items = []
        if self.position_types:
            for _item in self.position_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict["position_types"] = _items
        # set to None if creation_reason (nullable) is None
        # and model_fields_set contains the field
        if self.creation_reason is None and "creation_reason" in self.model_fields_set:
            _dict["creation_reason"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Position from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "season_id": obj.get("season_id"),
                "coach_id": obj.get("coach_id"),
                "start_on": obj.get("start_on"),
                "end_on": obj.get("end_on"),
                "partial_season": obj.get("partial_season"),
                "compensation_id": obj.get("compensation_id"),
                "coach_apr": obj.get("coach_apr"),
                "title": obj.get("title"),
                "name_display": obj.get("name_display"),
                "departing": obj.get("departing"),
                "departing_set_at": obj.get("departing_set_at"),
                "creation_reason": obj.get("creation_reason"),
                "creation_reason_updated_at": obj.get("creation_reason_updated_at"),
                "coach": (
                    Coach.from_dict(obj["coach"])
                    if obj.get("coach") is not None
                    else None
                ),
                "sport": (
                    Sport.from_dict(obj["sport"])
                    if obj.get("sport") is not None
                    else None
                ),
                "school": (
                    School.from_dict(obj["school"])
                    if obj.get("school") is not None
                    else None
                ),
                "article_link": obj.get("article_link"),
                "article_title": obj.get("article_title"),
                "article_description": obj.get("article_description"),
                "article_site_name": obj.get("article_site_name"),
                "article_publish_time": obj.get("article_publish_time"),
                "article_image_url": obj.get("article_image_url"),
                "position_types": (
                    [PositionType.from_dict(_item) for _item in obj["position_types"]]
                    if obj.get("position_types") is not None
                    else None
                ),
            }
        )
        return _obj
