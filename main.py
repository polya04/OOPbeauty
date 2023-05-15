from strategies import ChatBot
from strategies import Handler

if __name__ == '__main__':
    with ChatBot() as chat_bot:
        handler = Handler(chat_bot)

        ans = input(handler.obj.hello())
        chat_bot.history.append("BOT: " + handler.obj.hello())
        chat_bot.history.append("USER: " + ans + "\n")
        ans = ans.lower().strip()
        status = ("", "", "")

        while ans != "вихід":
            if ans in chat_bot.strategies or handler.theme in chat_bot.strategies:
                handler.theme = ans
                if ChatBot.i == 0:
                    response = handler.handle_question(ans)

                    chat_bot.history.append("BOT: " + response)
                else:
                    chat_bot.history.append("USER: " + tmp)
                    response = handler.handle_question(tmp)
                    if ChatBot.i == 1:
                        print(response)
                    chat_bot.history.append("BOT: " + response + "\n")
                if ChatBot.i == 1:
                    ChatBot.i = 0
                else:
                    tmp = input(response).strip().lower()
                if tmp in chat_bot.strategies or tmp == "вихід":
                    ans = tmp
                    chat_bot.history.append("USER: " + ans + "\n")
                    handler.theme = ans
                    ChatBot.i = 0
            else:
                ans = input(handler.obj.hello())
                chat_bot.history.append("BOT: " + handler.obj.hello())
                chat_bot.history.append("USER :" + ans + '\n')
                ans = ans.lower().strip()