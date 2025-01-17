# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.api.data_flow_api import DataFlowApi


class TestDataFlowApi(unittest.TestCase):
    """DataFlowApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataFlowApi()

    def tearDown(self) -> None:
        pass

    def test_v05_health_information_cm_on_request_post(self) -> None:
        """Test case for v05_health_information_cm_on_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_cm_request_post(self) -> None:
        """Test case for v05_health_information_cm_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_hip_on_request_post(self) -> None:
        """Test case for v05_health_information_hip_on_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_hip_request_post(self) -> None:
        """Test case for v05_health_information_hip_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_notify_post(self) -> None:
        """Test case for v05_health_information_notify_post

        Notifications corresponding to events during data flow
        """
        pass


if __name__ == "__main__":
    unittest.main()
