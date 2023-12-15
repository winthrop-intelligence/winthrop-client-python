# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from winthrop_client_python.models.coach import Coach
from winthrop_client_python.models.school_logo import SchoolLogo

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class School(BaseModel):
    """
    School
    """  # noqa: E501

    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    short_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    city: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    external_url: Optional[StrictStr] = None
    colors: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    primary_conference_id: Optional[StrictInt] = None
    cost_of_living_index_city_code: Optional[StrictStr] = None
    current_directors_cup_ranking: Optional[StrictInt] = None
    current_usnwr_ranking: Optional[StrictInt] = None
    private: Optional[StrictBool] = None
    school_classification_id: Optional[StrictInt] = None
    logo_updated_at: Optional[datetime] = None
    youtube_search_name: Optional[StrictStr] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    address_1: Optional[StrictStr] = None
    address_2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
    logo: Optional[SchoolLogo] = None
    athletic_director: Optional[Coach] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "short_name",
        "location",
        "created_at",
        "updated_at",
        "city",
        "nickname",
        "external_url",
        "colors",
        "state",
        "primary_conference_id",
        "cost_of_living_index_city_code",
        "current_directors_cup_ranking",
        "current_usnwr_ranking",
        "private",
        "school_classification_id",
        "logo_updated_at",
        "youtube_search_name",
        "latitude",
        "longitude",
        "address_1",
        "address_2",
        "zip_code",
        "logo",
        "athletic_director",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of School from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict["logo"] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of athletic_director
        if self.athletic_director:
            _dict["athletic_director"] = self.athletic_director.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of School from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "short_name": obj.get("short_name"),
                "location": obj.get("location"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "city": obj.get("city"),
                "nickname": obj.get("nickname"),
                "external_url": obj.get("external_url"),
                "colors": obj.get("colors"),
                "state": obj.get("state"),
                "primary_conference_id": obj.get("primary_conference_id"),
                "cost_of_living_index_city_code": obj.get(
                    "cost_of_living_index_city_code"
                ),
                "current_directors_cup_ranking": obj.get(
                    "current_directors_cup_ranking"
                ),
                "current_usnwr_ranking": obj.get("current_usnwr_ranking"),
                "private": obj.get("private"),
                "school_classification_id": obj.get("school_classification_id"),
                "logo_updated_at": obj.get("logo_updated_at"),
                "youtube_search_name": obj.get("youtube_search_name"),
                "latitude": obj.get("latitude"),
                "longitude": obj.get("longitude"),
                "address_1": obj.get("address_1"),
                "address_2": obj.get("address_2"),
                "zip_code": obj.get("zip_code"),
                "logo": SchoolLogo.from_dict(obj.get("logo"))
                if obj.get("logo") is not None
                else None,
                "athletic_director": Coach.from_dict(obj.get("athletic_director"))
                if obj.get("athletic_director") is not None
                else None,
            }
        )
        return _obj
