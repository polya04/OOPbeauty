from abc import ABC, abstractmethod
import math


class Theme(ABC):

    def __init__(self, parent=None):
        self.parent = parent
        self._themes = ["математика", "фізика", "географія", "загальні", "робота з текстом"]

    @abstractmethod
    def name(self):
        pass

    def action(self):
        themes = ', '.join(self._themes[:-1]) + self._themes[-1] if self._themes else ''
        return f"Ви обрали тему {self.name}. Ви можете задати мені питання з наступних тем: {themes}. "

    @property
    def themes(self):
        return self._themes


class Math(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()

    @property
    def name(self):
        return "математика"


class Physics(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()
        self._themes.extend(["вивести гравітаційну сталу", "вивести кулонівську сталу"])

    @property
    def name(self):
        return "фізика"


class Geography(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()

    @property
    def name(self):
        return "географія"


class Philology(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()

    @property
    def name(self):
        return "філологія"


class General(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()

    @property
    def name(self):
        return "загальні"


class Text(Theme):
    def __init__(self):
        super().__init__()
        self.parent = super()

    @property
    def name(self):
        return "робота з текстом"


class G(Physics):
    def action(self):
        return "G is approximately 6.67430 × 10-11 N(m/kg)^2"


class Coulomb(Physics):
    def action(self):
        return f"{str(8.9875517923e+9)} N*m^2/C^2"


class Handler:
    def handle(self):
        pass


class VirtualAssistant:
    _instance = None
    _DICT = {Physics: [G, Coulomb], Math: [], Geography: [],
             Philology: [], General: [], Text: []}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._dialogues = []
