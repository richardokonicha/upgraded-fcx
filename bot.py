import os
# filters

from telebot import apihelper, types as telebot_types
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func

# states
from tgbot.states.register_state import Register

# utils
from tgbot.utils.database import Database

# telebot
from telebot import TeleBot

# config
from tgbot import config

from flask import Flask, request

server = Flask(__name__)

db = Database()

# remove this if you won't use middlewares:
apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
bot = TeleBot(config.TOKEN, num_threads=5)


def register_handlers():
    bot.register_message_handler(
        admin_user, commands=['start'], admin=True, pass_bot=True)
    bot.register_message_handler(
        any_user, commands=['start'], admin=False, pass_bot=True)
    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)


register_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])


# custom filters
bot.add_custom_filter(AdminFilter())


@server.route('/' + config.TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot_types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    hook = f'{config.WEBHOOK_URL}/{config.TOKEN}'
    bot.set_webhook(url=hook)
    return f'!hooked to auto updated {hook}', 200


def run_web():
    if __name__ == "__main__":
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))


def run_poll():
    webhook_info = bot.get_webhook_info()
    if webhook_info.url:
        bot.delete_webhook()
    bot.infinity_polling()


if not config.WEBHOOKMODE:
    run_poll()
else:
    run_web()
