class DatabaseConnection:
    
    _instance = None  
    
    def __new__(cls):
        if cls._instance is None:
            print("Создаем новое подключение к базе данных...")
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection = None
        self.is_connected = False
        self.connection_count = 0
    
    def connect(self, database_name):
        if not self.is_connected:
            self.connection = f"Connection to {database_name}"
            self.is_connected = True
            self.connection_count += 1
            print(f"Подключено к базе данных: {database_name}")
        else:
            print(f"Уже подключено к базе данных")
    
    def disconnect(self):
        if self.is_connected:
            self.connection = None
            self.is_connected = False
            print("Отключено от базы данных")
        else:
            print("Нет активного подключения")
    
    def execute_query(self, query):
        if self.is_connected:
            print(f"Выполняем запрос: {query}")
            return f"Результат: {query}"
        else:
            print("Ошибка: нет подключения к БД")
            return None
    
    def get_connection_info(self):
        return {
            "is_connected": self.is_connected,
            "connection": self.connection,
            "connection_count": self.connection_count
        }


class Logger:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
            cls._instance.log_level = "INFO"
        return cls._instance
    
    def set_log_level(self, level):
        self.log_level = level
        self.log(f"Уровень логирования изменен на {level}")
    
    def log(self, message, level="INFO"):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        levels = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
        if levels.get(level, 1) >= levels.get(self.log_level, 1):
            self.logs.append(log_entry)
            print(log_entry)
    
    def get_logs(self):
        return self.logs.copy()
    
    def clear_logs(self):
        self.logs.clear()
        print("Логи очищены")


def test_singleton():
    print("\n--- Пример 1: Подключение к базе данных ---")
  
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")
    print(f"ID db1: {id(db1)}")
    print(f"ID db2: {id(db2)}")
    
    db1.connect("university_db")
    db2.connect("students_db") 
    
    db1.execute_query("SELECT * FROM students")
    
    print(f"\nИнформация о подключении из db2:")
    info = db2.get_connection_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    print("\n--- Пример 2: Логгер приложения ---")
    
    logger1 = Logger()
    logger2 = Logger()
    
    print(f"logger1 is logger2: {logger1 is logger2}")
    

logger1.set_log_level("INFO")
    logger1.log("Приложение запущено", "INFO")
    logger2.log("Отладочная информация", "DEBUG")  # Не выведется
    logger1.log("Предупреждение", "WARNING")
    logger2.log("Ошибка", "ERROR")
    
    print(f"\nВсего записей в логе: {len(logger1.get_logs())}")
    print("Последние 3 записи:")
    for log in logger1.get_logs()[-3:]:
        print(f"  {log}")
