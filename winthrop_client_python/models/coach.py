# coding: utf-8

"""
Winthrop Intelligence Internal API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.34.12
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from winthrop_client_python.models.avatar import Avatar
from typing import Optional, Set
from typing_extensions import Self


class Coach(BaseModel):
    """
    Coach
    """  # noqa: E501

    id: Optional[StrictInt] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    leader: Optional[StrictBool] = None
    bio: Optional[StrictStr] = None
    bio_text: Optional[StrictStr] = None
    dob: Optional[date] = None
    alma_mater_id: Optional[StrictInt] = Field(
        default=None,
        description="ID of School, You can view Alma Mater using School API",
    )
    alma_mater_year: Optional[StrictStr] = None
    hometown_city: Optional[StrictStr] = None
    hometown_state: Optional[StrictStr] = None
    twitter_handle: Optional[StrictStr] = None
    linkedin: Optional[StrictStr] = None
    instagram_handle: Optional[StrictStr] = None
    current_tenure_years: Optional[StrictInt] = None
    avatar: Optional[Avatar] = None
    years_of_experience: Optional[StrictInt] = None
    avatar_scraping_disabled: Optional[StrictBool] = None
    latest_salary: Optional[StrictInt] = None
    latest_salary_year: Optional[StrictInt] = None
    last_bio_text_updated_at: Optional[datetime] = None
    instagram_scraping_disabled: Optional[StrictBool] = None
    linkedin_scraping_disabled: Optional[StrictBool] = None
    twitter_scraping_disabled: Optional[StrictBool] = None
    email_scraping_disabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "leader",
        "bio",
        "bio_text",
        "dob",
        "alma_mater_id",
        "alma_mater_year",
        "hometown_city",
        "hometown_state",
        "twitter_handle",
        "linkedin",
        "instagram_handle",
        "current_tenure_years",
        "avatar",
        "years_of_experience",
        "avatar_scraping_disabled",
        "latest_salary",
        "latest_salary_year",
        "last_bio_text_updated_at",
        "instagram_scraping_disabled",
        "linkedin_scraping_disabled",
        "twitter_scraping_disabled",
        "email_scraping_disabled",
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
        """Create an instance of Coach from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of avatar
        if self.avatar:
            _dict["avatar"] = self.avatar.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Coach from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "first_name": obj.get("first_name"),
                "last_name": obj.get("last_name"),
                "email": obj.get("email"),
                "phone": obj.get("phone"),
                "leader": obj.get("leader"),
                "bio": obj.get("bio"),
                "bio_text": obj.get("bio_text"),
                "dob": obj.get("dob"),
                "alma_mater_id": obj.get("alma_mater_id"),
                "alma_mater_year": obj.get("alma_mater_year"),
                "hometown_city": obj.get("hometown_city"),
                "hometown_state": obj.get("hometown_state"),
                "twitter_handle": obj.get("twitter_handle"),
                "linkedin": obj.get("linkedin"),
                "instagram_handle": obj.get("instagram_handle"),
                "current_tenure_years": obj.get("current_tenure_years"),
                "avatar": (
                    Avatar.from_dict(obj["avatar"])
                    if obj.get("avatar") is not None
                    else None
                ),
                "years_of_experience": obj.get("years_of_experience"),
                "avatar_scraping_disabled": obj.get("avatar_scraping_disabled"),
                "latest_salary": obj.get("latest_salary"),
                "latest_salary_year": obj.get("latest_salary_year"),
                "last_bio_text_updated_at": obj.get("last_bio_text_updated_at"),
                "instagram_scraping_disabled": obj.get("instagram_scraping_disabled"),
                "linkedin_scraping_disabled": obj.get("linkedin_scraping_disabled"),
                "twitter_scraping_disabled": obj.get("twitter_scraping_disabled"),
                "email_scraping_disabled": obj.get("email_scraping_disabled"),
            }
        )
        return _obj
