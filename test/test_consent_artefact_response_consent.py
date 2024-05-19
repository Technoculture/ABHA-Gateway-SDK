# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.consent_artefact_response_consent import ConsentArtefactResponseConsent

class TestConsentArtefactResponseConsent(unittest.TestCase):
    """ConsentArtefactResponseConsent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsentArtefactResponseConsent:
        """Test ConsentArtefactResponseConsent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsentArtefactResponseConsent`
        """
        model = ConsentArtefactResponseConsent()
        if include_optional:
            return ConsentArtefactResponseConsent(
                status = 'GRANTED',
                consent_detail = abdm_gateway.models.consent_artefact_response_consent_consent_detail.ConsentArtefactResponse_consent_consentDetail(
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
                    hiu = abdm_gateway.models.consent_request_consent_hiu.ConsentRequest_consent_hiu(), 
                    consent_manager = abdm_gateway.models.consent_artefact_response_consent_consent_detail_consent_manager.ConsentArtefactResponse_consent_consentDetail_consentManager(), 
                    requester = abdm_gateway.models.requester.Requester(
                        name = 'Dr. Manju', 
                        identifier = abdm_gateway.models.requester_identifier.Requester_identifier(
                            type = 'REGNO', 
                            value = 'MH1001', 
                            system = 'https://www.mciindia.org', ), ), 
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
                signature = 'Signature of CM as defined in W3C standards; Base64 encoded'
            )
        else:
            return ConsentArtefactResponseConsent(
                status = 'GRANTED',
                consent_detail = abdm_gateway.models.consent_artefact_response_consent_consent_detail.ConsentArtefactResponse_consent_consentDetail(
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
                    hiu = abdm_gateway.models.consent_request_consent_hiu.ConsentRequest_consent_hiu(), 
                    consent_manager = abdm_gateway.models.consent_artefact_response_consent_consent_detail_consent_manager.ConsentArtefactResponse_consent_consentDetail_consentManager(), 
                    requester = abdm_gateway.models.requester.Requester(
                        name = 'Dr. Manju', 
                        identifier = abdm_gateway.models.requester_identifier.Requester_identifier(
                            type = 'REGNO', 
                            value = 'MH1001', 
                            system = 'https://www.mciindia.org', ), ), 
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
                signature = 'Signature of CM as defined in W3C standards; Base64 encoded',
        )
        """

    def testConsentArtefactResponseConsent(self):
        """Test ConsentArtefactResponseConsent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
