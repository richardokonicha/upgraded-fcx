from telebot import TeleBot
from telebot.types import Message
from tgbot.utils.messages import messages
from tgbot import config
from tgbot.utils.buttons import dashboard
from tgbot.models import db

def team(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    fcx_user = db.get_user(user_id)
    lang = fcx_user.language
    bot_info = bot.get_me()
    bot_name = bot_info.username
    withdrawal_minimum_amount = config.WITHDRAWAL_MINIMUM_AMOUNT
    invitation_link = messages["invitation_link"][lang].format(
        bot_name=bot_name,
        user_id=user_id
    )
    referral_system_info = messages["referral_system_info"][lang]
    commission_info = messages["commission_info"][lang]

    text_info = invitation_link + referral_system_info + commission_info

    fcx_markup_balances = messages["fcx_markup_balances"][lang]
    fcx_markup_balances_lang = fcx_markup_balances.format(account_balance=fcx_user.account_balance)
    dashboard[lang].keyboard[0][0] = fcx_markup_balances_lang

    bot.send_message(
        user_id,
        text=text_info,
        reply_markup=dashboard.get(lang),
        parse_mode="html"
    )
