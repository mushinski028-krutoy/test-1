# пример:РАЗНЫЕ ВИЛКИ (несовместимые интерфейсы)

class EuropeanPlug:
    """Европейская вилка (Type C/F)"""
    
    def connect_european(self):
        print(" Европейская вилка подключена к евророзетке")
        return "230V AC"
    
    def get_voltage_eu(self)
        return 230 


class AmericanPlug:
    """Американская вилка (Type A/B)"""
    
    def plug_in_usa(self):
        print(" Американская вилка вставлена в US розетку")
        return "120V AC"
    
    def get_voltage_us(self):
        return 120


class BritishPlug:
    """Британская вилка (Type G)"""
    
    def insert_uk(self):
        print("Британская вилка вставлена в UK розетку")
        return "240V AC"
    
    def uk_voltage(self):
        return 240


class JapanesePlug:
    """Японская вилка (Type A)"""
    
    def connect_japan(self):
        print(" Японская вилка подключена")
        return "100V AC"
    
    def get_japanese_voltage(self):
        return 100


# УНИВЕРСАЛЬНАЯ РОЗЕТКА

class UniversalSocket:
    
    def __init__(self, voltage=220):
        self.voltage = voltage
        self.is_on = False
    
    def plug_in(self, voltage: int) -> str:
        if voltage == self.voltage:
            self.is_on = True
            return f"Устройство подключено к {self.voltage}V"
        elif voltage < self.voltage:
            return f"Внимание: устройство {voltage}V подключено к {self.voltage}V (нужен адаптер!)"
        else:
            return f"Ошибка: устройство {voltage}V нельзя подключать к {self.voltage}V"
    
    def unplug(self):
        """Отключить устройство"""
        self.is_on = False
        return "Устройство отключено"
    
    def check_status(self):
        """Проверить статус"""
        return f"Розетка: {'включена' if self.is_on else 'выключена'}, напряжение: {self.voltage}V"

class EuropeanToUniversalAdapter:
    """Адаптер для европейской вилки"""
    
    def __init__(self, european_plug: EuropeanPlug):
        self._plug = european_plug
    
    def plug_in(self) -> str:
        """Адаптированный метод подключения"""
        voltage = self._plug.get_voltage_eu()
        
        result = self._plug.connect_european()
        
        return f"Европейский адаптер: {result}, напряжение: {voltage}V"


class AmericanToUniversalAdapter:
    """Адаптер для американской вилки"""
    
    def __init__(self, american_plug: AmericanPlug):
        self._plug = american_plug
        self._has_voltage_converter = True
    
    def plug_in(self) -> str:
        """Адаптированный метод подключения"""
        result = self._plug.plug_in_usa()
        us_voltage = self._plug.get_voltage_us()
        
        if self._has_voltage_converter:
            converted_voltage = 220
            return f"Американский адаптер: {result} → преобразовано в {converted_voltage}V"
        else:
            return f"Американский адаптер: {result}, требуется преобразователь напряжения!"


class BritishToUniversalAdapter:
    """Адаптер для британской вилки"""
    
    def __init__(self, british_plug: BritishPlug):
        self._plug = british_plug
    
    def plug_in(self) -> str:

"""Адаптированный метод подключения"""
        result = self._plug.insert_uk()
        uk_voltage = self._plug.uk_voltage()
        
        if 220 <= uk_voltage <= 240:
            return f"Британский адаптер: {result} (совместимо с 220V)"
        else:
            return f"Британский адаптер: {result}, напряжение: {uk_voltage}V"


class JapaneseToUniversalAdapter:
    """Адаптер для японской вилки"""
    
    def __init__(self, japanese_plug: JapanesePlug):
        self._plug = japanese_plug
        self._converter_present = True
    
    def plug_in(self) -> str:
        """Адаптированный метод подключения"""
        result = self._plug.connect_japan()
        jp_voltage = self._plug.get_japanese_voltage()
        
        if self._converter_present:
            return f"Японский адаптер: {result} → преобразовано 100V→220V"
        else:
            return f"Японский адаптер: {result} - ТРЕБУЕТСЯ ПРЕОБРАЗОВАТЕЛЬ НАПРЯЖЕНИЯ!"


