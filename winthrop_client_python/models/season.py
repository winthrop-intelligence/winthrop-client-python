# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from winthrop_client_python.models.coach import Coach

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Season(BaseModel):
    """
    Season
    """  # noqa: E501

    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    school_id: Optional[StrictInt] = None
    sport_id: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    wins: Optional[StrictInt] = None
    losses: Optional[StrictInt] = None
    conference_wins: Optional[StrictInt] = None
    conference_losses: Optional[StrictInt] = None
    apr: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    win_percent: Optional[Union[StrictFloat, StrictInt]] = None
    ties: Optional[StrictInt] = None
    rpi: Optional[StrictInt] = None
    prev_rpi: Optional[StrictInt] = None
    conference_position: Optional[StrictInt] = None
    conference_num_positions: Optional[StrictInt] = None
    coach_apr: Optional[StrictInt] = None
    attendance: Optional[StrictInt] = None
    conference_ties: Optional[StrictInt] = None
    recruit_ranking: Optional[StrictInt] = None
    offensive_efficiency: Optional[Union[StrictFloat, StrictInt]] = None
    defensive_efficiency: Optional[Union[StrictFloat, StrictInt]] = None
    sos_ranking: Optional[StrictInt] = None
    sos: Optional[Union[StrictFloat, StrictInt]] = None
    home_wins: Optional[StrictInt] = None
    home_losses: Optional[StrictInt] = None
    home_win_percent: Optional[Union[StrictFloat, StrictInt]] = None
    asr: Optional[StrictInt] = None
    head_coach: Optional[Coach] = None
    assistant_coaches: Optional[List[Coach]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "description",
        "school_id",
        "sport_id",
        "year",
        "wins",
        "losses",
        "conference_wins",
        "conference_losses",
        "apr",
        "created_at",
        "updated_at",
        "win_percent",
        "ties",
        "rpi",
        "prev_rpi",
        "conference_position",
        "conference_num_positions",
        "coach_apr",
        "attendance",
        "conference_ties",
        "recruit_ranking",
        "offensive_efficiency",
        "defensive_efficiency",
        "sos_ranking",
        "sos",
        "home_wins",
        "home_losses",
        "home_win_percent",
        "asr",
        "head_coach",
        "assistant_coaches",
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
        """Create an instance of Season from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of head_coach
        if self.head_coach:
            _dict["head_coach"] = self.head_coach.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assistant_coaches (list)
        _items = []
        if self.assistant_coaches:
            for _item in self.assistant_coaches:
                if _item:
                    _items.append(_item.to_dict())
            _dict["assistant_coaches"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Season from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "school_id": obj.get("school_id"),
                "sport_id": obj.get("sport_id"),
                "year": obj.get("year"),
                "wins": obj.get("wins"),
                "losses": obj.get("losses"),
                "conference_wins": obj.get("conference_wins"),
                "conference_losses": obj.get("conference_losses"),
                "apr": obj.get("apr"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "win_percent": obj.get("win_percent"),
                "ties": obj.get("ties"),
                "rpi": obj.get("rpi"),
                "prev_rpi": obj.get("prev_rpi"),
                "conference_position": obj.get("conference_position"),
                "conference_num_positions": obj.get("conference_num_positions"),
                "coach_apr": obj.get("coach_apr"),
                "attendance": obj.get("attendance"),
                "conference_ties": obj.get("conference_ties"),
                "recruit_ranking": obj.get("recruit_ranking"),
                "offensive_efficiency": obj.get("offensive_efficiency"),
                "defensive_efficiency": obj.get("defensive_efficiency"),
                "sos_ranking": obj.get("sos_ranking"),
                "sos": obj.get("sos"),
                "home_wins": obj.get("home_wins"),
                "home_losses": obj.get("home_losses"),
                "home_win_percent": obj.get("home_win_percent"),
                "asr": obj.get("asr"),
                "head_coach": Coach.from_dict(obj.get("head_coach"))
                if obj.get("head_coach") is not None
                else None,
                "assistant_coaches": [
                    Coach.from_dict(_item) for _item in obj.get("assistant_coaches")
                ]
                if obj.get("assistant_coaches") is not None
                else None,
            }
        )
        return _obj
