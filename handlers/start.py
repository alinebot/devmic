# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello š there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nš“ Do you want me to play music in your Telegram groups'voice chats? Please click the \'š User Manual š\' button below to know how you can use me.\n\nš“ The [Assistant](https://t.me/Denvilmusic) must be in your group to play music in the voice chat of your group.\n\nš“ More info & commands mentioned in the [User Manual](https://telegra.ph/Denvil-04-22)\n\nA project by @Anie_news""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "š Add me to  your group š", url="https://t.me/Denvilmusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "šØāš» Updates šØāš»", url="https://t.me/Anie_news"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat šļø", url="https://t.me/MusicBotEnjoy_group"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**š“ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šļø Support Group šļø", url="https://t.me/MusicBotEnjoy_group")
                ]
            ]
        )
   )

