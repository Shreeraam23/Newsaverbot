from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/myserver23")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/Pre_contact_bot")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://vault.pictures/p/5a0b682e8cb9420092b0cc8a853ce457",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
