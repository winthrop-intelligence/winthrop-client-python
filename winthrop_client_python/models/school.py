# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from winthrop_client_python.models.school_logo import SchoolLogo


class School(BaseModel):
    """
    School
    """

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
    __properties = [
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
    def from_json(cls, json_str: str) -> School:
        """Create an instance of School from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict["logo"] = self.logo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> School:
        """Create an instance of School from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return School.parse_obj(obj)

        _obj = School.parse_obj(
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
            }
        )
        return _obj
