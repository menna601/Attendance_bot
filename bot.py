from rivescript import RiveScript

bot = RiveScript(utf8=True)

bot.load_directory("brain")
bot.sort_replies()


def chat(message):
    if message == "":
        return "No message found "
    else:
        response = bot.reply("user", message)
    if response:
        return response
    else:
        return "No response found"



