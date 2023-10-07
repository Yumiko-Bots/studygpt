from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import openai
import asyncio

API = "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"
openai.api_key = API

API_ID=14688437
API_HASH="5310285db722d1dceb128b88772d53a6"
BOT_TOKEN="6652935072:AAEDRvQfbuQVdxpOpillomYwpYn6euetpdY"

studygpt = Client("studygpt", api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@studygpt.on_message(filters.command(["start"]))
async def start_command(_, message):
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
    msg = await message.reply_text(
        "Bot is starting...."
    )
    await asyncio.sleep(0.3)
    await msg.edit_text(
         text="""📚 Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴛᴜᴅʏ ɢᴘᴛ Bᴏᴛ! 🤖

I'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡɪᴛʜ ʏᴏᴜʀ sᴛᴜᴅɪᴇs. Jᴜsᴛ ᴛʏᴘᴇ ʏᴏᴜʀ ᴏ̨ᴜᴇsᴛɪᴏɴs ᴏʀ ᴛᴏᴘɪᴄs, ᴀɴᴅ I'ʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴇxᴘʟᴀɴᴀᴛɪᴏɴs, sᴜᴍᴍᴀʀɪᴇs, ᴀɴᴅ ᴀɴsᴡᴇʀs. Lᴇᴛ's ʟᴇᴀʀɴ ᴛᴏɢᴇᴛʜᴇʀ!

Tʏᴘᴇ '/help' ᴛᴏ sᴇᴇ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.

Hᴀᴘᴘʏ sᴛᴜᴅʏɪɴɢ! 📖✨
""",
         reply_markup=reply_markup,
    )

studygpt.run()
print("bot started!")

