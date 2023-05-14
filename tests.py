from abc import ABC, abstractmethod
import math


class Theme(ABC):
    _themes = []

    @abstractmethod
    def name(self):
        pass

    def action(self):
        return f"Ви обрали тему {self.name}. Ви можете задати  мені питання з наступних" \
               f" тем: {', '.join(self._themes[:-1]) + self._themes[-1]}. "

    @property
    def themes(self):
        return self._themes


class Math(Theme):
    @property
    def name(self):
        return "Математика"


class Physics(Theme):
    _themes = ["Вивести гравітаційну сталу"]

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


class G(Physics):
    def action(self):
        return "G is approximately 6.67430 × 10-11 N(m/kg)^2"


class Coulomb(Physics):
    def action(self):
        return f"{str(8.9875517923e+9)} N*m^2/C^2"


class VirtualAssistant:
    _instance = None
    _dict = {Physics(): [G, Coulomb]}
    _THEMES = [Math(), Physics(), Geography(), Philology(), General(), Text(), Game()]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._dialogues = []

    def answer(self):
        print(
            f"Вітаю, мене звати {VirtualAssistant.__name__}. Ви можете задати мені питання з наступних тем: "
            f"{', '.join([theme.name for theme in self._THEMES[:-1]])}, {self._THEMES[-1].name}.")
