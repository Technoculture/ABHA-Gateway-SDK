# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.patient_auth_purpose import PatientAuthPurpose

class TestPatientAuthPurpose(unittest.TestCase):
    """PatientAuthPurpose unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatientAuthPurpose(self):
        """Test PatientAuthPurpose"""
        # inst = PatientAuthPurpose()

if __name__ == '__main__':
    unittest.main()
