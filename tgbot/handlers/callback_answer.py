from tgbot.utils.buttons import lang_keys, dashboard
from tgbot.utils.messages import messages
from tgbot.models import db
from decimal import Decimal
from datetime import datetime

def callback_answer(call, **kwargs):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    fcx_user = db.get_user(user_id)
    lang = fcx_user.language
    bot = kwargs.get('bot')

    # Update account balance in dashboard
    fcx_markup_balances = messages["fcx_markup_balances"][lang]
    dashboard[lang].keyboard[0][0] = fcx_markup_balances.format(account_balance=fcx_user.account_balance)

    if call.data == "confirm_address":
        wallet_address = call.message.text.split('\n')[1]
        fcx_user.wallet_address = wallet_address
        db.commit()
        wallet_address_confirmation = messages["wallet_address_confirmation"][lang]
        bot.send_message(chat_id, text=wallet_address_confirmation, parse_mode="html", reply_markup=dashboard[lang])

    elif call.data == "cancel_address":
        bot.send_message(chat_id, text="Cancelled", reply_markup=dashboard[lang])

    elif call.data == "confirm_order":
        bot.answer_callback_query(call.id)
        withdrawal_order = call.message.text
        amount_text, address_text = withdrawal_order.split('\n')
        amount = Decimal(amount_text.split(' ')[-1])
        wallet_address = address_text.split(' ')[-1]
        fcx_user.account_balance -= amount

        transaction = db.create_transaction(
            user_id=fcx_user.user_id,
            transaction_type="withdrawal",
            amount=amount,
            status="Pending",
            balance=fcx_user.account_balance,
            wallet_address=wallet_address
        )
        db.commit()

        payout_processing_text = messages['payout_processing_text'][lang]
        bot.send_message(
            ADMIN_ID,
            text=withdrawal_order,
            parse_mode="html"
        )
        bot.send_message(
            chat_id,
            text=payout_processing_text,
            parse_mode="html",
            reply_markup=dashboard[lang]
        )

    elif call.data == "confirm_reinvestment":
        amount = call.message.text.split(":")[-1]
        amount = Decimal(amount.split(" ")[0])
        if amount > fcx_user.account_balance:
            text_insufficient = messages["text_insufficient"][lang]
            bot.send_message(
                chat_id,
                text=text_insufficient,
                reply_markup=dashboard[lang]
            )
        else:
            fcx_user.account_balance -= amount
            fcx_user.active_investment += amount
            fcx_reinvest = db.create_transaction(
                user_id=user_id,
                transaction_type="reinvestment",
                amount=amount,
                balance=fcx_user.account_balance,
                status="completed"
            )
            db.commit()
            start_date = fcx_reinvest.get_start_date()
            close_date = fcx_reinvest.get_close_date()
            reinvest_confirmation_text = messages["reinvest_confirmation_text"][lang].format(
                start_date=start_date,
                close_date=close_date
            )
            bot.send_message(
                chat_id,
                text=reinvest_confirmation_text,
                reply_markup=dashboard[lang],
                parse_mode="html"
            )
