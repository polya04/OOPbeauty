from abc import ABC, abstractmethod


class VirtualAssistant:
    _instance = None
    _THEMES = ["Фізика", "Математика", "Географія", "Філологія", "Робота з текстом", "Загальні", 'Гра "історія"']

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._dialogues = []

    def answer(self):
        print(
            f"Вітаю, мене звати {VirtualAssistant.__name__}. Ви можете задати мені питання з наступних тем: математика, фізика, філологія, географія.")


class Theme(ABC):
    @abstractmethod
    def name(self):
        pass


class Math(Theme):
    @property
    def name(self):
        return "Математика"


class Physics(Theme):
    @property
    def name(self):
        return "Фізика"


class Geography(Theme):
    @property
    def name(self):
        return "Географія"


class Philology(Theme):
    @property
    def name(self):
        return "Філологія"


class General(Theme):
    @property
    def name(self):
        return "Загальні"


class Text(Theme):
    @property
    def name(self):
        return "Робота з текстом"


class Game(Theme):
    @property
    def name(self):
        return 'Гра "історія"'
