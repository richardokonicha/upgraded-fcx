
from config import *

@bot.message_handler(
    func=lambda message: message.content_type == 'text'
    and (
        bool(re.search(r'Transactions', message.text, re.IGNORECASE))
         or  bool(re.search(r'Transazioni$', message.text, re.IGNORECASE))
        )
)
def transaction(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    fcx_user = db.User.get_user(user_id)
    balance = fcx_user.account_balance
    lang = fcx_user.language
    transactions = db.Transactions.get_transactions(user_id)
    deposits = []
    payouts = []
    reinvestments = []
    commissions = []
    try:
        for value in transactions:
            if value.transaction_type=="deposit" and value.status=="Completed":
                deposits.append(value.date.split("T")[0]+"   "+str(value.amount)+" BTC")
            if value.transaction_type=="withdrawal":
                payouts.append(value.date.split("T")[0]+"   "+str(value.amount)+" BTC")
            if value.transaction_type=="reinvestment":
                reinvestments.append(value.date.split("T")[0]+"   "+str(value.amount)+" BTC")
            if value.transaction_type=="commissions":
                commissions.append(value.date.split("T")[0]+"   "+str(value.amount)+" BTC")

        def listToString(s):
            str1 = """"""
            for ele in s:
                str1 += (ele+"""
    """)
            return str1  
        text_deposit = listToString(deposits)
        text_reinvestments = listToString(reinvestments)
        text_payout = listToString(payouts)
        text_commissions = listToString(commissions)
                
        text_info = {
            "en": f"""

    <b>Deposits:</b>
    .....  
    {text_deposit}
    <b>Payouts:</b>
    .....
    {text_payout}
    <b>Reinvestments:</b>
    ......
    {text_reinvestments}
    <b>Commissions:</b>
    .....
    {text_commissions}

            """,
            "it": f"""
    <b>Depositi:</b>
    .....
    {text_deposit}
    <b>Pagamenti:</b>
    .....
    {text_payout}
    <b>Reinvestimenti:</b>
    ......
    {text_reinvestments}
    <b>Commissioni:</b>
    .....
    {text_commissions}

            """
            }

        fcx_markup_balances = {
                    "en": f"Balances  {fcx_user.account_balance} BTC",
                    "it": f"Bilance  {fcx_user.account_balance} BTC"
                    }
        dashboard[lang].keyboard[0][0] = fcx_markup_balances[lang]
        bot.send_message(
            chat_id, text=text_info[lang],
            reply_markup=dashboard.get(lang), parse_mode="html"
            )

    except TypeError:
        bot.send_message(
            chat_id,
            text="No Transactions yet",
            reply_markup=dashboard.get(lang), parse_mode="html"


        )

