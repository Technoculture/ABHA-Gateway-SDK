# coding: utf-8

# flake8: noqa
"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from abdm_gateway.models.access_token_validity import AccessTokenValidity
from abdm_gateway.models.auth_confirm_identifier import AuthConfirmIdentifier
from abdm_gateway.models.auth_confirm_identifier_type import AuthConfirmIdentifierType
from abdm_gateway.models.auth_meta import AuthMeta
from abdm_gateway.models.authentication_mode import AuthenticationMode
from abdm_gateway.models.care_context import CareContext
from abdm_gateway.models.care_context_definition import CareContextDefinition
from abdm_gateway.models.care_context_representation import CareContextRepresentation
from abdm_gateway.models.certificate_or_key_get_schema import CertificateOrKeyGetSchema
from abdm_gateway.models.certs import Certs
from abdm_gateway.models.consent import Consent
from abdm_gateway.models.consent_acknowledgement import ConsentAcknowledgement
from abdm_gateway.models.consent_artefact_reference import ConsentArtefactReference
from abdm_gateway.models.consent_artefact_response import ConsentArtefactResponse
from abdm_gateway.models.consent_artefact_response_consent import ConsentArtefactResponseConsent
from abdm_gateway.models.consent_artefact_response_consent_consent_detail import ConsentArtefactResponseConsentConsentDetail
from abdm_gateway.models.consent_artefact_response_consent_consent_detail_consent_manager import ConsentArtefactResponseConsentConsentDetailConsentManager
from abdm_gateway.models.consent_fetch_request import ConsentFetchRequest
from abdm_gateway.models.consent_manager_patient_id import ConsentManagerPatientID
from abdm_gateway.models.consent_request import ConsentRequest
from abdm_gateway.models.consent_request_consent import ConsentRequestConsent
from abdm_gateway.models.consent_request_consent_hiu import ConsentRequestConsentHiu
from abdm_gateway.models.consent_request_consent_patient import ConsentRequestConsentPatient
from abdm_gateway.models.consent_request_init_response import ConsentRequestInitResponse
from abdm_gateway.models.consent_request_init_response_consent_request import ConsentRequestInitResponseConsentRequest
from abdm_gateway.models.consent_request_status_request import ConsentRequestStatusRequest
from abdm_gateway.models.consent_status import ConsentStatus
from abdm_gateway.models.date_range import DateRange
from abdm_gateway.models.endpoint import Endpoint
from abdm_gateway.models.error import Error
from abdm_gateway.models.error_response import ErrorResponse
from abdm_gateway.models.event_category_detail import EventCategoryDetail
from abdm_gateway.models.gateway_patient_status_notification import GatewayPatientStatusNotification
from abdm_gateway.models.hip_consent_notification import HIPConsentNotification
from abdm_gateway.models.hip_consent_notification_notification import HIPConsentNotificationNotification
from abdm_gateway.models.hip_consent_notification_notification_consent_detail import HIPConsentNotificationNotificationConsentDetail
from abdm_gateway.models.hip_consent_notification_notification_consent_detail_care_contexts_inner import HIPConsentNotificationNotificationConsentDetailCareContextsInner
from abdm_gateway.models.hip_consent_notification_notification_consent_detail_consent_manager import HIPConsentNotificationNotificationConsentDetailConsentManager
from abdm_gateway.models.hip_consent_notification_notification_consent_detail_hip import HIPConsentNotificationNotificationConsentDetailHip
from abdm_gateway.models.hip_consent_notification_response import HIPConsentNotificationResponse
from abdm_gateway.models.hiphi_request import HIPHIRequest
from abdm_gateway.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from abdm_gateway.models.hip_health_information_request_acknowledgement_hi_request import HIPHealthInformationRequestAcknowledgementHiRequest
from abdm_gateway.models.hi_request import HIRequest
from abdm_gateway.models.hi_request_hi_request import HIRequestHiRequest
from abdm_gateway.models.hi_type_enum import HITypeEnum
from abdm_gateway.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from abdm_gateway.models.hiu_consent_notification_event_notification import HIUConsentNotificationEventNotification
from abdm_gateway.models.hiu_consent_notification_response import HIUConsentNotificationResponse
from abdm_gateway.models.hiu_consent_request_status import HIUConsentRequestStatus
from abdm_gateway.models.hiu_consent_request_status_consent_request import HIUConsentRequestStatusConsentRequest
from abdm_gateway.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from abdm_gateway.models.hiu_health_information_request_response_hi_request import HIUHealthInformationRequestResponseHiRequest
from abdm_gateway.models.hiu_subscription import HIUSubscription
from abdm_gateway.models.hiu_subscription_context import HIUSubscriptionContext
from abdm_gateway.models.hiu_subscription_event_content import HIUSubscriptionEventContent
from abdm_gateway.models.hiu_subscription_notification import HIUSubscriptionNotification
from abdm_gateway.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
from abdm_gateway.models.hiu_subscription_notification_acknowledgment_acknowledgement import HIUSubscriptionNotificationAcknowledgmentAcknowledgement
from abdm_gateway.models.hiu_subscription_notification_event import HIUSubscriptionNotificationEvent
from abdm_gateway.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement
from abdm_gateway.models.hiu_subscription_request_notification_acknowledgement_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement
from abdm_gateway.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
from abdm_gateway.models.health_information_notification import HealthInformationNotification
from abdm_gateway.models.health_information_notification_notification import HealthInformationNotificationNotification
from abdm_gateway.models.health_information_notification_notification_notifier import HealthInformationNotificationNotificationNotifier
from abdm_gateway.models.health_information_notification_notification_status_notification import HealthInformationNotificationNotificationStatusNotification
from abdm_gateway.models.health_information_notification_notification_status_notification_status_responses_inner import HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
from abdm_gateway.models.heartbeat_response import HeartbeatResponse
from abdm_gateway.models.hip_data_notification_acknowledgement import HipDataNotificationAcknowledgement
from abdm_gateway.models.hip_data_notification_request import HipDataNotificationRequest
from abdm_gateway.models.hip_data_notification_request_notification import HipDataNotificationRequestNotification
from abdm_gateway.models.hip_data_notification_request_notification_hip import HipDataNotificationRequestNotificationHip
from abdm_gateway.models.hip_data_notification_request_notification_patient import HipDataNotificationRequestNotificationPatient
from abdm_gateway.models.identifier import Identifier
from abdm_gateway.models.identifier_type import IdentifierType
from abdm_gateway.models.key_material import KeyMaterial
from abdm_gateway.models.key_object import KeyObject
from abdm_gateway.models.link_confirmation_request import LinkConfirmationRequest
from abdm_gateway.models.link_confirmation_request_confirmation import LinkConfirmationRequestConfirmation
from abdm_gateway.models.location import Location
from abdm_gateway.models.meta import Meta
from abdm_gateway.models.open_id_configuration import OpenIdConfiguration
from abdm_gateway.models.organization_reference import OrganizationReference
from abdm_gateway.models.organization_representation import OrganizationRepresentation
from abdm_gateway.models.patient_address import PatientAddress
from abdm_gateway.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from abdm_gateway.models.patient_auth_confirm_request_credential import PatientAuthConfirmRequestCredential
from abdm_gateway.models.patient_auth_confirm_response import PatientAuthConfirmResponse
from abdm_gateway.models.patient_auth_confirm_response_auth import PatientAuthConfirmResponseAuth
from abdm_gateway.models.patient_auth_init_request import PatientAuthInitRequest
from abdm_gateway.models.patient_auth_init_request_query import PatientAuthInitRequestQuery
from abdm_gateway.models.patient_auth_init_response import PatientAuthInitResponse
from abdm_gateway.models.patient_auth_init_response_auth import PatientAuthInitResponseAuth
from abdm_gateway.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from abdm_gateway.models.patient_auth_mode_query_request_query import PatientAuthModeQueryRequestQuery
from abdm_gateway.models.patient_auth_mode_query_request_query_requester import PatientAuthModeQueryRequestQueryRequester
from abdm_gateway.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
from abdm_gateway.models.patient_auth_mode_query_response_auth import PatientAuthModeQueryResponseAuth
from abdm_gateway.models.patient_auth_notification import PatientAuthNotification
from abdm_gateway.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from abdm_gateway.models.patient_auth_notification_acknowledgement_acknowledgement import PatientAuthNotificationAcknowledgementAcknowledgement
from abdm_gateway.models.patient_auth_notification_auth import PatientAuthNotificationAuth
from abdm_gateway.models.patient_auth_purpose import PatientAuthPurpose
from abdm_gateway.models.patient_auth_requester import PatientAuthRequester
from abdm_gateway.models.patient_care_context_link import PatientCareContextLink
from abdm_gateway.models.patient_care_context_link_patient import PatientCareContextLinkPatient
from abdm_gateway.models.patient_care_context_link_request import PatientCareContextLinkRequest
from abdm_gateway.models.patient_care_context_link_response import PatientCareContextLinkResponse
from abdm_gateway.models.patient_care_context_link_response_acknowledgement import PatientCareContextLinkResponseAcknowledgement
from abdm_gateway.models.patient_demographic import PatientDemographic
from abdm_gateway.models.patient_demographic_response import PatientDemographicResponse
from abdm_gateway.models.patient_discovery_request import PatientDiscoveryRequest
from abdm_gateway.models.patient_discovery_request_patient import PatientDiscoveryRequestPatient
from abdm_gateway.models.patient_discovery_result import PatientDiscoveryResult
from abdm_gateway.models.patient_gender import PatientGender
from abdm_gateway.models.patient_identification_request import PatientIdentificationRequest
from abdm_gateway.models.patient_identification_request_query import PatientIdentificationRequestQuery
from abdm_gateway.models.patient_identification_request_query_patient import PatientIdentificationRequestQueryPatient
from abdm_gateway.models.patient_identification_request_query_requester import PatientIdentificationRequestQueryRequester
from abdm_gateway.models.patient_identification_response import PatientIdentificationResponse
from abdm_gateway.models.patient_identification_response_patient import PatientIdentificationResponsePatient
from abdm_gateway.models.patient_link_reference_request import PatientLinkReferenceRequest
from abdm_gateway.models.patient_link_reference_request_patient import PatientLinkReferenceRequestPatient
from abdm_gateway.models.patient_link_reference_result import PatientLinkReferenceResult
from abdm_gateway.models.patient_link_reference_result_link import PatientLinkReferenceResultLink
from abdm_gateway.models.patient_link_result import PatientLinkResult
from abdm_gateway.models.patient_link_result_patient import PatientLinkResultPatient
from abdm_gateway.models.patient_representation import PatientRepresentation
from abdm_gateway.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest
from abdm_gateway.models.patient_sms_notifcation_request_notification import PatientSMSNotifcationRequestNotification
from abdm_gateway.models.patient_sms_notifcation_request_notification_hip import PatientSMSNotifcationRequestNotificationHip
from abdm_gateway.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
from abdm_gateway.models.patient_status_notification import PatientStatusNotification
from abdm_gateway.models.patient_status_notification_notification import PatientStatusNotificationNotification
from abdm_gateway.models.patient_status_notification_notification_patient import PatientStatusNotificationNotificationPatient
from abdm_gateway.models.permission import Permission
from abdm_gateway.models.permission_date_range import PermissionDateRange
from abdm_gateway.models.permission_frequency import PermissionFrequency
from abdm_gateway.models.request_reference import RequestReference
from abdm_gateway.models.requester import Requester
from abdm_gateway.models.requester_identifier import RequesterIdentifier
from abdm_gateway.models.service_profile_response import ServiceProfileResponse
from abdm_gateway.models.service_role import ServiceRole
from abdm_gateway.models.session_request import SessionRequest
from abdm_gateway.models.session_response import SessionResponse
from abdm_gateway.models.share_profile_acknowledgement import ShareProfileAcknowledgement
from abdm_gateway.models.share_profile_acknowledgement1 import ShareProfileAcknowledgement1
from abdm_gateway.models.share_profile_request import ShareProfileRequest
from abdm_gateway.models.share_profile_request1 import ShareProfileRequest1
from abdm_gateway.models.share_profile_request1_intent import ShareProfileRequest1Intent
from abdm_gateway.models.share_profile_request1_profile import ShareProfileRequest1Profile
from abdm_gateway.models.share_profile_request_profile import ShareProfileRequestProfile
from abdm_gateway.models.share_profile_request_profile_patient import ShareProfileRequestProfilePatient
from abdm_gateway.models.share_profile_result import ShareProfileResult
from abdm_gateway.models.share_profile_result1 import ShareProfileResult1
from abdm_gateway.models.subscription_approval_notification import SubscriptionApprovalNotification
from abdm_gateway.models.subscription_approval_notification_notification import SubscriptionApprovalNotificationNotification
from abdm_gateway.models.subscription_category import SubscriptionCategory
from abdm_gateway.models.subscription_period import SubscriptionPeriod
from abdm_gateway.models.subscription_request import SubscriptionRequest
from abdm_gateway.models.subscription_request_subscription import SubscriptionRequestSubscription
from abdm_gateway.models.subscription_status import SubscriptionStatus
from abdm_gateway.models.use_purpose import UsePurpose
