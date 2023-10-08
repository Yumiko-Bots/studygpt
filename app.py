from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
import asyncio
from pyrogram.enums import ChatAction

openai.api_key = "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"

API_ID = 14688437
API_HASH = "5310285db722d1dceb128b88772d53a6"
BOT_TOKEN = "6652935072:AAEDRvQfbuQVdxpOpillomYwpYn6euetpdY"

studygpt = Client("studygpt", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def generate_code(code_input):
    response = openai.ChatCompletion.create(
        engine="davinci",
        prompt=code_input,
        max_tokens=50,
    )
    code_output = response.choices[0].text.strip()
    return code_output

@studygpt.on_message(filters.command(["start"]))
async def start(_, message):
    keyboard = [
        [
            InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/yumiko_group"),
        ],
        [
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/yumikoupdates"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = await message.reply_text("Bot is starting....")
    await asyncio.sleep(0.3)
    await msg.edit_text(
        text="""📚 Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴛᴜᴅʏ ɢᴘᴛ Bᴏᴛ! 🤖

I'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡɪᴛʜ ʏᴏᴜʀ sᴛᴜᴅɪᴇs. Jᴜsᴛ ᴛʏᴘᴇ ʏᴏᴜʀ ᴏ̨ᴜᴇsᴛɪᴏɴs ᴏʀ ᴛᴏᴘɪᴄs, ᴀɴᴅ I'ʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴇxᴘʟᴀɴᴀᴛɪᴏɴs, sᴜᴍᴍᴀʀɪᴇs, ᴀɴᴅ ᴀɴsᴡᴇʀs. Lᴇᴛ's ʟᴇᴀʀɴ ᴛᴏɢᴇᴛʜᴇʀ!

Tʏᴘᴇ '/help' ᴛᴏ sᴇᴇ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.

Hᴀᴘᴘʏ sᴛᴜᴅʏɪɴɢ! 📖✨
""",
        reply_markup=reply_markup,
    )

@studygpt.on_message(filters.command(["help"]))
async def help(_, message):
    keyboard = [
        [
            InlineKeyboardButton("Cᴏᴅɪɴɢ Assɪsᴛᴀɴᴛ", callback_data="coding"),
        ],
        [
            InlineKeyboardButton("Iᴍᴀɢᴇ ᴛᴏ Tᴇxᴛ", callback_data="image_to_text"),
        ],
        [
            InlineKeyboardButton("Cʜᴀᴛ GPT Assɪsᴛᴀɴᴛ", callback_data="chat_gpt"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ᴛᴏ sᴇᴇ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs:", reply_markup=reply_markup)

@studygpt.on_callback_query(filters.regex("help"))
async def help_callback(_, query):
    keyboard = [
        [
            InlineKeyboardButton("Cᴏᴅɪɴɢ Assɪsᴛᴀɴᴛ", callback_data="coding"),
        ],
        [
            InlineKeyboardButton("Iᴍᴀɢᴇ ᴛᴏ Tᴇxᴛ", callback_data="image_to_text"),
        ],
        [
            InlineKeyboardButton("Cʜᴀᴛ GPT Assɪsᴛᴀɴᴛ", callback_data="chat_gpt"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ᴛᴏ sᴇᴇ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs:", reply_markup=reply_markup)

@studygpt.on_callback_query()
async def callback_query_handler(_, query):
    if query.data == "coding":
        await query.message.reply_text("You selected Coding Assistant. How can I assist you with coding tasks?")
    elif query.data == "image_to_text":
        await query.message.reply_text("You selected Image to Text. Please provide an image, and I will convert it to text.")
    elif query.data == "chat_gpt":
        await query.message.reply_text("You selected Chat GPT Assistant. Feel free to ask me any questions!")

@studygpt.on_message(filters.text)
async def code(_, message):
    if message.text.startswith("/code "):
        code_input = message.text[len("/code "):]
        await message.reply_chat_action(action=ChatAction.TYPING)
        code_output = generate_code(code_input)
        await message.reply_text(f"**Input:**\n```\n{code_input}\n```\n**Output:**\n```\n{code_output}\n```")

studygpt.run()
print("Bot started!")
