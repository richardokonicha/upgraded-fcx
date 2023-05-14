# Telegram Bot Configuration
TOKEN = '******:AAFkRQbtqA0RZgwIwAYmBjLyjhAvdWB******'
DEBUG = True

# Webhook Configuration
WEBHOOKMODE = True
WEBHOOK_URL = 'https://5001-******-upgradedfcx-82z3zmfnasf.ws-eu97.gitpod.io'

# Database Configuration
POSTGRES_URL = "postgres://default:******@ep-calm-brook-****.us-east-1.postgres.vercel-storage.com:5432/verceldb"
SQLITE_URL = 'sqlite:///database/database.db'

# Merchant Configuration
MERCHANT_ID = "c4baf6ef23be73a2da7*******"
MERCHANT_PKEY = "c68f21F77B13FE4D6617EfcD0287c036da7A3aB1A5f3e870fb179E****"
MERCHANT_PBKEY = "953b0c668c9d75c2d3da984f62a00fd269dc66c6da701250a0d7e1******"

# IPN Configuration
IPN_URL = "https://5000-****-literateoct-ggrcswrdmbv.ws-eu97.gitpod.io"

# Admin Configuration
ADMIN_ID = 1053579181

# Financial Configuration
WITHDRAWAL_MINIMUM_AMOUNT = 0.002
DAILY_PROFITS = 0.1
DURATION_REINVEST = 1

# Validation
if not TOKEN:
    sys.exit('Missing env variable TOKEN')
