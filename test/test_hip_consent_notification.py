# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.hip_consent_notification import HIPConsentNotification


class TestHIPConsentNotification(unittest.TestCase):
    """HIPConsentNotification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HIPConsentNotification:
        """Test HIPConsentNotification
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HIPConsentNotification`
        """
        model = HIPConsentNotification()
        if include_optional:
            return HIPConsentNotification(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                notification = abdm_gateway.models.hip_consent_notification_notification.HIPConsentNotification_notification(
                    status = 'GRANTED', 
                    consent_id = '', 
                    consent_detail = abdm_gateway.models.hip_consent_notification_notification_consent_detail.HIPConsentNotification_notification_consentDetail(
                        schema_version = '', 
                        consent_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        patient = abdm_gateway.models.consent_manager_patient_id.ConsentManagerPatientID(
                            id = 'hinapatel79@ndhm', ), 
                        care_contexts = [
                            abdm_gateway.models.hip_consent_notification_notification_consent_detail_care_contexts_inner.HIPConsentNotification_notification_consentDetail_careContexts_inner(
                                patient_reference = 'hinapatel79@hospital', 
                                care_context_reference = 'Episode1', )
                            ], 
                        purpose = abdm_gateway.models.use_purpose.UsePurpose(
                            text = '', 
                            code = '', 
                            ref_uri = '', ), 
                        hip = abdm_gateway.models.hip_consent_notification_notification_consent_detail_hip.HIPConsentNotification_notification_consentDetail_hip(), 
                        consent_manager = abdm_gateway.models.hip_consent_notification_notification_consent_detail_consent_manager.HIPConsentNotification_notification_consentDetail_consentManager(), 
                        hi_types = [
                            'OPConsultation'
                            ], 
                        permission = abdm_gateway.models.permission.Permission(
                            access_mode = 'VIEW', 
                            date_range = abdm_gateway.models.permission_date_range.Permission_dateRange(
                                from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            data_erase_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            frequency = abdm_gateway.models.permission_frequency.Permission_frequency(
                                unit = 'HOUR', 
                                value = 56, 
                                repeats = 56, ), ), ), 
                    signature = 'Signature of CM as defined in W3C standards; Base64 encoded', )
            )
        else:
            return HIPConsentNotification(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                notification = abdm_gateway.models.hip_consent_notification_notification.HIPConsentNotification_notification(
                    status = 'GRANTED', 
                    consent_id = '', 
                    consent_detail = abdm_gateway.models.hip_consent_notification_notification_consent_detail.HIPConsentNotification_notification_consentDetail(
                        schema_version = '', 
                        consent_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        patient = abdm_gateway.models.consent_manager_patient_id.ConsentManagerPatientID(
                            id = 'hinapatel79@ndhm', ), 
                        care_contexts = [
                            abdm_gateway.models.hip_consent_notification_notification_consent_detail_care_contexts_inner.HIPConsentNotification_notification_consentDetail_careContexts_inner(
                                patient_reference = 'hinapatel79@hospital', 
                                care_context_reference = 'Episode1', )
                            ], 
                        purpose = abdm_gateway.models.use_purpose.UsePurpose(
                            text = '', 
                            code = '', 
                            ref_uri = '', ), 
                        hip = abdm_gateway.models.hip_consent_notification_notification_consent_detail_hip.HIPConsentNotification_notification_consentDetail_hip(), 
                        consent_manager = abdm_gateway.models.hip_consent_notification_notification_consent_detail_consent_manager.HIPConsentNotification_notification_consentDetail_consentManager(), 
                        hi_types = [
                            'OPConsultation'
                            ], 
                        permission = abdm_gateway.models.permission.Permission(
                            access_mode = 'VIEW', 
                            date_range = abdm_gateway.models.permission_date_range.Permission_dateRange(
                                from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            data_erase_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            frequency = abdm_gateway.models.permission_frequency.Permission_frequency(
                                unit = 'HOUR', 
                                value = 56, 
                                repeats = 56, ), ), ), 
                    signature = 'Signature of CM as defined in W3C standards; Base64 encoded', ),
        )
        """

    def testHIPConsentNotification(self):
        """Test HIPConsentNotification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
