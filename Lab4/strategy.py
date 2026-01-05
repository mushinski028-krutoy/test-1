class PaymentStrategy:  
  def pay(self, amount: float) -> str:
        raise NotImplementedError("Этот метод должен быть переопределен")


class CreditCardPayment(PaymentStrategy):
    """Оплата кредитной картой"""
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder
    
    def pay(self, amount: float) -> str:
        last_four = self.card_number[-4:]
        return f"Оплата {amount} руб. кредитной картой ****{last_four}"


class PayPalPayment(PaymentStrategy):
    """Оплата PayPal"""
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} руб. через PayPal ({self.email})"


class BitcoinPayment(PaymentStrategy):
    """Оплата Bitcoin"""
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float) -> str:
        # Конвертируем рубли в биткоины
        btc_amount = amount / 7300000 
        return f"Оплата {btc_amount:.8f} BTC с кошелька {self.wallet_address[:10]}..."


class CashPayment(PaymentStrategy):
    """Оплата наличными"""
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} руб. наличными"


class ShoppingCart:
    """Корзина покупок, использующая стратегию оплаты"""
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item: str, price: float):
        """Добавить товар в корзину"""
        self.items.append((item, price))
        print(f"Добавлен: {item} - {price} руб.")
    
    def calculate_total(self) -> float:
        """Рассчитать общую сумму"""
        return sum(price for _, price in self.items)
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        """Установить стратегию оплаты"""
        self.payment_strategy = strategy
        print(f"Установлен способ оплаты: {strategy.__class__.__name__}")
    
    def checkout(self) -> str:
        """Оформить заказ"""
        if not self.items:
            return "Корзина пуста!"
        
        if not self.payment_strategy:
            return "Не выбран способ оплаты!"
        
        total = self.calculate_total()
        print(f"\nОформление заказа...")
        print(f"Товаров: {len(self.items)}")
        print(f"Общая сумма: {total} руб.")
        
        result = self.payment_strategy.pay(total)
        
        self.items.clear()
        
        return f"Заказ оформлен успешно! {result}"


class SortStrategy:
    """Абстрактная стратегия сортировки"""
    def sort(self, data: list) -> list:
        raise NotImplementedError


class BubbleSort(SortStrategy):
    """Пузырьковая сортировка"""
    def sort(self, data: list) -> list:
        print("Сортировка пузырьком...")
        arr = data.copy()
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


class QuickSort(SortStrategy):
    """Быстрая сортировка"""
    def sort(self, data: list) -> list:
        print("Быстрая сортировка...")
        return self._quick_sort(data.copy())
    
    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)


class Sorter:

    def __init__(self, strategy: SortStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def execute_sort(self, data: list) -> list:
        if not self.strategy:
            print("Стратегия не установлена, возвращаю исходный список")
            return data
        return self.strategy.sort(data)


def test_strategy():
    print("Пример 1: Система оплаты в интернет-магазине")
    print("-" * 40)
    
    cart = ShoppingCart()
    
    cart.add_item("Ноутбук", 75000)
    cart.add_item("Мышь", 1500)
    cart.add_item("Клавиатура", 3500)
    
    print("\n--- Тест 1: Кредитная карта ---")
    cart.set_payment_strategy(CreditCardPayment("1234567812345678", "Даниел Константинович"))
    print(cart.checkout())
    
    print("\n--- Тест 2: PayPal ---")
    cart.add_item("Наушники", 5000)
    cart.add_item("Чехол", 1000)
    cart.set_payment_strategy(PayPalPayment("misis@university.ru"))
    print(cart.checkout())
    
    print("\n--- Тест 3: Bitcoin ---")
    cart.add_item("Флешка", 800)
    cart.set_payment_strategy(BitcoinPayment("2jnjHU@Ul4jonono@Uj345jk1"))
    print(cart.checkout())
    
    print("\n" + "=" * 40)
    print("Пример 2: Стратегии сортировки")
    print("-" * 40)
    
    data = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Исходные данные: {data}")
    
    sorter = Sorter()
    
    sorter.set_strategy(BubbleSort())
    result = sorter.execute_sort(data)
    print(f"После пузырьковой сортировки: {result}")
    
    sorter.set_strategy(QuickSort())
    result = sorter.execute_sort(data)
    print(f"После быстрой сортировки: {result}")
