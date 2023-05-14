from telebot import TeleBot
from telebot.types import Message
from tgbot.models import db, User
from tgbot.utils.messages import messages
from tgbot.utils.buttons import lang_keys, dashboard


def start(message: Message, bot: TeleBot):
    """this is the starting point, it checks if user is not registered 
    and renders lang settings if user is registered uses pervious lang """
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
    fcx_user = db.get_user(user_id)
    select_preferred_lang = messages["select_preferred_lang"]
    welcome_text = messages["welcome_text"]
    
    if fcx_user is not None:
        lang = fcx_user.language
        if lang == None or lang not in ['en', 'it']:
            bot.send_message(
                chat_id,
                text=select_preferred_lang,
                reply_markup=lang_keys,
                parse_mode="HTML"
            )
        else:
            fcx_markup_balances = {
                "en": f"Balance  {fcx_user.account_balance} BTC",
                "it": f"Bilance  {fcx_user.account_balance} BTC"
            }
            dashboard[lang].keyboard[0][0] = fcx_markup_balances[lang]
            bot.send_message(
                chat_id,
                text=welcome_text[lang],
                reply_markup=dashboard[lang],
                parse_mode="HTML"
            )
            if fcx_user.referral:
                referral_id = fcx_user.referral
                fcx_referral = db.get_user(referral_id)
                referral_name = fcx_referral.name
                referred = {
                    "en": f"You were referred by {referral_name}",
                    "it": f"You were referred by {referral_name}"
                }
                bot.send_message(
                    chat_id,
                    text=referred[lang],
                    reply_markup=dashboard[lang],
                    parse_mode="HTML"
                )
            else:
                pass
    else:
        try:
            referral = message.text.split(' ')[1]
            if not db.user_exists(int(referral)):
                referral = "Invalid referral"
        except (IndexError, ValueError) as error:
            referral = None
            print(error)

        fcx_user = db.create_user(
            name=name,
            user_id=user_id,
            referral=referral,
            is_new_user=True,
            is_admin=False
        )

        bot.send_message(
            chat_id,
            text=select_preferred_lang,
            reply_markup=lang_keys,
            parse_mode="HTML"
        )
