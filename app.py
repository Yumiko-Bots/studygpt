from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
import asyncio
import os

openai.api_key = os.environ.get("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")


API_ID = 14688437
API_HASH = "5310285db722d1dceb128b88772d53a6"
BOT_TOKEN = "6652935072:AAEDRvQfbuQVdxpOpillomYwpYn6euetpdY"

studygpt = Client("studygpt", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def generate_code(prompt):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    answer = chat_completion.choices[0].message["content"]
    return answer

@studygpt.on_message(filters.command(["start"]))
async def start(_, message):
    keyboard = [
        [
            InlineKeyboardButton("Help & Commands", callback_data="help"),
            InlineKeyboardButton("Support", url="https://t.me/yumiko_group"),
        ],
        [
            InlineKeyboardButton("Updates", url="https://t.me/yumikoupdates"),
            InlineKeyboardButton("About", callback_data="about"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = await message.reply_text("Bot is starting....")
    await asyncio.sleep(0.3)
    await msg.edit_text(
        text="""📚 Welcome to Study GPT Bot! 🤖

I'm here to help you with your studies. Just type your questions or topics, and I'll provide you with explanations, summaries, and answers. Let's learn together!

Type '/help' to see a list of available commands.

Happy studying! 📖✨
""",
        reply_markup=reply_markup,
    )

@studygpt.on_message(filters.command(["help"]))
async def help(_, message):
    keyboard = [
        [
            InlineKeyboardButton("Coding Assistant", callback_data="coding"),
        ],
        [
            InlineKeyboardButton("Image to Text", callback_data="image_to_text"),
        ],
        [
            InlineKeyboardButton("Chat GPT Assistant", callback_data="chat_gpt"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Here is the help section. Click the buttons below:", reply_markup=reply_markup)

@studygpt.on_callback_query(filters.regex("help"))
async def help_callback(_, query):
    keyboard = [
        [
            InlineKeyboardButton("Coding Assistant", callback_data="coding"),
        ],
        [
            InlineKeyboardButton("Image to Text", callback_data="image_to_text"),
        ],
        [
            InlineKeyboardButton("Chat GPT Assistant", callback_data="chat_gpt"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Here is the help section. Click the buttons below:", reply_markup=reply_markup)

@studygpt.on_callback_query()
async def callback_query_handler(_, query):
    if query.data == "coding":
        await query.message.reply_text("You selected Coding Assistant. How can I assist you with coding tasks?")
    elif query.data == "image_to_text":
        await query.message.reply_text("You selected Image to Text. Please provide an image, and I will convert it to text.")
    elif query.data == "chat_gpt":
        await query.message.reply_text("You selected Chat GPT Assistant. Feel free to ask me any questions!")

@studygpt.on_message(filters.command("code"))
async def code(_, message):
    if len(message.text.split()) > 1:
        prompt = message.text.split(None, 1)[1]
        answer = generate_code(prompt)
        await message.reply_text(answer)
    else:
        await message.reply_text("Please use /code (your code or ask a code)")

@studygpt.on_message(filters.text)
async def reply(_, message):
    if message.text.startswith("/"):
        return
    else:
        prompt = message.text
        answer = generate_code(prompt)
        await message.reply_text(answer)

studygpt.run()
print("Bot started!")
