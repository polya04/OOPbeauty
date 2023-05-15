from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def __init__(self):
        self.sub_str = {
        }

    @abstractmethod
    def handle_question(self, question):
        sub_str = {}


class MathStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question) -> str | list:
        sub_str = {"формула розв'язання квадратного рівняння": MathStrategy1(),
                   "формула векторного добутку векторів": MathStrategy2(),
                   "вивести число π": MathStrategy3(),
                   "знайти координати точки перетину двох прямих,"
                   " заданих векторами (x1, y1) та (x2, y2).": MathStrategy4()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class MathStrategy1(MathStrategy):
    def handle_question(self, question):
        return "Math FIRST"


class MathStrategy2(MathStrategy):
    def handle_question(self, question):
        return "Math Second"


class MathStrategy3(MathStrategy):
    def handle_question(self, question):
        return "Math Third"


class MathStrategy4(MathStrategy):
    def handle_question(self, question):
        return "Math Third"


class PhysicsStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question) -> str | list:
        sub_str = {"вивести кулонівську сталу": PhysicsStrategy1(),
                   "вивести гравітаційну сталу": PhysicsStrategy2()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class PhysicsStrategy1(PhysicsStrategy):
    def handle_question(self, question):
        return "FIRST"


class PhysicsStrategy2(PhysicsStrategy):

    def handle_question(self, question):
        return "SECOND"


class PhilologyStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question) -> str | list:
        sub_str = {"які часи є в англійській мові?": PhilologyStrategy1(),
                   "як утворюються питальні речення в англійській мові?": PhilologyStrategy2(),
                   "Як утворити Passive Voice в Present Simple??".lower(): PhilologyStrategy3()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class PhilologyStrategy1(PhilologyStrategy):
    def handle_question(self, question):
        return "Philo FIRST"


class PhilologyStrategy2(PhilologyStrategy):
    def handle_question(self, question):
        return "Philo 2"


class PhilologyStrategy3(PhilologyStrategy):
    def handle_question(self, question):
        return "Philo 3"


class GeographyStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        sub_str = {"яке найбільше озеро в світі за площею?": GeographyStrategy1(),
                   "який океан найбільший за площею?": GeographyStrategy2()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class GeographyStrategy1(GeographyStrategy):
    def handle_question(self, question):
        return "Geo FIRST"


class GeographyStrategy2(GeographyStrategy):

    def handle_question(self, question):
        return "Geo SECOND"


class TextManipulationStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        sub_str = {"вивести вміст файлу в зворотному порядку.": TextManipulationStrategy1(),
                   "вивести всі слова довші за 10 символів.": TextManipulationStrategy2(),
                   "перевести текст в нижній регістр.": TextManipulationStrategy3()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class TextManipulationStrategy1(TextManipulationStrategy):
    def handle_question(self, question):
        return "text FIRST"


class TextManipulationStrategy3(TextManipulationStrategy):
    def handle_question(self, question):
        return "text 3"


class TextManipulationStrategy2(TextManipulationStrategy):
    def handle_question(self, question):
        return "text 2"


class GeneralStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        sub_str = {"скільки днів до Нового Року?": GeneralStrategy1(),
                   "який зараз місяць?": GeneralStrategy2(),
                   "пограти у вгадай число між 1 та 10": GeneralStrategy3(),
                   "заспівати колядку": GeneralStrategy4(),
                   "варіант від студента 6?": GeneralStrategy5(),
                   "варіант від студента 8": GeneralStrategy6(),
                   "варіант від студента 10": GeneralStrategy7(),
                   "варіант від студента 12": GeneralStrategy8(),
                   "варіант від студента 23": GeneralStrategy9(),
                   "варіант від студента 25": GeneralStrategy10(),
                   "варіант від студента 27": GeneralStrategy11()
                   }
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class GeneralStrategy1(GeneralStrategy):
    def handle_question(self, question):
        return "general FIRST"


class GeneralStrategy2(GeneralStrategy):
    def handle_question(self, question):
        return "general 2"


class GeneralStrategy3(GeneralStrategy):
    def handle_question(self, question):
        return "general 3"


class GeneralStrategy4(GeneralStrategy):
    def handle_question(self, question):
        return "general 4"


class GeneralStrategy5(GeneralStrategy):
    def handle_question(self, question):
        return "general 5"


class GeneralStrategy6(GeneralStrategy):
    def handle_question(self, question):
        return "general 6"


class GeneralStrategy7(GeneralStrategy):
    def handle_question(self, question):
        return "general 7"


class GeneralStrategy8(GeneralStrategy):
    def handle_question(self, question):
        return "general 8"


class GeneralStrategy9(GeneralStrategy):
    def handle_question(self, question):
        return "general 9"


class GeneralStrategy10(GeneralStrategy):
    def handle_question(self, question):
        return "general 10"


class GeneralStrategy11(GeneralStrategy):
    def handle_question(self, question):
        return "general 11"


class ChatBot:
    _instance = None
    i = 0

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print(self._history)
        return self._history

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.strategies = {
            "математика": MathStrategy(),
            "фізика": PhysicsStrategy(),
            "географія": GeographyStrategy(),
            "робота з текстом": TextManipulationStrategy(),
            "загальні": GeneralStrategy()
        }
        self._history = []

    def hello(self):
        return f"Вітаю, мене звати {ChatBot.__name__}. Ви можете задати мені питання з наступних" \
               f" тем: {', '.join(list(self.strategies.keys()))[:]}.\n"

    def handle_question(self, question, theme):
        if theme in self.strategies:
            strategy = self.strategies[theme]
            response = strategy.handle_question(question)
            tmp = list(self.strategies.keys())
            tmp.extend(response)
            if isinstance(response, list):
                if ChatBot.i == -1:
                    return f"Я не знаю таку тему. Ви обрали тему {theme}, доступні дані питання: " + ", ".join(
                        tmp) + "\n"
                else:
                    ChatBot.i = -1
                    return f"Ви обрали тему {theme}, доступні дані питання: " + ", ".join(response) + "\n"

            else:
                ChatBot.i = 0
                return response

        else:
            return "Sorry, I don't know how to answer that question."

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, item):
        self._history.extend(item)


class Handler:
    def __init__(self, obj):
        self._theme = ""
        self.obj: ChatBot = obj

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, theme):
        self._theme = theme

    def handle_question(self, question):
        if self.theme == "":
            return self.obj.hello()
        else:
            return self.obj.handle_question(question, self.theme)


if __name__ == '__main__':
    with ChatBot() as chat_bot:
        handler = Handler(chat_bot)

        ans = input(handler.obj.hello())
        chat_bot.history.append(handler.obj.hello())
        chat_bot.history.append(ans)
        ans = ans.lower().strip()
        while ans != "вихід":
            if ans in chat_bot.strategies or handler.theme in chat_bot.strategies:
                handler.theme = ans
                if ChatBot.i == 0:
                    response = handler.handle_question(ans)
                    chat_bot.history.append(response)
                else:
                    chat_bot.history.append(tmp)
                    response = handler.handle_question(tmp)
                    chat_bot.history.append(response)
                tmp = input(response).strip().lower()
                if tmp in chat_bot.strategies or tmp == "вихід":
                    ans = tmp
                    chat_bot.history.append(ans)
                    handler.theme = ans
                    ChatBot.i = 0
            else:
                ans = input(handler.obj.hello())
                chat_bot.history.append(handler.obj.hello())
                chat_bot.history.append(ans)
                ans = ans.lower().strip()
