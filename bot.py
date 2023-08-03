-import pyrogram

bot = pyrogram.Client("my_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH")

@bot.on_message()
def handle_message(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Welcome to my bot! I can create tokens and collect members for you.")
        bot.send_message(message.chat.id, "To create a token, type /create_token.")
        bot.send_message(message.chat.id, "To collect members, type /collect_members.")

@bot.on_command("create_token")
def create_token(message):
    token = pyrogram.utils.get_random_token()
    bot.send_message(message.chat.id, "Your token is: " + token)

@bot.on_command("collect_members")
def collect_members(message):
    members = []
    for user in message.chat.members:
        members.append(user.id)
    bot.send_message(message.chat.id, "The members of this chat are: " + ",".join(members))

bot.run()
