messages = {
    "select_preferred_lang": """
Please select your language
Per favore scelga la sua lingua
    """,


    "welcome_text": {

        "en": """
<b>Welcome to FCX Trading Bot</b>

FCX Trading Bot is one of the most innovative Crypto and Forex trading providers. Successful traders, now allow access to the financial world not only for big investors but also for the average person. With the simplified interface of the FCX Trading Bot, investing has never been this easy to handle.

FCX Trading Bot profits depends on the global market situation and there is no guarantee of a fixed percentage of interest. Our strategy is to generate profits at the lowest possible risk.

Deposits are being handled at the highest security level according to a modern portfolio management serving the FCX Trading Bot.

        """,


        "it": """
<b>Benvenuti a FCX Trading Bot </b>

FCX Trading Bot è uno dei più innovativi fornitori di Crypto e Forex trading. I trader di successo ora permettono l'accesso al mondo finanziario non solo ai grandi investitori ma anche alla persona media. Con l'interfaccia semplificata del FCX Trading Bot l'investimento non è mai stato così facile da gestire.

I profitti del FCX Trading Bot dipendono dalla situazione del mercato globale e non c'è garanzia di una percentuale fissa di interessi. La nostra strategia è quella di generare profitti al minor rischio possibile.

I depositi sono gestiti al più alto livello di sicurezza secondo una moderna gestione di portafoglio al servizio del Trading Bot FCM.
        """
    },

    "balance_msg": {

        "en": """
Your Account Balance:
<strong>{balance} BTC</strong>
Total Active Investments:
<strong>{active_investment} BTC</strong>
Total Active Reinvestments:
<strong>{active_reinvestment} BTC</strong>
Total Pending Investments:
<strong>{pending_investment} BTC</strong>
                """,

        "it": """

Saldo del conto:
<strong>{balance} BTC</strong>
Investimenti attivi:
<strong>{active_investment} BTC</strong>
Reinvestimenti attivi:
<strong>{active_reinvestment} BTC</strong>
Investimenti in sospeso:
<strong>{pending_investment} BTC</strong>

    """,
    },

    "no_balance_text": {
        "en": f"""
            No investment yet. Go to <b>Deposit</b> to add funds.
        """,
        "it": f"""
            Ancora nessun investimento
Andate a <b>Deposito</b> per aggiungere fondi.
        """
    },

    "fcx_markup_balances": {
        "en": "Balance  {account_balance} BTC",
        "it": "Bilance  {account_balance} BTC"
    },

    "support_info": {
        "en": f"""
Contact:
@fcx_bot
        """,
        "it": f"""
Contatto:
@fcx_bot

        """
    },

    # deposits
    "deposit_amount_text": {
        "en": """<b>Enter the amount you wish to deposit 
(min: 0.025 BTC max: 5 BTC)</b>""",
        "it": """Enter the amount you wish to deposit(italian
(min: 0.025 BTC max: 5 BTC)"""
    },

    "duration_text": {
        "en": """
Bitcoin Amount:
Min: 0.025 BTC
Max: 5 BTC

This address will be active for 4 hours.
Funds will show up after first blockchain confirmation.
""",
        "it": """
Importo Bitcoin: 
Min. 0,025 BTC 
Max. 5 BTC

Questo indirizzo sarà attivo per 4 ore.
I fondi appariranno dopo la prima conferma della Blockchain.
        
            """
    },

    "arrival_text": {
        "en": """Here is your personal BTC address for your Investments ⬇️⬇️⬇️""",
        "it": """Qui il Vostro indirizzo personale Bitcoin per i Vostri investimenti:"""
    },

    # Reinvest
    "reinvest_info": {
        "en": f"""
You can make a reinvest any time, depending on your account balance . 
Minimum amount to reinvest is 0.002 BTC. Once credited, each reinvestment counts for itself and runs for 180 days.
        """,
        "it": f"""
Potete effettuare un reinvestimento in qualsiasi momento, a seconda del saldo del Vostro conto. L'importo minimo da reinvestire è di 0,002 BTC. Una volta accreditato, ogni reinvestimento vale per se stesso e dura 180 giorni.
        """
    },
    "reinvest_insufficient": {
        "en": """
You don't have enough funds to create a reinvest
        """,
        "it": """
Non avete abbastanza fondi per creare un reinvestimento. 
        """
    },

    "reinvest_enter_amount": {
        "en": """
<b>Please enter the amount to reinvest:</b>
        """,
        "it": """
<b>Per favore inserire l'importo da reinvestire:</b>
        """
    },

    "text_insufficient": {
        "en": "You have insufficient account balance",
        "it": "Hai un saldo del conto insufficiente"
    },

    "invalid_amount": {
        "en": "Invalid reinvestment amount",
        "it": "Importo del reinvestimento non valido"
    },

    "investment_confirmation": {
        "en": """
You're about to make a reinvestment of:{reinvestment_amount} BTC""",
        "it": """
Stai per effettuare un reinvestimento di:{reinvestment_amount} BTC"""
    },

    "invalid_amount": {
        "en": "Invalid reinvestment amount",
        "it": "Invalid reinvestment amount (italian)"
    },

    # callback

    "wallet_address_confirmation": {
        "en": """
Your bitcoin wallet address has been set to : 
<strong>{wallet_address}</strong>

You can now make a <b>withdrawal</b>
                """,
        "it": """
Il tuo indirizzo di portafoglio bitcoin è stato impostato su : 
<strong>{wallet_address}</strong>

Ora puoi effettuare un <b>prelievo</b>
                """
    },

    "payout_processing_text": {
        "en": f"""Your payout request will be processed within the next 48 hours""",
        "it": f"""La Vostra richiesta di pagamento sarà eseguita entro le prossime 48 ore"""
    },


    "reinvest_confirmation_text": {
        "en": """
    <b>Done. 
Your reinvest starts on {start_date}
for 180 days up until {close_date}</b>
                """,
        "it": """
    <b>Fatto. 
Il Vostro reinvestimento inizia il {start_date}
per 180 giorni fino al {close_date}</b>
                """
    },

    # transaction


    "transaction_text_info": {
        "en": """
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
        "it": """
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
    },


    # Team


    "invitation_link": {
        "en": """
Invitation link to share with your friends:
https://t.me/{bot_name}?start={user_id}
    """,
        "it": """
Link di invito da condividere con i Vostri amici:
https://t.me/{bot_name}?start={user_id}
    """
    },

    "referral_system_info": {
        "en": """
Refferal system:
1. Level 5%
2. Level 3%
3. Level 1%

Team:
1. Level partner: 10
2. Level partner:  5
3. Level partner:  2

Team volume:
1. Level: 1.000000 BTC
2. Level  0.557777 BTC
3. Level  0.236675 BTC

Total team earnings:
xx.xxxxxx BTC
        """,
        "it": """
Livelli Bonus:
1. Livello 5%
2. Livello 3%
3. Livello 1%

Team:
1. Partner di livello: 10
2. Partner di livello: 5
3. Partner di livello: 2

Totale della squadra:
1. Livello: 1.000000 BTC
2. Livello 0,557777 BTC
3. Livello 0,236675 BTC

Guadagno totale della squadra:
xx.xxxxxx BTC
        """
    },


    "commission_info": {
        "en": """
Your commissions will be added automatically to your main account balance each time a team member makes a deposit or a reinvestment.
        """,
        "it": """
Le Vostre commissioni saranno aggiunte automaticamente al saldo del Vostro conto principale ogni volta che un membro del team effettua un deposito o un reinvestimento. 
        """
    }






}
