# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.hiu_consent_request_status import HIUConsentRequestStatus


class TestHIUConsentRequestStatus(unittest.TestCase):
    """HIUConsentRequestStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HIUConsentRequestStatus:
        """Test HIUConsentRequestStatus
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HIUConsentRequestStatus`
        """
        model = HIUConsentRequestStatus()
        if include_optional:
            return HIUConsentRequestStatus(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                consent_request = abdm_gateway.models.hiu_consent_request_status_consent_request.HIUConsentRequestStatus_consentRequest(
                    id = '<consent-request-id>', 
                    status = 'GRANTED', 
                    consent_artefacts = [
                        abdm_gateway.models.consent_artefact_reference.ConsentArtefactReference(
                            id = '<consent-artefact-id>', )
                        ], ),
                error = abdm_gateway.models.error.Error(
                    code = 1000, 
                    message = '', ),
                resp = abdm_gateway.models.request_reference.RequestReference(
                    request_id = '', )
            )
        else:
            return HIUConsentRequestStatus(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                resp = abdm_gateway.models.request_reference.RequestReference(
                    request_id = '', ),
        )
        """

    def testHIUConsentRequestStatus(self):
        """Test HIUConsentRequestStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
