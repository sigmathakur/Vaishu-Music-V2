import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from VaishuMusic import app
from VaishuMusic.utils.database import add_served_chat, get_assistant

# 👉 Apna owner ID daal (int me)
OWNERS = [8519634448]


@app.on_message(filters.command("gadd") & filters.user(OWNERS))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    
    if len(command_parts) != 2:
        await message.reply(
            "**❍ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ.\nᴜsᴇ » `/gadd @Bot_username`**"
        )
        return

    bot_username = command_parts[1]

    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id

        done = 0
        failed = 0

        lol = await message.reply("❍ **ᴀᴅᴅɪɴɢ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs...**")

        await userbot.send_message(bot_username, "/start")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002100130095:
                continue

            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
            except Exception:
                failed += 1

            await lol.edit(
                f"**❍ ᴀᴅᴅɪɴɢ {bot_username}**\n\n"
                f"**➥ ᴀᴅᴅᴇᴅ: {done} ✔**\n"
                f"**➥ ғᴀɪʟᴇᴅ: {failed} ✘**\n\n"
                f"**➲ ʙʏ » @{userbot.username}**"
            )

            await asyncio.sleep(3)

        await lol.edit(
            f"**❍ {bot_username} ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🎉**\n\n"
            f"**➥ ᴀᴅᴅᴇᴅ: {done} ✅**\n"
            f"**➥ ғᴀɪʟᴇᴅ: {failed} ✘**\n\n"
            f"**➲ ʙʏ » @{userbot.username}**"
        )

    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")
