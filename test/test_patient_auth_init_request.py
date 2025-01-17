# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.patient_auth_init_request import PatientAuthInitRequest


class TestPatientAuthInitRequest(unittest.TestCase):
    """PatientAuthInitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatientAuthInitRequest:
        """Test PatientAuthInitRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatientAuthInitRequest`
        """
        model = PatientAuthInitRequest()
        if include_optional:
            return PatientAuthInitRequest(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                query = abdm_gateway.models.patient_auth_init_request_query.PatientAuthInitRequest_query(
                    id = 'hinapatel@ndhm', 
                    purpose = 'LINK', 
                    auth_mode = 'MOBILE_OTP', 
                    requester = abdm_gateway.models.patient_auth_requester.PatientAuthRequester(
                        type = 'HIP', 
                        id = '100005', ), )
            )
        else:
            return PatientAuthInitRequest(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                query = abdm_gateway.models.patient_auth_init_request_query.PatientAuthInitRequest_query(
                    id = 'hinapatel@ndhm', 
                    purpose = 'LINK', 
                    auth_mode = 'MOBILE_OTP', 
                    requester = abdm_gateway.models.patient_auth_requester.PatientAuthRequester(
                        type = 'HIP', 
                        id = '100005', ), ),
        )
        """

    def testPatientAuthInitRequest(self):
        """Test PatientAuthInitRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
