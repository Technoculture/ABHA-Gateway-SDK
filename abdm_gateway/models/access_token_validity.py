# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from abdm_gateway.models.patient_auth_purpose import PatientAuthPurpose
from abdm_gateway.models.patient_auth_requester import PatientAuthRequester
from typing import Optional, Set
from typing_extensions import Self


class AccessTokenValidity(BaseModel):
    """
    AccessTokenValidity
    """  # noqa: E501

    purpose: PatientAuthPurpose
    requester: PatientAuthRequester
    expiry: datetime = Field(
        description="Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ"
    )
    limit: StrictInt = Field(description="number of times, the token can be used")
    __properties: ClassVar[List[str]] = ["purpose", "requester", "expiry", "limit"]

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
        """Create an instance of AccessTokenValidity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict["requester"] = self.requester.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessTokenValidity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "purpose": obj.get("purpose"),
                "requester": PatientAuthRequester.from_dict(obj["requester"])
                if obj.get("requester") is not None
                else None,
                "expiry": obj.get("expiry"),
                "limit": obj.get("limit"),
            }
        )
        return _obj
