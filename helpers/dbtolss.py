import os
import time
import string
import random
import datetime
import aiofiles
import asyncio
import traceback
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

from helpers.database import db, Database, dcmdb

# Komut Önleme Özelliği

delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool:
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


async def delcmd_on(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id}) 
