import pytest
from uuid import uuid4
from decimal import Decimal
from domain.entities import Order, OrderLine
from domain.value_objects import Money, OrderStatus
from domain.exceptions import DomainException


class TestMoney:
    def test_money_creation(self):
        money = Money(Decimal('100.50'))
        assert money.amount == Decimal('100.50')
        assert money.currency == "USD"
    
    def test_money_addition(self):
        m1 = Money(Decimal('100'))
        m2 = Money(Decimal('50'))
        result = m1 + m2
        assert result.amount == Decimal('150')
    
    def test_money_negative_amount(self):
        with pytest.raises(ValueError):
            Money(Decimal('-10'))


class TestOrder:
    def test_create_order(self):
        order_id = uuid4()
        customer_id = uuid4()
        order = Order(order_id, customer_id)
        
        assert order.id == order_id
        assert order.customer_id == customer_id
        assert order.status == OrderStatus.PENDING
        assert len(order.lines) == 0
    
    def test_add_line_to_order(self):
        order = Order(uuid4(), uuid4())
        product_id = uuid4()
        
        order.add_line(product_id, "Test Product", 2, Money(Decimal('50')))
        
        assert len(order.lines) == 1
        assert order.lines[0].product_id == product_id
        assert order.total_amount == Money(Decimal('100'))
    
    def test_cannot_pay_empty_order(self):
        order = Order(uuid4(), uuid4())
        
        with pytest.raises(DomainException, match="Cannot pay empty order"):
            order.pay()
    
    def test_cannot_pay_paid_order(self):
        order = Order(uuid4(), uuid4())
        order.add_line(uuid4(), "Product", 1, Money(Decimal('100')))
        order.pay()
        
        with pytest.raises(DomainException, match="Order is already paid"):
            order.pay()
    
    def test_cannot_modify_after_payment(self):
        order = Order(uuid4(), uuid4())
        product_id = uuid4()
        order.add_line(product_id, "Product", 1, Money(Decimal('100')))
        order.pay()
        
        with pytest.raises(DomainException, match="Cannot modify order after payment"):
            order.add_line(uuid4(), "New Product", 1, Money(Decimal('50')))
        
        with pytest.raises(DomainException, match="Cannot modify order after payment"):
            order.remove_line(product_id)
    
    def test_total_amount_calculation(self):
        order = Order(uuid4(), uuid4())
        order.add_line(uuid4(), "Product 1", 2, Money(Decimal('30')))
        order.add_line(uuid4(), "Product 2", 1, Money(Decimal('40')))
        
        assert order.total_amount == Money(Decimal('100'))  
