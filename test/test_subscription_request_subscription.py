# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.subscription_request_subscription import SubscriptionRequestSubscription

class TestSubscriptionRequestSubscription(unittest.TestCase):
    """SubscriptionRequestSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionRequestSubscription:
        """Test SubscriptionRequestSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionRequestSubscription`
        """
        model = SubscriptionRequestSubscription()
        if include_optional:
            return SubscriptionRequestSubscription(
                purpose = abdm_gateway.models.use_purpose.UsePurpose(
                    text = '', 
                    code = '', 
                    ref_uri = '', ),
                patient = abdm_gateway.models.consent_manager_patient_id.ConsentManagerPatientID(
                    id = 'hinapatel79@ndhm', ),
                hiu = abdm_gateway.models.organization_representation.OrganizationRepresentation(
                    id = '', ),
                hips = [
                    abdm_gateway.models.organization_representation.OrganizationRepresentation(
                        id = '', )
                    ],
                categories = [
                    'LINK'
                    ],
                period = abdm_gateway.models.subscription_period.SubscriptionPeriod(
                    from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return SubscriptionRequestSubscription(
                purpose = abdm_gateway.models.use_purpose.UsePurpose(
                    text = '', 
                    code = '', 
                    ref_uri = '', ),
                patient = abdm_gateway.models.consent_manager_patient_id.ConsentManagerPatientID(
                    id = 'hinapatel79@ndhm', ),
                hiu = abdm_gateway.models.organization_representation.OrganizationRepresentation(
                    id = '', ),
                categories = [
                    'LINK'
                    ],
                period = abdm_gateway.models.subscription_period.SubscriptionPeriod(
                    from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testSubscriptionRequestSubscription(self):
        """Test SubscriptionRequestSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
