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
                   "формула векторного добутку векторів": MathStrategy2()}
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


class GeographyStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        # execute geography logic here and return response
        pass


class TextManipulationStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        # execute text manipulation logic here and return response
        pass


class GeneralStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question):
        # execute general logic here and return response
        pass


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
