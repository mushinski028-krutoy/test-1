class Computer:
    
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.motherboard = None
        self.power_supply = None
        self.cooling = None
        self.extras = []
    
    def __str__(self):
        parts = ["КОМПЬЮТЕР:"]
        
        if self.cpu:
            parts.append(f"  Процессор: {self.cpu}")
        if self.ram:
            parts.append(f"  Оперативная память: {self.ram}")
        if self.storage:
            parts.append(f"  Накопитель: {self.storage}")
        if self.gpu:
            parts.append(f"  Видеокарта: {self.gpu}")
        if self.motherboard:
            parts.append(f"  Материнская плата: {self.motherboard}")
        if self.power_supply:
            parts.append(f"  Блок питания: {self.power_supply}")
        if self.cooling:
            parts.append(f"  Охлаждение: {self.cooling}")
        if self.extras:
            parts.append(f"  Дополнительно: {', '.join(self.extras)}")
        
        parts.append(f"  Стоимость: ${self.calculate_cost()}")
        
        return "\n".join(parts)
    
    def calculate_cost(self):
        cost = 0
        
        if self.cpu:
            if "i9" in self.cpu or "Ryzen 9" in self.cpu:
                cost += 400
            elif "i7" in self.cpu or "Ryzen 7" in self.cpu:
                cost += 300
            else:
                cost += 200
        
        if self.ram:
            if "32" in self.ram:
                cost += 150
            elif "16" in self.ram:
                cost += 80
            else:
                cost += 40
        
        if self.gpu and "RTX" in self.gpu:
            if "4090" in self.gpu:
                cost += 2000
            elif "4080" in self.gpu:
                cost += 1200
            elif "4070" in self.gpu:
                cost += 600
            else:
                cost += 300
        
        if self.storage:
            if "2TB" in self.storage:
                cost += 150
            elif "1TB" in self.storage:
                cost += 80
            else:
                cost += 40
        
        if self.motherboard:
            cost += 150
        if self.power_supply:
            cost += 100
        if self.cooling:
            cost += 80
        
        cost += len(self.extras) * 20
        
        return cost


class ComputerBuilder:
    
    def __init__(self):
        self.computer = Computer()
    
    def build_cpu(self):
        raise NotImplementedError
    
    def build_ram(self):
        raise NotImplementedError
    
    def build_storage(self):
        raise NotImplementedError
    
    def build_gpu(self):
        raise NotImplementedError
    
    def build_motherboard(self):
        raise NotImplementedError
    
    def build_power_supply(self):
        raise NotImplementedError
    
    def build_cooling(self):
        raise NotImplementedError
    
    def build_extras(self):
        raise NotImplementedError
    
    def get_computer(self):
        return self.computer


class GamingComputerBuilder(ComputerBuilder):
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9-13900K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5 6000MHz"
    
    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG Maximus Z790"
    
    def build_power_supply(self):
        self.computer.power_supply = "1200W 80+ Platinum"
    
    def build_cooling(self):
        self.computer.

cooling = "Система жидкостного охлаждения"
    
    def build_extras(self):
        self.computer.extras = [
            "RGB подсветка",
            "Wi-Fi 6E",
            "Bluetooth 5.3",
            "Программируемые кнопки"
        ]


class OfficeComputerBuilder(ComputerBuilder):
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4 3200MHz"
    
    def build_storage(self):
        self.computer.storage = "512GB SSD"
    
    def build_gpu(self):
        self.computer.gpu = "Встроенная графика"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS Prime B760"
    
    def build_power_supply(self):
        self.computer.power_supply = "500W 80+ Bronze"
    
    def build_cooling(self):
        self.computer.cooling = "Стандартное воздушное охлаждение"
    
    def build_extras(self):
        self.computer.extras = [
            "Тихая работа",
            "Энергоэффективность"
        ]


class HomeComputerBuilder(ComputerBuilder):
    
    def build_cpu(self):
        self.computer.cpu = "AMD Ryzen 7 7700X"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR5 4800MHz"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4060"
    
    def build_motherboard(self):
        self.computer.motherboard = "GIGABYTE B650"
    
    def build_power_supply(self):
        self.computer.power_supply = "750W 80+ Gold"
    
    def build_cooling(self):
        self.computer.cooling = "Усиленное воздушное охлаждение"
    
    def build_extras(self):
        self.computer.extras = [
            "Wi-Fi",
            "Bluetooth",
            "Несколько портов USB"
        ]


class Director:
    
    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_basic_computer(self):
        print("Сборка базовой конфигурации...")
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_motherboard()
        self.builder.build_power_supply()
        return self.builder.get_computer()
    
    def build_standard_computer(self):
        print("Сборка стандартной конфигурации...")
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
        self.builder.build_motherboard()
        self.builder.build_power_supply()
        self.builder.build_cooling()
        return self.builder.get_computer()
    
    def build_premium_computer(self):
        print("Сборка премиум конфигурации...")
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
        self.builder.build_motherboard()
        self.builder.build_power_supply()
        self.builder.build_cooling()
        self.builder.build_extras()
        return self.builder.get_computer()


def test_builder():
    print("\n--- Пример: Система сборки компьютеров ---")
    
    director = Director()
    
    print("\n1. ИГРОВОЙ КОМПЬЮТЕР")
    print("=" * 30)
    
    gaming_builder = GamingComputerBuilder()
    director.set_builder(gaming_builder)
    
    print("\nа) Базовая конфигурация:")
    gaming_basic = director.build_basic_computer()
    print(gaming_basic)
    
    print("\nб) Премиум конфигурация:")
    gaming_premium = director.build_premium_computer()
    print(gaming_premium)
    
    print("\n2. ОФИСНЫЙ КОМПЬЮТЕР")
    print("=" * 30)
    
    office_builder = OfficeComputerBuilder()
    director.

set_builder(office_builder)
    
    office_standard = director.build_standard_computer()
    print(office_standard)
    
    print("\n3. ДОМАШНИЙ КОМПЬЮТЕР")
    print("=" * 30)
    
    home_builder = HomeComputerBuilder()
    director.set_builder(home_builder)
    
    home_premium = director.build_premium_computer()
    print(home_premium)
    
    print("\n--- Пример 2: Кастомная сборка ---")
    print("=" * 30)
    
    custom_builder = ComputerBuilder()
    custom_builder.computer = Computer()
    
    print("\nСобираю кастомный компьютер по своему усмотрению:")
    custom_builder.computer.cpu = "AMD Ryzen 5 7600X"
    custom_builder.computer.ram = "32GB DDR5 5200MHz"
    custom_builder.computer.storage = "1TB SSD + 2TB HDD"
    custom_builder.computer.gpu = "NVIDIA RTX 4070"
    custom_builder.computer.extras = ["Подсветка", "Дополнительные вентиляторы"]
    
    custom_computer = custom_builder.get_computer()
    print(custom_computer)
