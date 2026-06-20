# -----------------------------------------------
# 🔸 ShashankMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VaishuMusic import app

start_txt = """
<b>❖ ʜᴇʏ ᴛʜᴇʀᴇ, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴠᴀɪsʜᴜ ᴍᴜsɪᴄ ✨</b>

<b>● ɪ ᴀᴍ ➥ ᴠᴀɪsʜᴜ ᴍᴜsɪᴄ ʙᴏᴛ 🎶</b>

<b>❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.</b>

<b>✦ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴠᴀɪsʜᴜ ᴍᴜsɪᴄ 💜</b>
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton(
                "✦ ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                url="https://t.me/sigma_thakur"
            ),
            InlineKeyboardButton(
                "✦ ʀᴇᴘᴏ",
                url="https://github.com/sigmathakur/Vaishu-Music"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_video(
        video="https://graph.org/file/7c1aa59649fbf3ab422da.mp4",
        caption=start_txt,
        reply_markup=reply_markup,
        has_spoiler=True,
        supports_streaming=True
    )
