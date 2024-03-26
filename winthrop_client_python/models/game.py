# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class Game(BaseModel):
    """
    Game
    """  # noqa: E501

    id: Optional[StrictInt] = None
    home_school_id: Optional[StrictInt] = None
    away_school_id: Optional[StrictInt] = None
    sport_id: StrictInt
    game_date: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    neutral: Optional[StrictBool] = None
    city: Optional[StrictStr] = None
    game_contract_id: Optional[StrictInt] = None
    state_id: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    in_conference: Optional[StrictBool] = None
    season_year_tbd: Optional[StrictInt] = None
    home_school_score: Optional[StrictInt] = None
    away_school_score: Optional[StrictInt] = None
    overtime: Optional[StrictInt] = None
    season_year: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "home_school_id",
        "away_school_id",
        "sport_id",
        "game_date",
        "created_at",
        "updated_at",
        "neutral",
        "city",
        "game_contract_id",
        "state_id",
        "description",
        "in_conference",
        "season_year_tbd",
        "home_school_score",
        "away_school_score",
        "overtime",
        "season_year",
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
        """Create an instance of Game from a JSON string"""
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
        """Create an instance of Game from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "home_school_id": obj.get("home_school_id"),
                "away_school_id": obj.get("away_school_id"),
                "sport_id": obj.get("sport_id"),
                "game_date": obj.get("game_date"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "neutral": obj.get("neutral"),
                "city": obj.get("city"),
                "game_contract_id": obj.get("game_contract_id"),
                "state_id": obj.get("state_id"),
                "description": obj.get("description"),
                "in_conference": obj.get("in_conference"),
                "season_year_tbd": obj.get("season_year_tbd"),
                "home_school_score": obj.get("home_school_score"),
                "away_school_score": obj.get("away_school_score"),
                "overtime": obj.get("overtime"),
                "season_year": obj.get("season_year"),
            }
        )
        return _obj
