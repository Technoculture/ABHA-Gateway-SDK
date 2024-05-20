# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.api.hiu_facing_api import HiuFacingApi


class TestHiuFacingApi(unittest.TestCase):
    """HiuFacingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HiuFacingApi()

    def tearDown(self) -> None:
        pass

    def test_v05_consent_requests_init_post(self) -> None:
        """Test case for v05_consent_requests_init_post

        Create consent request
        """
        pass

    def test_v05_consent_requests_status_post(self) -> None:
        """Test case for v05_consent_requests_status_post

        Get consent request status
        """
        pass

    def test_v05_consents_fetch_post(self) -> None:
        """Test case for v05_consents_fetch_post

        Get consent artefact
        """
        pass

    def test_v05_consents_hiu_on_notify_post(self) -> None:
        """Test case for v05_consents_hiu_on_notify_post

        Consent notification
        """
        pass

    def test_v05_health_information_cm_request_post(self) -> None:
        """Test case for v05_health_information_cm_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_notify_post(self) -> None:
        """Test case for v05_health_information_notify_post

        Notifications corresponding to events during data flow
        """
        pass

    def test_v05_patients_find_post(self) -> None:
        """Test case for v05_patients_find_post

        Identify a patient by her consent-manager user-id
        """
        pass

    def test_v05_patients_status_on_notify_post(self) -> None:
        """Test case for v05_patients_status_on_notify_post

        Acknowledgment by HIP/HIU
        """
        pass

    def test_v05_subscription_requests_cm_init_post(self) -> None:
        """Test case for v05_subscription_requests_cm_init_post

        Request for subscription
        """
        pass

    def test_v05_subscription_requests_hiu_on_notify_post(self) -> None:
        """Test case for v05_subscription_requests_hiu_on_notify_post

        Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
        """
        pass

    def test_v05_subscriptions_hiu_on_notify_post(self) -> None:
        """Test case for v05_subscriptions_hiu_on_notify_post

        Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
        """
        pass

    def test_v05_users_auth_confirm_post(self) -> None:
        """Test case for v05_users_auth_confirm_post

        Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
        """
        pass

    def test_v05_users_auth_fetch_modes_post(self) -> None:
        """Test case for v05_users_auth_fetch_modes_post

        Get a patient's authentication modes relevant to specified purpose
        """
        pass

    def test_v05_users_auth_init_post(self) -> None:
        """Test case for v05_users_auth_init_post

        Initialize authentication from HIP
        """
        pass

    def test_v05_users_auth_on_notify_post(self) -> None:
        """Test case for v05_users_auth_on_notify_post

        callback API by HIU/HIPs as acknowledgement of auth notification
        """
        pass


if __name__ == "__main__":
    unittest.main()
