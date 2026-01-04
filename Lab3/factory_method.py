from abc import ABC, abstractmethod

class Document(ABC):
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def get_type(self):
        pass


class PDFDocument(Document):
    
    def create(self):
        return 
    
    def open(self):
        return 
    
    def save(self):
        return 
    
    def get_type(self):
        return 
    
    def add_password(self):
        return 


class WordDocument(Document):
    
    def create(self):
        return 
    
    def open(self):
        return 
    
    def save(self):
        return 
    
    def get_type(self):
        return 
    
    def add_header(self, text):
        return f"Добавлен заголовок: {text}"


class ExcelDocument(Document):
    
    def create(self):
        return 
    
    def open(self):
        return 
    
    def save(self):
        return 
    
    def get_type(self):
        return 
    
    def add_formula(self, formula):
        return f"Добавлена формула: {formula}"


class DocumentCreator(ABC):
    
    @abstractmethod
    def create_document(self) -> Document:
        pass
    
    def process_document(self):
        document = self.create_document()
        
        print(f"Тип документа: {document.get_type()}")
        print(f"1. {document.create()}")
        print(f"2. {document.open()}")
        print(f"3. {document.save()}")
        
        if isinstance(document, PDFDocument):
            print(f"4. {document.add_password()}")
        elif isinstance(document, WordDocument):
            print(f"4. {document.add_header('Лабораторная работа')}")
        elif isinstance(document, ExcelDocument):
            print(f"4. {document.add_formula('=SUM(A1:A10)')}")
        
        return document


class PDFCreator(DocumentCreator):
    
    def create_document(self) -> Document:
        return PDFDocument()


class WordCreator(DocumentCreator):
    
    def create_document(self) -> Document:
        return WordDocument()


class ExcelCreator(DocumentCreator):
    
    def create_document(self) -> Document:
        return ExcelDocument()


def test_factory_method():
    print("\n--- Пример: Система обработки документов ---")
    
    creators = [
        ("PDF документ", PDFCreator()),
        ("Word документ", WordCreator()),
        ("Excel таблица", ExcelCreator())
    ]
    
    for doc_type, creator in creators:
        print(f"\n{doc_type}:")
        print("-" * 30)
        creator.process_document()
    
    print("\n--- Пример 2: Динамическое создание ---")
    
    document_types = {
        "1": ("PDF", PDFCreator()),
        "2": ("Word", WordCreator()),
        "3": ("Excel", ExcelCreator())
    }
    
    print("\nВыберите тип документа:")
    for key, (name, _) in document_types.items():

print(f"{key}. {name}")
    
    choice = input("Введите номер: ")
    
    if choice in document_types:
        name, creator = document_types[choice]
        print(f"\nСоздаем {name} документ:")
        document = creator.create_document()
        print(f"Документ создан: {document.create()}")
        print(f"Тип: {document.get_type()}")
    else:
        print("Неверный выбор")
