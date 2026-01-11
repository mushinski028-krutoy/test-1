from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities import Order
from domain.value_objects import Money


class OrderRepository(ABC):
    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Order:
        pass
    
    @abstractmethod
    def save(self, order: Order) -> None:
        pass


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, order_id: UUID, amount: Money) -> bool:
        pass
