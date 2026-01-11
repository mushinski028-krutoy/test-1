from uuid import UUID
from dataclasses import dataclass
from typing import Tuple
from .interfaces import OrderRepository, PaymentGateway
from domain.entities import Order
from domain.exceptions import DomainException


@dataclass
class PaymentResult:
    success: bool
    order_id: UUID
    amount_paid: str
    message: str = ""


class PayOrderUseCase:
    def __init__(self, order_repo: OrderRepository, payment_gateway: PaymentGateway):
        self.order_repo = order_repo
        self.payment_gateway = payment_gateway
    
    def execute(self, order_id: UUID) -> PaymentResult:
        try:
            order = self.order_repo.get_by_id(order_id)
            
            order.pay()
            
            payment_success = self.payment_gateway.charge(order_id, order.total_amount)
            
            if not payment_success:
                return PaymentResult(
                    success=False,
                    order_id=order_id,
                    amount_paid="0",
                    message="Payment gateway declined the transaction"
                )
            
            self.order_repo.save(order)
            
            return PaymentResult(
                success=True,
                order_id=order_id,
                amount_paid=str(order.total_amount.amount),
                message="Order paid successfully"
            )
            
        except DomainException as e:
            return PaymentResult(
                success=False,
                order_id=order_id,
                amount_paid="0",
                message=str(e)
            )
        except Exception as e:
            return PaymentResult(
                success=False,
                order_id=order_id,
                amount_paid="0",
                message=f"Unexpected error: {str(e)}"
            )
