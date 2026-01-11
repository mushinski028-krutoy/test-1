import pytest
from uuid import uuid4
from decimal import Decimal
from unittest.mock import Mock, patch
from domain.entities import Order
from domain.value_objects import Money
from application.use_cases import PayOrderUseCase, PaymentResult
from infrastructure.repositories import InMemoryOrderRepository
from infrastructure.payment_gateways import FakePaymentGateway


class TestPayOrderUseCase:
    @pytest.fixture
    def setup(self):
        self.order_repo = InMemoryOrderRepository()
        self.payment_gateway = FakePaymentGateway()
        self.use_case = PayOrderUseCase(self.order_repo, self.payment_gateway)
        
        self.order_id = uuid4()
        self.customer_id = uuid4()
        order = Order(self.order_id, self.customer_id)
        order.add_line(uuid4(), "Test Product", 2, Money(Decimal('50')))
        self.order_repo.save(order)
        
        return self.order_repo, self.payment_gateway, self.use_case
    
    def test_successful_payment(self, setup):
        with patch.object(self.payment_gateway, 'charge', return_value=True):
            result = self.use_case.execute(self.order_id)
            
            assert result.success is True
            assert result.order_id == self.order_id
            assert result.amount_paid == "100"
            assert "successfully" in result.message
            
            updated_order = self.order_repo.get_by_id(self.order_id)
            assert updated_order.status == "paid"
    
    def test_payment_empty_order(self, setup):
        empty_order_id = uuid4()
        empty_order = Order(empty_order_id, uuid4())
        self.order_repo.save(empty_order)
        
        result = self.use_case.execute(empty_order_id)
        
        assert result.success is False
        assert "Cannot pay empty order" in result.message
    
    def test_double_payment_error(self, setup):
        with patch.object(self.payment_gateway, 'charge', return_value=True):
            result1 = self.use_case.execute(self.order_id)
            assert result1.success is True
        
        result2 = self.use_case.execute(self.order_id)
        assert result2.success is False
        assert "already paid" in result2.message.lower()
    
    def test_payment_gateway_declined(self, setup):
        with patch.object(self.payment_gateway, 'charge', return_value=False):
            result = self.use_case.execute(self.order_id)
            
            assert result.success is False
            assert "declined" in result.message.lower()
            
            order = self.order_repo.get_by_id(self.order_id)
    
    def test_total_amount_calculation_in_use_case(self, setup):
        order = self.order_repo.get_by_id(self.order_id)
        expected_total = order.total_amount
        
        with patch.object(self.payment_gateway, 'charge') as mock_charge:
            mock_charge.return_value = True
            result = self.use_case.execute(self.order_id)

          
            mock_charge.assert_called_once()
            call_args = mock_charge.call_args[0]
            assert call_args[0] == self.order_id
            assert call_args[1] == expected_total


def test_payment_result_structure():
    order_id = uuid4()
    result = PaymentResult(
        success=True,
        order_id=order_id,
        amount_paid="100.50",
        message="Success"
    )
    
    assert result.success is True
    assert result.order_id == order_id
    assert result.amount_paid == "100.50"
    assert result.message == "Success"
