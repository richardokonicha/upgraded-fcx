from telebot import TeleBot
from telebot.types import Message
from tgbot.utils.buttons import lang_keys
from tgbot.utils.messages import messages

from tgbot.models import db
from .start import start

def show_language(message: Message, bot: TeleBot):
    chat_id = message.chat.id
    select_preferred_lang = messages["select_preferred_lang"]
    bot.send_message(
            chat_id,
            text=select_preferred_lang,
            reply_markup=lang_keys,
            parse_mode="HTML"
            )

def set_language(message: Message, bot: TeleBot):
    """sets language and returns language value and send user confirmation message"""
    chat_id = message.chat.id
    user_id = message.from_user.id
    fcx_user = db.get_user(user_id)
    message_lang = message.text.split()[0].upper()
    if message_lang == "ENGLISH":
        fcx_user.language = 'en'
    if message_lang == "ITALIANO":
        fcx_user.language = "it"
    lang = fcx_user.language
    db.commit()
    db.session.refresh(fcx_user) 
    set_lang_text = {
        "en": """Language is set to: English 🇬🇧""",
        "it": """La lingua è impostata su: Italian 🇮🇹"""
    }
    start(message, bot)
