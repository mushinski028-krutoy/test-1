from dataclasses import dataclass, field
from decimal import Decimal
from typing import List
from uuid import UUID, uuid4
from .value_objects import Money, OrderStatus
from .exceptions import DomainException


@dataclass
class OrderLine:
    product_id: UUID
    product_name: str
    quantity: int
    unit_price: Money
    
    @property
    def total_price(self) -> Money:
        return Money(self.unit_price.amount * Decimal(self.quantity))


@dataclass
class Order:
    id: UUID
    customer_id: UUID
    lines: List[OrderLine] = field(default_factory=list)
    status: str = OrderStatus.PENDING
    _version: int = field(default=0, init=False)
    
    def __post_init__(self):
        self._validate_invariants()
    
    def add_line(self, product_id: UUID, product_name: str, quantity: int, unit_price: Money) -> None:
        if self.status == OrderStatus.PAID:
            raise DomainException("Cannot modify order after payment")
        
        self.lines.append(OrderLine(product_id, product_name, quantity, unit_price))
        self._validate_invariants()
    
    def remove_line(self, product_id: UUID) -> None:
        if self.status == OrderStatus.PAID:
            raise DomainException("Cannot modify order after payment")
        
        self.lines = [line for line in self.lines if line.product_id != product_id]
        self._validate_invariants()
    
    def pay(self) -> None:
        if self.status == OrderStatus.PAID:
            raise DomainException("Order is already paid")
        
        if not self.lines:
            raise DomainException("Cannot pay empty order")
        
        self.status = OrderStatus.PAID
        self._version += 1
    
    @property
    def total_amount(self) -> Money:
        if not self.lines:
            return Money(Decimal('0'))
        
        total = self.lines[0].total_price
        for line in self.lines[1:]:
            total = total + line.total_price
        return total
    
    def _validate_invariants(self):
        calculated_total = self.total_amount
