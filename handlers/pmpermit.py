from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba Hoşgeldin. Otomatik karşıma mesajı hizmetidir.\n\n ❗️ kurallar:\n - Sohbete izin yok. Sürekli yazı yazmayı bırak, Komutlar için - Müzik botunun mesaj bölümüne bakınız.\n - İstenmeyen postaya izin verilmez\n\n🛑 **USERBOT GRUBUNUZA KATILAMAZ İSE GRUBUNUZUN DAVET BAĞLANTISINI VEYA GRUBUNUN LİNKİNİ GÖNDERİN.**\n\n ⚠️ DİKKAT: Burada bir mesaj Gönderiyorsanız. Yöneticinin iletinizi göreceği anlamına gelir. Sohbete katılın\n  - Bu kullanıcıyı gizli gruplara eklemeyin.\n - Özel bilgileri burada paylaşmayınız. 📚 Bilgi için geliştirici @Mahoaga\n\n")
  return                        

 
