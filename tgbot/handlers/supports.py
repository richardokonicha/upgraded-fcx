from telebot import TeleBot
from telebot.types import Message
from tgbot.models import db
from tgbot.utils.buttons import dashboard
from tgbot.utils.messages import messages


def support(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    fcx_user = db.get_user(user_id)
    lang = fcx_user.language
    support_info = messages["support_info"]
    bot.send_message(
        user_id, text=support_info[lang],
        reply_markup=dashboard.get(lang), parse_mode="html"
        )