# УНИВЕРСАЛЬНЫЙ АДАПТЕР

class UniversalAdapter:
    """Универсальный адаптер для любых вилок"""
    
    def __init__(self):
        self._adapters = {
            'european': EuropeanToUniversalAdapter,
            'american': AmericanToUniversalAdapter,
            'british': BritishToUniversalAdapter,
            'japanese': JapaneseToUniversalAdapter
        }
        self._current_adapter = None
    
    def create_adapter(self, plug_type: str, plug):
        if plug_type in self._adapters:
            adapter_class = self._adapters[plug_type]
            self._current_adapter = adapter_class(plug)
            return f"Создан адаптер для {plug_type} вилки"
        else:
            return f"Неизвестный тип вилки: {plug_type}"
    
    def plug_in(self):
        if self._current_adapter:
            return self._current_adapter.plug_in()
        else:
            return "Сначала создайте адаптер для вилки!"
    
    def get_info(self):
        if self._current_adapter:
            return f"Текущий адаптер: {type(self._current_adapter).__name__}"
        return "Адаптер не выбран"


def test_adapter_simple():
    
    print("=" * 60)
    print("ПРИМЕР: ЭЛЕКТРИЧЕСКИЕ ВИЛКИ РАЗНЫХ СТРАН")
    print("=" * 60)
    
    print("\n1. СОЗДАЕМ ВИЛКИ РАЗНЫХ СТРАН:")
    print("-" * 40)
    
    eu_plug = EuropeanPlug()
    us_plug = AmericanPlug()
    uk_plug = BritishPlug()
    jp_plug = JapanesePlug()
    
    print("Созданы вилки: Европейская, Американская, Британская, Японская")
    
    print("\n2. СОЗДАЕМ УНИВЕРСАЛЬНУЮ РОЗЕТКУ (220V):")
    print("-" * 40)
    
    socket = UniversalSocket(voltage=220)
    print(socket.check_status())
    
    print("\n3. ПРОБУЕМ ПОДКЛЮЧИТЬ БЕЗ АДАПТЕРА:")
    print("-" * 40)
    
    print("Нельзя вызвать: socket.plug_in(eu_plug.connect_european())")
    print( Интерфейсы не совместимы!")
    
    print("\n4. СОЗДАЕМ АДАПТЕРЫ:")
    print("-" * 40)
    
    eu_adapter = EuropeanToUniversalAdapter(eu_plug)
    print(" Создан Европейский адаптер")
    
    us_adapter = AmericanToUniversalAdapter(us_plug)
    print(" Создан Американский адаптер")
    
    uk_adapter = BritishToUniversalAdapter(uk_plug)
    print("Создан Британский адаптер")
    
    jp_adapter = JapaneseToUniversalAdapter(jp_plug)
    print(" Создан Японский адаптер")
    
    print("\n5. ТЕСТИруем")

print("-" * 40)
    
    print("\na) Европейская вилка через адаптер:")
    result = eu_adapter.plug_in()
    print(f"   Результат: {result}")
    print(f"   Подключение к розетке: {socket.plug_in(230)}")
    
    print("\nb) Американская вилка через адаптер:")
    result = us_adapter.plug_in()
    print(f"   Результат: {result}")
    print(f"   Подключение к розетке: {socket.plug_in(120)}")
    
    print("\nc) Британская вилка через адаптер:")
    result = uk_adapter.plug_in()
    print(f"   Результат: {result}")
    print(f"   Подключение к розетке: {socket.plug_in(240)}")
    
    print("\nd) Японская вилка через адаптер:")
    result = jp_adapter.plug_in()
    print(f"   Результат: {result}")
    print(f"   Подключение к розетке: {socket.plug_in(100)}")
    
    print("\n6. УНИВЕРСАЛЬНЫЙ АДАПТЕР:")
    print("-" * 40)
    
    universal = UniversalAdapter()
    
    print("\na) Настраиваем для Европейской вилки:")
    print(universal.create_adapter('european', eu_plug))
    print(universal.plug_in())
    
    print("\nb) Меняем на Американскую вилку:")
    print(universal.create_adapter('american', us_plug))
    print(universal.plug_in())
