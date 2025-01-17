# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.hi_request import HIRequest


class TestHIRequest(unittest.TestCase):
    """HIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HIRequest:
        """Test HIRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HIRequest`
        """
        model = HIRequest()
        if include_optional:
            return HIRequest(
                request_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hi_request = abdm_gateway.models.hi_request_hi_request.HIRequest_hiRequest(
                    consent = abdm_gateway.models.consent.consent(
                        id = '', ), 
                    date_range = abdm_gateway.models.date_range.dateRange(
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    data_push_url = '', 
                    key_material = abdm_gateway.models.key_material.keyMaterial(
                        crypto_alg = 'ECDH', 
                        curve = 'Curve25519', 
                        dh_public_key = abdm_gateway.models.key_object.keyObject(
                            expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            parameters = 'Curve25519/32byte random key', 
                            key_value = '', ), 
                        nonce = '3fa85f64-5717-4562-b3fc-2c963f66afa6', ), )
            )
        else:
            return HIRequest(
                request_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hi_request = abdm_gateway.models.hi_request_hi_request.HIRequest_hiRequest(
                    consent = abdm_gateway.models.consent.consent(
                        id = '', ), 
                    date_range = abdm_gateway.models.date_range.dateRange(
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    data_push_url = '', 
                    key_material = abdm_gateway.models.key_material.keyMaterial(
                        crypto_alg = 'ECDH', 
                        curve = 'Curve25519', 
                        dh_public_key = abdm_gateway.models.key_object.keyObject(
                            expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            parameters = 'Curve25519/32byte random key', 
                            key_value = '', ), 
                        nonce = '3fa85f64-5717-4562-b3fc-2c963f66afa6', ), ),
        )
        """

    def testHIRequest(self):
        """Test HIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
