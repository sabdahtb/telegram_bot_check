import os
import requests
import telegram
from dotenv import load_dotenv
import telegram.ext.filters as Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Welcome to your Dex Checker Bot! Please enter a token address to check.')


def extract_address_from_url(url):
    # Remove any leading or trailing slashes
    url = url.strip('/')
    # Split by '/' and take the last part
    parts = url.split('/')
    address = parts[-1]
    return address


def fetch_token_info(address: str) -> str:
    api_url = 'https://checkdex.xyz/api/checkToken'
    params = {
        'tokenAddress': address
    }
    try:
        response = requests.get(api_url, params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error fetching data: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"


def message_handler(update: Update, context: CallbackContext) -> None:
    try:
        text = update.message.text
        address = extract_address_from_url(text)

        token_info = fetch_token_info(address)

        if "error" in token_info:
            update.message.reply_text(token_info["error"])
        else:
            exists = token_info["exists"]
            symbol = token_info["symbol"]

            if exists:
                reply_message = f"*✅ Dexscreener PAID for {symbol} ✅* \n\n CA: `{address}`"
            else:
                reply_message = f"*❗️ Dexscreener is NOT PAID for {symbol} ❗️* \n\n CA: `{address}`"

            keyboard = [[InlineKeyboardButton(
                "🌐 CheckDex", url=f"https://checkdex.xyz/?tokenAddress={address}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            sent_message = update.message.reply_text(
                reply_message, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=reply_markup)
            context.user_data['last_message'] = sent_message.message_id
    except:
        update.message.reply_text(
            f"Something went wrong when checking: {address} \n\nMake sure you paste the correct CA or try again later.")
    finally:
        print(f"finish check : {address}")


def main():
    # Ensure only one instance of the bot is running
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.Filters.text & ~
                   Filters.Filters.command, message_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
