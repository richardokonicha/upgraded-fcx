# Create files for handlers in this folder.
import re
from .admin import admin_user
from .spam_command import anti_spam
from .user import any_user
from .start import start
from .language import show_language, set_language
from .balances import balance
from .supports import support
from .deposits import deposit, promo


def register_handlers(bot):
    bot.register_message_handler(
        admin_user, commands=['startadmin'], admin=True, pass_bot=True)
    bot.register_message_handler(
        any_user, commands=['starttest'], admin=False, pass_bot=True)
    bot.register_message_handler(
        anti_spam, commands=['spam'], pass_bot=True)
    bot.register_message_handler(
        start, commands=['start'], admin=False, pass_bot=True)
    bot.register_message_handler(
        set_language,
        func=lambda message: message.content_type == "text"
        and re.search(r"^(English|Italiano)", message.text),
        admin=False, pass_bot=True
    )
    bot.register_message_handler(
        show_language,
        func=lambda message: message.content_type == "text"
        and any(re.search(pattern, message.text, re.IGNORECASE) for pattern in ['^.+language', '^.+linguaggio', '^/lang', '^/language']),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        balance,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'^balance', message.text.split()[0], re.IGNORECASE)) or 
            bool(re.search(r'^bilance', message.text.split()[0], re.IGNORECASE))
            ),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        support,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'Support$', message.text, re.IGNORECASE)) or 
            bool(re.search(r'Supporto$', message.text, re.IGNORECASE))
            ),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        deposit,
        func=lambda message: message.content_type == "text"
        and (
               bool(re.search(r'deposit$', message.text, re.IGNORECASE)) or 
               bool(re.search(r'Depositare$', message.text, re.IGNORECASE))
            ),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        promo,
        func=lambda message: message.content_type == "text"
        and (
               bool(re.search(r'^PROMO', message.text, re.IGNORECASE))
            ),
        admin=False, pass_bot=True
    )
    
