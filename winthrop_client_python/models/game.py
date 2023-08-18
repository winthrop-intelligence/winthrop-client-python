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

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class Game(BaseModel):
    """
    Game
    """

    id: Optional[StrictInt] = None
    home_school_id: Optional[StrictInt] = None
    away_school_id: Optional[StrictInt] = None
    sport_id: StrictInt = Field(...)
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
    __properties = [
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
    def from_json(cls, json_str: str) -> Game:
        """Create an instance of Game from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Game:
        """Create an instance of Game from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Game.parse_obj(obj)

        _obj = Game.parse_obj(
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
