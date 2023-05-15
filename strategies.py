from abc import ABC, abstractmethod
import math
import datetime as dt
import random
import json


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
                   " заданих векторами (x1, y1) та (x2, y2)": MathStrategy4()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class MathStrategy1(MathStrategy):
    def handle_question(self, question):
        return "x = (-b ±√(b^2 - 4ac)) / 2a, де a, b та c - коефіцієнти квадратного рівняння ax^2 + bx + c = 0"


class MathStrategy2(MathStrategy):
    def handle_question(self, question):
        return "A x B = (AyBz - AzBy, AzBx - AxBz, AxBy - AyBx), де A та B - вектори."


class MathStrategy3(MathStrategy):
    def handle_question(self, question):
        return f"Pi is: {math.pi}"


class MathStrategy4(MathStrategy):
    @staticmethod
    def convert(num):
        try:
            f = float(num)
            return f
        except ValueError:
            return False

    def is_correct(self, question: str):
        tmp = question.split(",")
        if len(tmp) == 4 and all(map(self.convert, tmp)):
            return map(float, tmp)
        else:
            return False

    def handle_question(self, question):
        """f ChatBot.status[2] != 1:
            ChatBot.status = (handler.theme, question, 1)
        GG = "Введіть 4 числа у форматі: x1, y1, x2, y2\n"
        tmp1 = input("Введіть 4 числа у форматі: x1, y1, x2, y2")
        ChatBot().history.append(GG)
        ChatBot().history.append(tmp1)
        while not self.is_correct(tmp1):
            tmp1 = input("Введіть 4 числа у форматі: x1, y1, x2, y2")
            ChatBot().history.append(GG)
            ChatBot().history.append(tmp1+"\n")
        """
        return "ну дурні питання, я тобі як без точок це зроблю, як ти на 2 курс перейшла?"


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
        return "ε0 = 8,85⋅10−12 Ф/м\n"


class PhysicsStrategy2(PhysicsStrategy):

    def handle_question(self, question):
        return "G = 6.67384(80)10-11 м3 кг-1 с-2"


class PhilologyStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def handle_question(self, question) -> str | list:
        sub_str = {"які часи є в англійській мові?": PhilologyStrategy1(),
                   "як утворюються питальні речення в англійській мові?": PhilologyStrategy2(),
                   "Як утворити Passive Voice в Present Simple?".lower(): PhilologyStrategy3()}
        if question in sub_str:
            solver = sub_str[question]
            return solver.handle_question(question)
        else:
            return list(sub_str.keys())


class PhilologyStrategy1(PhilologyStrategy):
    def handle_question(self, question):
        return "Present Simple використовують для виразу звичайної, регулярно повторюваної дії." \
               "Past Simple використовують для виразу дії, яка відбулася у минулому.\n" \
               "Future Simple використовують для виразу дії, яка відбудеться у майбутньому." \
               "Present Continuous використовують для виразу дії, яка відбувається на даний момент.\n" \
               "Past Continuous використовують для виразу дії, яка вже відбулася в певний момент часу у минулому." \
               "Future Continuous використовують для виразу дії," \
               "яка буде відбуватися у певний момент часу в майбутньому.\n" \
               "Present Perfect використовують для виразу дії, яка відбулася (або яка відбувається)," \
               "результат якої зв’язаний з теперішнім.Past Perfect використовують для виразу дії,\n" \
               "яка закінчилася раніше другої дії або певного моменту у минулому.Future Perfect використовують" \
               "для виразу дії, яка завершиться до певного моменту часу в майбутньому."


class PhilologyStrategy2(PhilologyStrategy):
    def handle_question(self, question):
        return "Питальне слово + допоміжне (або модальне) дієслово + підмет + присудок + додаток + інші члени " \
               "речення.\n" \
               "Простіше — на прикладі: What (питальне слово) are" \
               " (допоміжне дієслово) you (підмет) cooking (присудок)?" \
               " – Що ти готуєш?"


class PhilologyStrategy3(PhilologyStrategy):
    def handle_question(self, question):
        return "Предмет / людина + am / are / is + 3-тя форма неправильного" \
               " дієслова або правильний дієслово з закінченням -ed."


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
        return "Озеро Каспій"


class GeographyStrategy2(GeographyStrategy):

    def handle_question(self, question):
        return "Тихий Океан"


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
        sub_str = {"скільки днів до Нового Року?".lower(): GeneralStrategy1(),
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
        now = dt.datetime.now().today()
        end = dt.datetime.today().replace(month=12, day=31)
        return f"{(end - now).days}"


class GeneralStrategy2(GeneralStrategy):
    def handle_question(self, question):
        now = dt.datetime.today().month
        return f"{now}"


class GeneralStrategy3(GeneralStrategy):
    def handle_question(self, question):
        num = round(random.random() * 10)
        predict = "Назви число\n"
        ChatBot._history.append(predict)

        guess = input(predict)
        ChatBot._history.append(guess)
        try:
            guess = int(guess)
            if guess == num:
                return "Вгадали"
            else:
                return "Не вгадали"
        except:
            return "число треба було вводити"


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
    status = ()
    _history = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        def rounder(args):
            n, string = args
            if n % 2 == 1:
                return "User:" + string.strip() + "\n"
            else:
                return "Bot:" + string.strip() + "\n"

        ChatBot._history = list(map(rounder, enumerate(ChatBot._history)))
        with open(self.file, "w") as dump:
            dump.writelines(self._history)
        return ChatBot._history

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        with open("config.json", "r") as json_file:
            tmp = json.load(json_file)['file'].split('.')
            self.file = tmp[0]+str(dt.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))+"."+tmp[1]



        self.strategies = {
            "математика": MathStrategy(),
            "фізика": PhysicsStrategy(),
            "географія": GeographyStrategy(),
            "робота з текстом": TextManipulationStrategy(),
            "загальні": GeneralStrategy(),
            "філологія": PhilologyStrategy()
        }

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
                    ChatBot.status = (strategy, question, ChatBot.i)
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
        if question != "назад":
            if self.theme == "":
                return self.obj.hello()
            else:
                return self.obj.handle_question(question, self.theme)
        else:
            if ChatBot.status == ():
                return self.obj.hello()
            elif ChatBot.status[2] == -1:
                ChatBot.status = ()
                return self.obj.hello()
            else:
                # todo
                return ChatBot.status


if __name__ == '__main__':
    with ChatBot() as chat_bot:
        handler = Handler(chat_bot)

        ans = input(handler.obj.hello())
        chat_bot.history.append(handler.obj.hello())
        chat_bot.history.append(ans + "\n")
        ans = ans.lower().strip()
        status = ("", "", "")
        while ans != "вихід":
            if ans in chat_bot.strategies or handler.theme in chat_bot.strategies:
                handler.theme = ans
                if ChatBot.i == 0:
                    response = handler.handle_question(ans)
                    chat_bot.history.append(response)
                else:
                    chat_bot.history.append(tmp)
                    response = handler.handle_question(tmp)
                    chat_bot.history.append(response + "\n")
                tmp = input(response).strip().lower()
                if tmp in chat_bot.strategies or tmp == "вихід":
                    ans = tmp
                    chat_bot.history.append(ans + "\n")
                    handler.theme = ans
                    ChatBot.i = 0
            else:
                ans = input(handler.obj.hello())
                chat_bot.history.append(handler.obj.hello())
                chat_bot.history.append(ans + '\n')
                ans = ans.lower().strip()
