#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href='tg://user?id={1942517921}'>𝙳𝚁𝙾𝙽𝙾</a>\n★ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : <code>𝙿𝚈𝚃𝙷𝙾𝙽 3</code>\n★ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : <a href='https://docs.pyrogram.org/'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙰𝚂𝚈𝙽𝙲𝙸𝙾 {__version__}</a>\n★ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 : <a href='https://github.com/skdrono05/FileSharingBot'>Click here</a>\n★ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : <a href='https://t.me/+QoCiOv4LptpkYzM1'>𝙹𝙾𝙸𝙽 𝙻𝙸𝙽𝙺</a>\n★ 𝙶𝚁𝙾𝚄𝙿 : <a href='https://t.me/MovieShowGroup'>𝙹𝙾𝙸𝙽 𝙻𝙸𝙽𝙺</a>\n",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝙲𝙾𝙻𝚂𝙴", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
