# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.20.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class Subscription(BaseModel):
    """
    Subscription
    """  # noqa: E501

    id: Optional[StrictInt] = None
    accountable_id: Optional[StrictInt] = None
    creator_id: Optional[StrictInt] = None
    start_at: Optional[date] = None
    end_at: Optional[date] = None
    amount_cents: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    subscription_type_id: Optional[StrictInt] = None
    autorenew: Optional[StrictBool] = None
    activity_cache_id: Optional[StrictInt] = None
    old_email_domain: Optional[StrictStr] = None
    account_id: Optional[StrictInt] = None
    contract_term: Optional[StrictInt] = None
    raw_contract_id: Optional[StrictInt] = None
    slug: Optional[StrictStr] = None
    contract_accepted: Optional[StrictBool] = None
    active: Optional[StrictBool] = None
    contract_accepted_ip_address: Optional[StrictStr] = None
    renewal: Optional[StrictBool] = None
    renewing: Optional[StrictBool] = None
    invoicing: Optional[StrictBool] = None
    notes: Optional[StrictStr] = None
    send_renewal: Optional[StrictBool] = None
    has_foia_clause: Optional[StrictBool] = None
    standard_agreement: Optional[StrictBool] = None
    active_users_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "accountable_id",
        "creator_id",
        "start_at",
        "end_at",
        "amount_cents",
        "created_at",
        "updated_at",
        "subscription_type_id",
        "autorenew",
        "activity_cache_id",
        "old_email_domain",
        "account_id",
        "contract_term",
        "raw_contract_id",
        "slug",
        "contract_accepted",
        "active",
        "contract_accepted_ip_address",
        "renewal",
        "renewing",
        "invoicing",
        "notes",
        "send_renewal",
        "has_foia_clause",
        "standard_agreement",
        "active_users_count",
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
        """Create an instance of Subscription from a JSON string"""
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
        """Create an instance of Subscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "accountable_id": obj.get("accountable_id"),
                "creator_id": obj.get("creator_id"),
                "start_at": obj.get("start_at"),
                "end_at": obj.get("end_at"),
                "amount_cents": obj.get("amount_cents"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "subscription_type_id": obj.get("subscription_type_id"),
                "autorenew": obj.get("autorenew"),
                "activity_cache_id": obj.get("activity_cache_id"),
                "old_email_domain": obj.get("old_email_domain"),
                "account_id": obj.get("account_id"),
                "contract_term": obj.get("contract_term"),
                "raw_contract_id": obj.get("raw_contract_id"),
                "slug": obj.get("slug"),
                "contract_accepted": obj.get("contract_accepted"),
                "active": obj.get("active"),
                "contract_accepted_ip_address": obj.get("contract_accepted_ip_address"),
                "renewal": obj.get("renewal"),
                "renewing": obj.get("renewing"),
                "invoicing": obj.get("invoicing"),
                "notes": obj.get("notes"),
                "send_renewal": obj.get("send_renewal"),
                "has_foia_clause": obj.get("has_foia_clause"),
                "standard_agreement": obj.get("standard_agreement"),
                "active_users_count": obj.get("active_users_count"),
            }
        )
        return _obj
