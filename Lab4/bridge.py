# Пример1: Система уведомлений с разными способами отправки

class MessageSender:
    """способ отправки сообщений"""
    def send(self, message: str, recipient: str):
        raise NotImplementedError


class EmailSender(MessageSender):
    """Отправка по email"""
    def send(self, message: str, recipient: str):
        print(f"Отправка email на {recipient}: {message}")
        return f"Email отправлен на {recipient}"


class SMSSender(MessageSender):
    """Отправка SMS"""
    def send(self, message: str, recipient: str):
        print(f"Отправка SMS на {recipient}: {message[:50]}...")
        return f"SMS отправлено на {recipient}"


class PushNotificationSender(MessageSender):
    """Отправка push-уведомлений"""
    def send(self, message: str, recipient: str):
        print(f"Отправка push-уведомления для {recipient}: {message}"
        return f"Push-уведомление отправлено для {recipient}"


class Message:
    """Абстракция - сообщение"""
    def __init__(self, sender: MessageSender):
        self._sender = sender
    
    def send(self, recipient: str):
        """Отправить сообщение"""
        raise NotImplementedError


class SimpleMessage(Message):
    """Простое текстовое сообщение"""
    def __init__(self, sender: MessageSender, text: str):
        super().__init__(sender)
        self.text = text
    
    def send(self, recipient: str):
        return self._sender.send(self.text, recipient)


class HTMLMessage(Message):
    """HTML сообщение"""
    def __init__(self, sender: MessageSender, title: str, body: str):
        super().__init__(sender)
        self.title = title
        self.body = body
    
    def send(self, recipient: str):
        message = f"<h1>{self.title}</h1><p>{self.body}</p>"
        return self._sender.send(message, recipient)


class UrgentMessage(Message):
    """Срочное сообщение"""
    def __init__(self, sender: MessageSender, text: str, priority: int = 1):
        super().__init__(sender)
        self.text = text
        self.priority = priority
    
    def send(self, recipient: str):
        urgent_text = f" СРОЧНО (приоритет {self.priority}) \n{self.text}"
        return self._sender.send(urgent_text, recipient)


#пример2: Устройства и пульты 
class Device:
    """Абстракция реализации - устройство"""
    def is_enabled(self) -> bool:
        raise NotImplementedError
    
    def enable(self):
        raise NotImplementedError
    
    def disable(self):
        raise NotImplementedError
    
    def get_volume(self) -> int:
        raise NotImplementedError
    
    def set_volume(self, percent: int):
        raise NotImplementedError
    
    def get_channel(self) -> int:
        raise NotImplementedError
    
    def set_channel(self, channel: int):
        raise NotImplementedError


class TV(Device):
    """Телевизор"""
    def __init__(self):
        self._enabled = False
        self._volume = 50
        self._channel = 1
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def enable(self):
        self._enabled = True
        print(" Телевизор включен")
    
    def disable(self):
        self._enabled = False
        print(" Телевизор выключен")
    
    def get_volume(self) -> int:
        return self._volume
    
    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f"Громкость установлена на {self._volume}%")
    
    def get_channel(self) -> int:
        return self._channel
    
    def set_channel(self, channel: int):
        self._channel = max(1, min(999, channel))
        print(f"Канал установлен на {self._channel}")


class Radio(Device):
    """Радио"""
    def __init__(self):
        self._enabled = False
        self._volume = 30
        self.

t, [05.01.2026 3:23]
_frequency = 101.5 
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def enable(self):
        self._enabled = True
        print(" Радио включено")
    
    def disable(self):
        self._enabled = False
        print(" Радио выключено")
    
    def get_volume(self) -> int:
        return self._volume
    
    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f" Громкость установлена на {self._volume}%")
    
    def get_channel(self) -> float:
        return self._frequency
    
    def set_channel(self, frequency: float):
        self._frequency = max(87.5, min(108.0, frequency))
        print(f" частота установлена на {self._frequency} FM")


class RemoteControl:
    """Абстракция - пульт управления"""
    def __init__(self, device: Device):
        self._device = device
    
    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()
    
    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)
    
    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)
    
    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)
    
    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedRemoteControl(RemoteControl):
    """Продвинутый пульт управления"""
    def mute(self):
        self._device.set_volume(0)
        print(" Без звука")
    
    def set_channel_directly(self, channel: int):
        self._device.set_channel(channel)
        print(f" Прямой набор канала {channel}")


def test_bridge():
    print("Пример 1: Система уведомлений")
    print("-" * 40)
    
    email_sender = EmailSender()
    sms_sender = SMSSender()
    push_sender = PushNotificationSender()
    
    print("\n--- Тест 1: Простое сообщение разными способами ---")
    simple_msg = SimpleMessage(email_sender, "Привет! Как дела?")
    print(simple_msg.send("misos@example.com"))
    
    simple_msg._sender = sms_sender
    print(simple_msg.send("+79161234567"))
    
    simple_msg._sender = push_sender
    print(simple_msg.send("user_device_token"))
    
    print("\n--- Тест 2: Разные типы сообщений одним способом ---")
    html_msg = HTMLMessage(email_sender, "Новости", "У нас новые поступления!")
    print(html_msg.send("misis@example.com"))
    
    urgent_msg = UrgentMessage(sms_sender, "Совещание через 15 минут!", priority=2)
    print(urgent_msg.send("+7968679807"))
    
    print("\n" + "=" * 40)
    print("Пример 2: Устройства и пульты управления")
    print("-" * 40)
    
    tv = TV()
    radio = Radio()
    
    print("\n--- Тест 1: Базовый пульт для телевизора ---")
    basic_remote = RemoteControl(tv)
    basic_remote.toggle_power() 
    basic_remote.volume_up()
    basic_remote.volume_up()
    basic_remote.channel_up()
    basic_remote.channel_up()
    basic_remote.channel_up()
    
    print("\n--- Тест 2: Продвинутый пульт для радио ---")
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power() 
    advanced_remote.volume_up()
    advanced_remote.set_channel_directly(105.3)
    advanced_remote.mute()
    advanced_remote.toggle_power() 
    
    print("\n--- Тест 3: Меняем устройство у пульта ---")
    universal_remote = AdvancedRemoteControl(tv)
    universal_remote.toggle_power()
    universal_remote.set_channel_directly(25)
    
    universal_remote._device = radio
    universal_remote.toggle_power()
    universal_remote.set_channel_directly(98.7)
