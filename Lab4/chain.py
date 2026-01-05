# Пример: Система обработки заявок в техподдержку

class SupportHandler:
    """Абстрактный обработчик техподдержки"""
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler):
        """Установить следующий обработчик в цепочке"""
        self.next_handler = handler
        return handler 
    
    def handle(self, request: dict) -> str:
        """Обработать запрос или передать следующему"""
        if self.next_handler:
            return self.next_handler.handle(request)
        return "Запрос не может быть обработан"


class FirstLineSupport(SupportHandler):
    """Первая линия подержки"""
    def handle(self, request: dict) -> str:
        issue = request.get("issue", "").lower()
        complexity = request.get("complexity", 1)
        
        if complexity <= 2:
            solutions = {
                "не включается": "Проверьте подключение к розетки",
                "нет интернета": "Перезагрузите роутер",
                "завис": "Попробуйте перезагрузить устройство",
                "не печатает": "Проверьте наличие бумаги и чернил"
            }
            
            for key, solution in solutions.items():
                if key in issue:
                    return f"Первая линия: {solution}"
            
            return "Первая линия: Попробуйте основные шаги по устранению неполадок"
        
        print("Первая линия: Проблема слишком сложная, передаю второй линии")
        return super().handle(request)


class SecondLineSupport(SupportHandler):
    """Вторая линия"""
    def handle(self, request: dict) -> str:
        issue = request.get("issue", "").lower()
        complexity = request.get("complexity", 1)
        
        if 3 <= complexity <= 5:
            solutions = {
                "синий экран": "требуется обновление драйверов",
                "медленно работает": "Оптимизировал настройки, удалил временные файлы",
                "вирус": "Провел антивирусное сканирование, удалил угрозы",
                "настройка сети": "Настроил параметры сети"
            }
            
            for key, solution in solutions.items():
                if key in issue:
                    return f"Вторая линия: {solution}"
            
            return "Вторая линия: Провел диагностику и базовый ремонт"
        
        print("Вторая линия: Проблема требует эксперта, передаю специалисту")
        return super().handle(request)


class SpecialistSupport(SupportHandler):
    """Специалист"""
    def handle(self, request: dict) -> str:
        issue = request.get("issue", "").lower()
        
        solutions = {
            "потеря данных": "Восстановил данные с резервной копии",
            "аппаратная неисправность": "Заказал замену комплектующих",
            "сложная настройка": "Выполнил тонкую настройку системы",
            "интеграция": "Настроил интеграцию с другими системами"
        }
        
        for key, solution in solutions.items():
            if key in issue:
                return f"Специалист: {solution}"
        
        return "Специалист: Требуется глубокий анализ и разработка решения"


class ManagerSupport(SupportHandler):
    """Менеджер"""
    def handle(self, request: dict) -> str:
        return "Менеджер: Извините за неудобства. Мы свяжемся с вами для решения проблемы"


class Logger:
    """Базовый класс логгера"""
    def __init__(self, level: int):
        self.level = level
        self.next_logger = None
    
    def set_next(self, logger):
        self.next_logger = logger

def log_message(self, level: int, message: str):
        if self.level <= level:
            self.write(message)
        
        if self.next_logger:
            self.next_logger.log_message(level, message)
    
    def write(self, message: str):
        raise NotImplementedError


class ConsoleLogger(Logger):
    """Логгер в консоль (уровень 1: INFO)"""
    def write(self, message: str):
        print(f"[INFO] {message}")


class FileLogger(Logger):
    """Логгер в файл (уровень 2: DEBUG)"""
    def write(self, message: str):
        print(f"[DEBUG] {message} (записано в файл)")


class EmailLogger(Logger):
    """Логгер по email (уровень 3: ERROR)"""
    def write(self, message: str):
        print(f"[ERROR] {message} (отправлено по email администратору)")


def test_chain_of_responsibility():
    """Тестирование паттерна Цепочка обязанностей"""
    print("Пример 1: Система техподдержки")
    print("-" * 40)
    
    first_line = FirstLineSupport()
    second_line = SecondLineSupport()
    specialist = SpecialistSupport()
    manager = ManagerSupport()
    
    first_line.set_next(second_line).set_next(specialist).set_next(manager)
    
    requests = [
        {"issue": "Не включается компьютер", "complexity": 1},
        {"issue": "Синий экран при загрузке", "complexity": 4},
        {"issue": "Потеря важных данных после сбоя", "complexity": 8},
        {"issue": "Неизвестная проблема с оборудованием", "complexity": 10}
    ]
    
    for i, request in enumerate(requests, 1):
        print(f"\nЗапрос {i}: {request['issue']}")
        print("-" * 30)
        result = first_line.handle(request)
        print(f"Результат: {result}")
    
    print("\n" + "=" * 40)
    print("Пример 2: Система логирования")
    print("-" * 40)
    
    console_logger = ConsoleLogger(1)  
    file_logger = FileLogger(2)        
    email_logger = EmailLogger(3)      
    
    console_logger.set_next(file_logger)
    file_logger.set_next(email_logger)
    
    print("\nТест 1: Логирование INFO сообщения")
    console_logger.log_message(1, "Приложение запущено")
    
    print("\nТест 2: Логирование DEBUG сообщения")
    console_logger.log_message(2, "Пользователь выполнил действие")
    
    print("\nТест 3: Логирование ERROR сообщения")
    console_logger.log_message(3, "Критическая ошибка в системе!")
    
    print("\nВывод: Каждый обработчик в цепочке решает, может ли он обработать запрос!")
