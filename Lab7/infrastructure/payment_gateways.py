from uuid import UUID
import random
from domain.value_objects import Money
from application.interfaces import PaymentGateway


class FakePaymentGateway(PaymentGateway):
    def charge(self, order_id: UUID, amount: Money) -> bool:
        return random.random() < 0.8
