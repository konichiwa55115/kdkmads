from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import enums

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action(enums.ChatAction.TYPING)

    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join Project Channel!", url="https://t.me/odbots")]]
        ),
    )
