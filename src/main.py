"""
You can use this file to run the application.
refer to the README.md for more information.
"""
import os

from fastapi import FastAPI
from paystackapi.paystack import Paystack

app = FastAPI()

paystack = Paystack(secret_key=os.environ.get("PAYSTACK_SECRET_KEY"))


@app.get("/")
async def root():
    """
    This is the root endpoint. It will return a string.
    I am using this to test the connection to the API.

    test_connection = paystack.transaction.verify(reference="tr_1f9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9")
    test_charge = paystack.transaction.charge(amount=5000)
    test_refund = paystack.transaction.refund(amount=5000, reference="tr_1f9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c9c")
    test_plan = paystack.plan.create(name="test plan", description="test plan", amount=5000, interval="monthly", send_invoices=True, send_sms=True, currency="NGN", billing_cycles=12, plan_code="test_plan")
    test_subscription = paystack.subscription.create(plan="test_plan")
    test_subscription_list = paystack.subscription.list()
    test_subscription_retrieve = paystack.subscription.retrieve(subscription_code="sub_test_plan")
    test_subscription_update = paystack.subscription.update(subscription_code="sub_test_plan", plan="test_plan")
    test_subscription_cancel = paystack.subscription.cancel(subscription_code="sub_test_plan")
    test_subscription_resume = paystack.subscription.resume(subscription_code="sub_test_plan")
    test_subscription_reactivate = paystack.subscription.reactivate(subscription_code="sub_test_plan")
    test_subscription_get_transactions = paystack.subscription.get_transactions(subscription_code="sub_test_plan")
    test_subscription_get_customer = paystack.subscription.get_customer(subscription_code="sub_test_plan")
    test_subscription_get_customer_subscriptions = paystack.subscription.get_customer_subscriptions(customer_code="cus_test_plan")
    test_subscription_get_customer_subscription = paystack.subscription.get_customer_subscription(customer_code="cus_test_plan", subscription_code="sub_test_plan")
    """
    test_charge = paystack.transaction.charge(
        amount=100,
        email="your@gmail.com",
        currency="NGN",
        metadata={
            "custom_fields": [
                {"display_name": "Test", "variable_name": "test", "value": "test"}
            ]
        },
    )
    get_plan = paystack.plan.get(plan_id="PLN_274vqgpc8enkb3z")
    return {"message": "Hello World", "test_charge": test_charge, "get_plan": get_plan}
