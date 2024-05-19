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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from abdm_gateway.models.care_context_definition import CareContextDefinition
from abdm_gateway.models.consent_request_consent_hiu import ConsentRequestConsentHiu
from abdm_gateway.models.consent_request_consent_patient import ConsentRequestConsentPatient
from abdm_gateway.models.hi_type_enum import HITypeEnum
from abdm_gateway.models.hip_consent_notification_notification_consent_detail_hip import HIPConsentNotificationNotificationConsentDetailHip
from abdm_gateway.models.permission import Permission
from abdm_gateway.models.requester import Requester
from abdm_gateway.models.use_purpose import UsePurpose
from typing import Optional, Set
from typing_extensions import Self

class ConsentRequestConsent(BaseModel):
    """
    ConsentRequestConsent
    """ # noqa: E501
    purpose: UsePurpose
    patient: ConsentRequestConsentPatient
    hip: Optional[HIPConsentNotificationNotificationConsentDetailHip] = None
    care_contexts: Optional[List[CareContextDefinition]] = Field(default=None, alias="careContexts")
    hiu: ConsentRequestConsentHiu
    requester: Requester
    hi_types: List[HITypeEnum] = Field(alias="hiTypes")
    permission: Permission
    __properties: ClassVar[List[str]] = ["purpose", "patient", "hip", "careContexts", "hiu", "requester", "hiTypes", "permission"]

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
        """Create an instance of ConsentRequestConsent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of purpose
        if self.purpose:
            _dict['purpose'] = self.purpose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of patient
        if self.patient:
            _dict['patient'] = self.patient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hip
        if self.hip:
            _dict['hip'] = self.hip.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in care_contexts (list)
        _items = []
        if self.care_contexts:
            for _item in self.care_contexts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['careContexts'] = _items
        # override the default output from pydantic by calling `to_dict()` of hiu
        if self.hiu:
            _dict['hiu'] = self.hiu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permission
        if self.permission:
            _dict['permission'] = self.permission.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConsentRequestConsent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "purpose": UsePurpose.from_dict(obj["purpose"]) if obj.get("purpose") is not None else None,
            "patient": ConsentRequestConsentPatient.from_dict(obj["patient"]) if obj.get("patient") is not None else None,
            "hip": HIPConsentNotificationNotificationConsentDetailHip.from_dict(obj["hip"]) if obj.get("hip") is not None else None,
            "careContexts": [CareContextDefinition.from_dict(_item) for _item in obj["careContexts"]] if obj.get("careContexts") is not None else None,
            "hiu": ConsentRequestConsentHiu.from_dict(obj["hiu"]) if obj.get("hiu") is not None else None,
            "requester": Requester.from_dict(obj["requester"]) if obj.get("requester") is not None else None,
            "hiTypes": obj.get("hiTypes"),
            "permission": Permission.from_dict(obj["permission"]) if obj.get("permission") is not None else None
        })
        return _obj


