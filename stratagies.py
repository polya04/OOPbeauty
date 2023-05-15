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

    def handle_question(self, question):
        # execute math logic here and return response
        pass


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
        self.tmp = 0

    def hello(self):
        return f"Вітаю, мене звати {ChatBot.__name__}. Ви можете задати мені питання з наступних" \
               f" тем: {', '.join(list(self.strategies.keys()))[:-1]}, {list(self.strategies.keys())[-1]}.\n"

    def handle_question(self, question, theme):
        if theme in self.strategies:
            strategy = self.strategies[theme]
            response = strategy.handle_question(question)
            tmp = list(self.strategies.keys())
            tmp.extend(response)
            if isinstance(response, list):
                if ChatBot.i == -1:
                    return f"Ви обрали тему {theme}, доступні дані питання: " + ", ".join(tmp) + "\n"
                else:
                    ChatBot.i = -1
                    return "Доступні дані теми: " + ", ".join(response) + "\n"

            else:
                ChatBot.i = 0
                return response

        else:
            return "Sorry, I don't know how to answer that question."


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
    chat_bot = ChatBot()
    handler = Handler(chat_bot)

    ans = input(handler.obj.hello()).lower().strip()
    while ans != "вихід":
        if ans in chat_bot.strategies or handler.theme in chat_bot.strategies:
            handler.theme = ans
            if ChatBot.i == 0:
                response = handler.handle_question(ans)
            else:
                response = handler.handle_question(tmp)
            tmp = input(response).strip().lower()
            if tmp in chat_bot.strategies:
                ans = tmp
                handler.theme = ans
                ChatBot.i = 0
        else:
            ans = input("Choose correct variant\n")
