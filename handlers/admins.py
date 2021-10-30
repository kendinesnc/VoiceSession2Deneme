from asyncio.queues import QueueEmpty
 
from pyrogram import Client, filters 
from pyrogram.types import Message
from helpers.channelmusic import get_chat_id
from cache.admins import admins

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'ᴅᴜʀᴅᴜʀᴜʟᴅᴜ'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 ᴍᴜᴢɪᴋ ᴀᴄɪᴋ ᴅᴇɢɪʟ!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🤐 ᴅᴜʀᴅᴜʀᴜʟᴅᴜ!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 ʜɪᴄʙɪʀꜱᴇʏ ᴅᴜʀᴅᴜʀᴜʟᴍᴀᴅɪ!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🥳 ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ!")


@Client.on_message(command("son") & other_filters)
@errors
@authorized_users_only
async def bitir(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 🙄 ʜɪᴄʙɪʀꜱᴇʏ ᴏʏɴᴀᴛɪʟᴍɪʏᴏʀ!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ **ᴍᴜᴢɪᴋ ᴋᴀᴘᴀᴛɪʟᴅɪ!**\n\n• **ᴜꜱᴇʀʙᴏᴛ'ᴜɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ʙᴀɢʟᴀɴᴛɪꜱɪ ᴋᴇꜱɪʟᴅɪ**")



@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🙆‍♂️ ᴀᴛʟᴀᴛɪʟᴀᴄᴀᴋ ᴍᴜᴢɪᴋ ʏᴏᴋ!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("➡️ **ʙɪʀ ꜱᴏɴʀᴀᴋɪ ᴘᴀʀᴄᴀʏᴀ ɢᴇᴄɪʟᴅɪ!**\n• **ᴏʏɴᴀᴛɪʟɪʏᴏʀ.. 🥳**" )


# Yetki Vermek için (ver) Yetki almak için (al) komutlarını ekledim. Helpers dosyasının modüllerini kontrol ediniz.
# Gayet güzel çalışıyor. @Mahoaga Tarafından Eklenmiştir. 
@Client.on_message(filters.command("ver"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Kullanıcıya Yetki Vermek için yanıtlayınız!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkili.")
    else:
        await message.reply("✔ Kullanıcı Zaten Yetkili!")


@Client.on_message(filters.command("al"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✘ Kullanıcıyı yetkisizleştirmek için mesaj atınız!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkisiz")
    else:
        await message.reply("✔ Kullanıcının yetkisi alındı!")


@Client.on_message(command(["volume"]) & other_filters)
@authorized_users_only
async def change_volume(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **Birim olarak ayarlandı:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**hata:** {e}")


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def helper(client , message:Message):
     await message.reply_text("Komutlar ve kullanım burada açıklanmıştır.: \n 🎵 `/dinle` Youtube'da şarkıyı dinlemek için \n ▶️ `/oynat` Bir bağlantıya veya oynatılacak herhangi bir telgraf ses dosyasına yanıt olarak bunu yanıtlayın veya bul komutu ile kullanılabilir. \n ⏭️ `/atla` geçerli şarkıyı atlamak için \n ❌ `/son` şarkı akışını durdurmak için \n ⏸️ `/durdur` akışı duraklatmak için \n ⏩ `/devam` kayıttan yürütmeyi sürdürmek için. \n Satır içi arama da desteklenir.")
