# FCX Bot

## Introduction
FCX Bot is a Telegram bot that provides various features and functionalities related to a virtual currency. It allows users to perform actions such as creating an account, checking balances, making deposits, requesting withdrawals, and participating in a referral program.

## Functionality
The FCX Bot offers the following functionalities:

### Account Management
- Users can create an account and set their preferred language.
- Users can view their account balance.

## Deposits and Promo Codes

The application supports deposits and promo codes to enhance user experience and testing capabilities.

### Deposits

Users can make deposits to their accounts using the following steps:

1. Enter the desired deposit amount.
2. The application will generate a unique deposit address for the user.
3. The user can complete the deposit by sending the specified amount to the provided address.
4. Once the deposit is confirmed, the user's account balance will be updated accordingly.
5. Deposits can be made using the supported currency (e.g., BTC).

Please note that there might be minimum deposit requirements or restrictions based on the configuration and payment provider settings.

### Promo Codes

Promo codes can be used to add virtual funds to a user's account for testing purposes. Here's how it works:

1. Enter the promo code in the appropriate input field.
2. If the promo code is valid, the specified amount will be added to the user's account balance.
3. The user can then use the virtual funds to test other features of the application.
4. Promo codes are typically provided for testing and promotional purposes.

Please note that promo codes might have expiration dates or usage limitations based on the application's policies.

Feel free to explore the deposit and promo code functionality to enhance your testing experience!


## Withdrawals

Users can withdraw funds from their accounts using the following steps:

1. Enter the desired withdrawal amount.
2. If the account balance is sufficient, the user will be prompted to enter their wallet address.
3. Enter the wallet address where the funds should be transferred.
4. Confirm the withdrawal request.
5. The requested amount will be deducted from the user's account balance.
6. The withdrawal will be processed, and the funds will be transferred to the specified wallet address.

Please note the following:

- There might be a minimum withdrawal amount set by the application.
- If the account balance is insufficient to cover the withdrawal amount, the user will be notified.
- The provided wallet address must be valid and follow the specified format.
- Withdrawal requests are typically processed within a certain timeframe.

Ensure that you have sufficient account balance and provide a valid wallet address to successfully withdraw funds from your account.

Feel free to explore the withdrawal functionality to manage your account balance effectively!


## Investment

The application provides an investment feature that allows users to reinvest their funds. The investment strategy is as follows:

1. When a user chooses to reinvest, they will be prompted to enter the amount they want to reinvest.

2. The application will validate the reinvestment amount against the user's account balance.

3. If the reinvestment amount is greater than the account balance, an error message will be displayed.

4. If the reinvestment amount is valid, the user will be presented with a confirmation message showing the reinvestment details, including the amount.

5. Upon confirming the reinvestment, the user's account balance will be updated, deducting the reinvestment amount.

6. A new investment transaction will be created, indicating the reinvestment type, amount, and the updated account balance.

7. The user will receive a reinvestment confirmation message with the start date and close date of the investment.

To initiate the reinvestment process, users can use the "/reinvest" command or access the reinvestment option through the user interface.

Please note that there is a minimum withdrawal amount set in the configuration file (config.WITHDRAWAL_MINIMUM_AMOUNT). If a user's account balance falls below this amount, they will not be able to reinvest.

Feel free to explore the investment feature and optimize your earnings!


### Referral Program
- Users can participate in a referral program and earn commissions from their referred team members' activities.
- Commission percentages are provided for different referral levels.
- Users can view their team members and the corresponding team volumes.
- Total team earnings are displayed.

## Getting Started
To use the FCX Bot, follow these steps:
1. Start a chat with the bot on Telegram.
2. Create an account by providing the necessary information.
3. Use the available commands and buttons to perform various actions.

## Installation
To run the FCX Bot locally, follow these steps:
1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your Telegram bot token and other configurations in the `config.py` file.
4. Run the bot: `python bot.py`


or use Docker or docker compose
docker compose up 

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).