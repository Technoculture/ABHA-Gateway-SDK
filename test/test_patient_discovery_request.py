# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.patient_discovery_request import PatientDiscoveryRequest


class TestPatientDiscoveryRequest(unittest.TestCase):
    """PatientDiscoveryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatientDiscoveryRequest:
        """Test PatientDiscoveryRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatientDiscoveryRequest`
        """
        model = PatientDiscoveryRequest()
        if include_optional:
            return PatientDiscoveryRequest(
                request_id = '499a5a4a-7dda-4f20-9b67-e24589627061',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transaction_id = '',
                patient = abdm_gateway.models.patient_discovery_request_patient.PatientDiscoveryRequest_patient(
                    id = '<patient-id>@<consent-manager-id>', 
                    verified_identifiers = [
                        abdm_gateway.models.identifier.Identifier(
                            type = 'MR', 
                            value = '+919800083232', )
                        ], 
                    unverified_identifiers = [
                        abdm_gateway.models.identifier.Identifier(
                            value = '+919800083232', )
                        ], 
                    name = 'chandler bing', 
                    gender = 'M', 
                    year_of_birth = 2000, )
            )
        else:
            return PatientDiscoveryRequest(
                request_id = '499a5a4a-7dda-4f20-9b67-e24589627061',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transaction_id = '',
                patient = abdm_gateway.models.patient_discovery_request_patient.PatientDiscoveryRequest_patient(
                    id = '<patient-id>@<consent-manager-id>', 
                    verified_identifiers = [
                        abdm_gateway.models.identifier.Identifier(
                            type = 'MR', 
                            value = '+919800083232', )
                        ], 
                    unverified_identifiers = [
                        abdm_gateway.models.identifier.Identifier(
                            value = '+919800083232', )
                        ], 
                    name = 'chandler bing', 
                    gender = 'M', 
                    year_of_birth = 2000, ),
        )
        """

    def testPatientDiscoveryRequest(self):
        """Test PatientDiscoveryRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
