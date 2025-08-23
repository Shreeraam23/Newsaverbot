from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/rajputservermusic")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/Pre_contact_bot")],  # @username ko URL banaya
        [
            InlineKeyboardButton("📱 Open in App", url="tg://resolve?domain=rajputserver&post=19"),
            InlineKeyboardButton("💻 Open in Browser/PC", url="https://t.me/rajputserver/19")
        ]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return

    # ❌ "https://t.me/rajputserver/19" photo ke liye valid nahi hai
    # ✅ Ya to direct image link do (jpg/png), ya ek baar image bhejkar uska file_id use karo

    await message.reply_photo(
        photo="https://envs.sh/F6T.jpg",  # yahan apna direct image link ya file_id dalna
        caption=script.START_TXT.format(message.from_user.mention),
        reply_markup=buttons
    )
