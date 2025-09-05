# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import traceback
from asyncio import get_running_loop
from io import BytesIO
from deep_translator import GoogleTranslator
from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import Message


def convert(text):
    audio = BytesIO()
    try:
        # Detect language using deep_translator
        detected = GoogleTranslator(source='auto', target='en').translate(text)
        # For language detection, we'll assume the original language is the most common one
        # or default to 'en' if detection fails
        lang = 'en'  # Default to English for now
    except:
        lang = 'en'  # Fallback to English
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".mp3"
    tts.write_to_fp(audio)
    return audio


@Client.on_message(filters.command("tts"))
async def text_to_speech(bot, message: Message):
    vj = await bot.ask(chat_id = message.from_user.id, text = "Now send me your text.")
    if vj.text:
        m = await vj.reply_text("Processing")
        text = vj.text
        try:
            loop = get_running_loop()
            audio = await loop.run_in_executor(None, convert, text)
            await vj.reply_audio(audio)
            await m.delete()
            audio.close()
        except Exception as e:
            await m.edit(e)
            e = traceback.format_exc()
            print(e)
    else:
        await vj.reply_text("Send me only text Buddy.")



