import os
import sys
from dotenv import load_dotenv
load_dotenv()


# Validate the most important variables
required_variables = ['TOKEN', 'WEBHOOK_URL']

for variable in required_variables:
    if variable not in os.environ:
        sys.exit(f'Missing environment variable: {variable}')


# Telegram Bot Configuration
TOKEN = os.getenv('TOKEN', '5529901971:AAE1EP8JSAaFznJAUeDe4Yo4Eje3SgokCRk')
DEBUG = os.getenv('DEBUG', 'True')
PORT = os.getenv('PORT', 5001)

# Webhook Configuration
WEBHOOKMODE = os.getenv('WEBHOOKMODE', 'True')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://5001-richardokon-upgradedfcx-82z3zmfnasf.ws-eu97.gitpod.io')

# Database Configuration
POSTGRES_URL = os.getenv('POSTGRES_URL', "postgres://default:***@ep-calm-brook-757839.us-east-1.postgres.vercel-storage.com:5432/verceldb")
SQLITE_URL = os.getenv('SQLITE_URL', 'sqlite:///database/database.db')

# Merchant Configuration
MERCHANT_ID = os.getenv('MERCHANT_ID', "c4baf6ef23be73a2da7fa05********")
MERCHANT_PKEY = os.getenv('MERCHANT_PKEY', "c68f21F77B13FE4D6617EfcD0287c036da7A3aB1A5f3e870fb179E94********")
MERCHANT_PBKEY = os.getenv('MERCHANT_PBKEY', "953b0c668c9d75c2d3da984f62a00fd269dc66c6da701250a0d7e14********")

# IPN Configuration
IPN_URL = os.getenv('IPN_URL', "https://5001-richardokon-upgradedfcx-82z3zmfnasf.ws-eu97.gitpod.io")
PROXY = os.getenv('PROXY', 'http://proxy_ip:proxy_port')

# Admin Configuration
ADMIN_ID = os.getenv('ADMIN_ID', 1053579181)

# Financial Configuration
WITHDRAWAL_MINIMUM_AMOUNT = float(os.getenv('WITHDRAWAL_MINIMUM_AMOUNT', '0.002'))
DAILY_PROFITS = float(os.getenv('DAILY_PROFITS', '0.1'))
DURATION_REINVEST = int(os.getenv('DURATION_REINVEST', '1'))

# Validation
if not TOKEN:
    sys.exit('Missing env variable TOKEN')


