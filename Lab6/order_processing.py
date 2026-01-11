from typing import Dict, List, Any, Optional, Tuple

TAX_RATE = 0.21
DEFAULT_CURRENCY = "USD"

COUPON_SAVE10 = "SAVE10"
COUPON_SAVE20 = "SAVE20"
COUPON_VIP = "VIP"

DISCOUNT_RATE_10_PERCENT = 0.10
DISCOUNT_RATE_20_PERCENT = 0.20
DISCOUNT_RATE_5_PERCENT = 0.05
VIP_DISCOUNT_LARGE = 50
VIP_DISCOUNT_SMALL = 10
VIP_DISCOUNT_THRESHOLD = 100
SAVE20_DISCOUNT_THRESHOLD = 200

ERROR_USER_ID_REQUIRED = "user_id is required"
ERROR_ITEMS_REQUIRED = "items is required"
ERROR_ITEMS_NOT_LIST = "items must be a list"
ERROR_ITEMS_EMPTY = "items must not be empty"
ERROR_ITEM_MISSING_FIELDS = "item must have price and qty"
ERROR_PRICE_NOT_POSITIVE = "price must be positive"
ERROR_QTY_NOT_POSITIVE = "qty must be positive"
ERROR_UNKNOWN_COUPON = "unknown coupon"


def _parse_request(request: Dict[str, Any]) -> Tuple[Any, Any, Optional[str], str]:
    user_id = request.get("user_id")
    items = request.get("items")
    coupon = request.get("coupon")
    currency = request.get("currency", DEFAULT_CURRENCY)
    
    return user_id, items, coupon, currency


def _validate_request(user_id: Any, items: Any) -> None:
    if user_id is None:
        raise ValueError(ERROR_USER_ID_REQUIRED)
    
    if items is None:
        raise ValueError(ERROR_ITEMS_REQUIRED)
    
    if not isinstance(items, list):
        raise ValueError(ERROR_ITEMS_NOT_LIST)
    
    if len(items) == 0:
        raise ValueError(ERROR_ITEMS_EMPTY)
    
    for item in items:
        if "price" not in item or "qty" not in item:
            raise ValueError(ERROR_ITEM_MISSING_FIELDS)
        
        if item["price"] <= 0:
            raise ValueError(ERROR_PRICE_NOT_POSITIVE)
        
        if item["qty"] <= 0:
            raise ValueError(ERROR_QTY_NOT_POSITIVE)


def _calculate_subtotal(items: List[Dict[str, Any]]) -> int:
    return sum(item["price"] * item["qty"] for item in items)


def _calculate_discount(subtotal: int, coupon: Optional[str]) -> int:
    if not coupon:
        return 0
    
    discount_rules = {
        COUPON_SAVE10: lambda s: int(s * DISCOUNT_RATE_10_PERCENT),
        COUPON_SAVE20: lambda s: (
            int(s * DISCOUNT_RATE_20_PERCENT) 
            if s >= SAVE20_DISCOUNT_THRESHOLD 
            else int(s * DISCOUNT_RATE_5_PERCENT)
        ),
        COUPON_VIP: lambda s: (
            VIP_DISCOUNT_LARGE 
            if s >= VIP_DISCOUNT_THRESHOLD 
            else VIP_DISCOUNT_SMALL
        ),
    }
    
    if coupon not in discount_rules:
        raise ValueError(ERROR_UNKNOWN_COUPON)
    
    return discount_rules[coupon](subtotal)


def _calculate_tax(amount: int) -> int:
    return int(amount * TAX_RATE)


def _generate_order_id(user_id: Any, items_count: int) -> str:
    return f"{user_id}-{items_count}-X"


def process_checkout(request: Dict[str, Any]) -> Dict[str, Any]:
    user_id, items, coupon, currency = _parse_request(request)
    
    _validate_request(user_id, items)
    
    subtotal = _calculate_subtotal(items)
    discount = _calculate_discount(subtotal, coupon)
    
    total_after_discount = max(subtotal - discount, 0)
    tax = _calculate_tax(total_after_discount)
    total = total_after_discount + tax
    
order_id = _generate_order_id(user_id, len(items))
    
    return {
        "order_id": order_id,
        "user_id": user_id,
        "currency": currency,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
        "items_count": len(items),
    }
