from telebot import TeleBot
from telebot.types import Message
from tgbot.models import db
from tgbot.utils.buttons import force_r, dashboard, confirm_reinvestment
from tgbot import config
from tgbot.utils.messages import messages
from decimal import Decimal

# @bot.callback_query_handler(func=lambda call: True)
# def callback_answer(call):
#         user_id = call.from_user.id
#         fcx_user = db.User.get_user(user_id)
#         balance = fcx_user.account_balance
#         lang = fcx_user.language
#         if call.data == "confirm_reinvestment":
#                 pass


def process_reinvest(message):
    pass


def verify_reinvest(message, **kwargs):
    bot = kwargs.get("bot")
    markup = kwargs.get("markup")

    user_id = message.from_user.id
    fcx_user = db.get_user(user_id)
    chat_id = message.chat.id
    # fcx_user = db.User.get_user(user_id)
    reply_from = message.reply_to_message.text
    if reply_from in ["Please enter the amount to reinvest:", "Per favore inserire l'importo da reinvestire:"]:
        balance = fcx_user.account_balance
        lang = fcx_user.language
        try:
            reinvestment_amount = Decimal(message.text)
            if reinvestment_amount > balance:
                text_insufficient = messages["text_insufficient"][lang]

                bot.reply_to(
                    message,
                    text=text_insufficient,
                    reply_markup=markup
                )
            elif reinvestment_amount < 0:
                invalid_amount = messages["invalid_amount"][lang]
                bot.reply_to(
                    message,
                    text=invalid_amount,
                    reply_markup=markup
                )
            else:
                investment_confirmation = messages["investment_confirmation"][lang].format(
                    reinvestment_amount=reinvestment_amount)
                bot.send_message(
                    chat_id,
                    text=investment_confirmation,
                    reply_markup=confirm_reinvestment[lang]
                )
        except ValueError as err:
            invalid_amount = messages["invalid_amount"][lang]
            bot.reply_to(
                message,
                text=invalid_amount,
                reply_markup=dashboard[lang]
            )


def reinvest(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    chat_id = message.chat.id
    fcx_user = db.get_user(user_id)
    lang = fcx_user.language

    fcx_markup_balances = messages["fcx_markup_balances"]
    dashboard[lang].keyboard[0][0] = fcx_markup_balances[lang].format(
        account_balance=fcx_user.account_balance)

    reinvest_info = messages["reinvest_info"][lang]
    reinvest_insufficient = messages["reinvest_insufficient"][lang]
    reinvest_enter_amount = messages["reinvest_enter_amount"][lang]

    if fcx_user.account_balance < config.WITHDRAWAL_MINIMUM_AMOUNT:
        bot.send_message(
            chat_id, text=reinvest_info + reinvest_insufficient,
            reply_markup=dashboard[lang], parse_mode="html"
        )
    else:
        bot.send_message(
            chat_id,
            text=reinvest_info
        )
        bot.send_message(
            chat_id,
            text=reinvest_enter_amount,
            # reply_markup=dashboard.get(lang),
            parse_mode="html",
            reply_markup=force_r
        )
        bot.register_next_step_handler(
            message, verify_reinvest, bot=bot, markup=dashboard[lang])
