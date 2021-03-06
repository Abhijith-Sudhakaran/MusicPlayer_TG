# A Module for Uploading Telegr.ph Images🌷.
# Don't remove these Copyright words when you Use these Code.
# line is Created by @Abhijith_Sudhakaran <https://github.com/Abhijith-Sudhakaran>
# ©-2022 All Right Reserved..!

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from config import OWNER_NAME, UPDATES_CHANNEL

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

@Client.on_message(filters.private & filters.media)
async def getmedia(bot, update):
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    try:
        message = await update.reply(
            text="`Processing Media you Send...`",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        print(error)
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('More Help', callback_data='help')
            ]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**© •** @{OWNER_NAME}"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
        InlineKeyboardButton(text="Share To", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
        ],[
        InlineKeyboardButton(text="Updates Channel", url="https://telegram.me/{UPDATES_CHANNEL}")
        ]]
    )
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
