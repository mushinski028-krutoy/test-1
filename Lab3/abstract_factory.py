from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass


class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def input(self, text):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def toggle(self):
        pass


# Продукты для Windows
class WindowsButton(Button):
    def render(self):
        return "[Windows Button]"
    
    def click(self):
        return "Windows button clicked: Playing default sound"


class WindowsTextField(TextField):
    def render(self):
        return "[Windows TextField]"
    
    def input(self, text):
        return f"Windows: '{text}' entered"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "[Windows Checkbox]"
    
    def toggle(self):
        return "Windows checkbox toggled"


# Продукты для macOS
class MacOSButton(Button):
    def render(self):
        return "[macOS Button]"
    
    def click(self):
        return "macOS button clicked: Smooth animation"


class MacOSTextField(TextField):
    def render(self):
        return "[macOS TextField]"
    
    def input(self, text):
        return f"macOS: '{text}' entered"


class MacOSCheckbox(Checkbox):
    def render(self):
        return "[macOS Checkbox]"
    
    def toggle(self):
        return "macOS checkbox toggled"


# Продукты для Linux
class LinuxButton(Button):
    def render(self):
        return "[Linux Button]"
    
    def click(self):
        return "Linux button clicked: GTK event"


class LinuxTextField(TextField):
    def render(self):
        return "[Linux TextField]"
    
    def input(self, text):
        return f"Linux: '{text}' entered"


class LinuxCheckbox(Checkbox):
    def render(self):
        return "[Linux Checkbox]"
    
    def toggle(self):
        return "Linux checkbox toggled"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_textfield(self) -> TextField:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_textfield(self) -> TextField:
        return WindowsTextField()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_textfield(self) -> TextField:
        return MacOSTextField()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_textfield(self) -> TextField:
        return LinuxTextField()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


class Application:
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.textfield = None
        self.checkbox = None
    
    def create_ui(self):
        print("Создание UI элементов...")
        self.button = self.factory.create_button()
        self.textfield = self.factory.create_textfield()
        self.checkbox = self.factory.create_checkbox()
    
    def render(self):
        print("\n--- Интерфейс ---")
        print(f"Кнопка: {self.button.render()}")
        print(f"Текстовое поле: {self.textfield.render()}")
        print(f"Чекбокс: {self.checkbox.render()}")
    
    def simulate_interaction(self):

        print("\n--- Взаимодействие ---")
        print(f"1. {self.button.click()}")
        print(f"2. {self.textfield.input('Hello, World!')}")
        print(f"3. {self.checkbox.toggle()}")


def detect_platform():
    import platform
    system = platform.system().lower()
    
    if system == "windows":
        return "windows"
    elif system == "darwin":  
        return "macos"
    else:
        return "linux" 


def test_abstract_factory():
    print("\n--- Пример: Кроссплатформенное приложение ---")
    
    platform = detect_platform()
    print(f"Обнаружена платформа: {platform}")
    
    factories = {
        "windows": ("Windows", WindowsFactory()),
        "macos": ("macOS", MacOSFactory()),
        "linux": ("Linux", LinuxFactory())
    }
    
    platform_name, factory = factories.get(platform, ("Windows", WindowsFactory()))
    
    print(f"\nСоздаем приложение для {platform_name}...")
    app = Application(factory)
    app.create_ui()
    app.render()
    app.simulate_interaction()
    
    print("\n--- Пример 2: Все стили интерфейса ---")
    
    all_factories = [
        ("Windows Style", WindowsFactory()),
        ("macOS Style", MacOSFactory()),
        ("Linux Style", LinuxFactory())
    ]
    
    for style_name, factory in all_factories:
        print(f"\n{style_name}:")
        app = Application(factory)
        app.create_ui()
        app.render()
