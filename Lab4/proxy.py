# Пример1: Прокси для доступа к базе данных

class Database:
    """Реальный объект - база данных"""
    def __init__(self):
        self._data = {
            1: {"name": "Иван Иванов", "age": 25, "salary": 50000},
            2: {"name": "Петр Петров", "age": 30, "salary": 70000},
            3: {"name": "Сергей Сергеев", "age": 35, "salary": 90000}
        }
        print("База данных инициализирована (дорогая операция)")
    
    def get_employee(self, emp_id: int):
        """Получить данные сотрудника"""
        print(f"Запрос к реальной БД для сотрудника {emp_id}")
        return self._data.get(emp_id)
    
    def update_salary(self, emp_id: int, new_salary: float):
        """Обновить зарплату сотрудника"""
        print(f"Обновление зарплаты в реальной БД для сотрудника {emp_id}")
        if emp_id in self._data:
            self._data[emp_id]["salary"] = new_salary
            return True
        return False


class DatabaseProxy:
    def __init__(self, database: Database):
        self._database = database
        self._cache = {}  
        self._access_log = [] 
        self._admin_password = "admin123"  
    
    def get_employee(self, emp_id: int, user_role: str = "user"):
        """Получить данные сотрудника через прокси"""
        self._log_access(f"Запрос данных сотрудника {emp_id}", user_role)
        
        if user_role != "admin":
            print("Предупреждение: Неполные данные (скрыта зарплата)")
        
        if emp_id in self._cache:
            print(f"Данные из кэша для сотрудника {emp_id}")
            data = self._cache[emp_id].copy()
        else:
            data = self._database.get_employee(emp_id)
            if data:
                self._cache[emp_id] = data.copy()
        
        if data and user_role != "admin":
            data = data.copy()
            data.pop("salary", None)
        
        return data
    
    def update_salary(self, emp_id: int, new_salary: float, password: str):
        self._log_access(f"Попытка обновления зарплаты сотрудника {emp_id}", "admin")
        
        if password != self._admin_password:
            print("Ошибка: Неверный пароль администратора")
            return False
        
        if emp_id in self._cache:
            del self._cache[emp_id]
        
        success = self._database.update_salary(emp_id, new_salary)
        
        if success:
            print(f"Зарплата сотрудника {emp_id} успешно обновлена")
        
        return success
    
    def _log_access(self, action: str, user_role: str)
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {user_role}: {action}"
        self._access_log.append(log_entry)
    
    def get_access_log(self, password: str):
        """Получить лог доступа"""
        if password == self._admin_password:
            return self._access_log
        else:
            print("Ошибка: Недостаточно прав для просмотра лога")
            return []


#пример2: прокси для изображений
class Image:
    def __init__(self, filename: str):
        self._filename = filename
        self._load_image()
    
    def _load_image(self):
        print(f"Загрузка изображения {self._filename}...")
        self.

_image_data = f"Данные изображения {self._filename}"
    
    def display(self):
        print(f"Отображение: {self._filename}")
        return self._image_data


class ImageProxy:
    """Прокси для изображения"""
    def __init__(self, filename: str):
        self._filename = filename
        self._real_image = None
        self._loaded = False
    
    def display(self):
        if not self._loaded:
            self._real_image = Image(self._filename)
            self._loaded = True
            print("(Изображение загружено)")
        else:
            print("(Изображение уже загружено, используем кэш)")
        
        return self._real_image.display()


def test_proxy():
    print("Пример 1: Прокси для базы данных сотрудников")
    print("-" * 40)
    
    real_db = Database()
    db_proxy = DatabaseProxy(real_db)
    
    print("\n--- Тест 1: Обычный пользователь ---")
    emp_data = db_proxy.get_employee(1, "user")
    print(f"Данные сотрудника 1: {emp_data}")

print("\n--- Тест 2: Администратор ---")
    emp_data = db_proxy.get_employee(1, "admin")
    print(f"Данные сотрудника 1: {emp_data}")
    
    print("\n--- Тест 3: Повторный запрос (кэширование) ---")
    emp_data = db_proxy.get_employee(1, "admin")
    
    print("\n--- Тест 4: Обновление зарплаты ---")
    success = db_proxy.update_salary(1, 55000, "wrongpass")
    print(f"Обновление с неверным паролем: {'Успех' if success else 'Неудача'}")
    
    success = db_proxy.update_salary(1, 55000, "admin123")
    print(f"Обновление с верным паролем: {'Успех' if success else 'Неудача'}")
    
    print("\n--- Тест 5: Просмотр лога ---")
    log = db_proxy.get_access_log("admin123")
    print("Лог доступа к БД:")
    for entry in log[-3:]:  
        print(f"  {entry}")
    
    print("\n" + "=" * 40)
    print("Пример 2:прокси для изображений")
    print("-" * 40)
    
    print("\nСоздаем прокси для изображений (само изображение не загружается):")
    image1 = ImageProxy("photo1.jpg")
    image2 = ImageProxy("photo2.jpg")
    image3 = ImageProxy("photo3.jpg")
    
    print("\nДобавляем изображения в галерею...")
    gallery = [image1, image2, image3]
    
    print("\nПоказываем галерею (изображения загружаются по требованию):")
    for i, img in enumerate(gallery, 1):
        print(f"\nИзображение {i}:")
        img.display()
    
    print("\nПоказываем снова (используем загруженные изображения):")
    image1.display() 
