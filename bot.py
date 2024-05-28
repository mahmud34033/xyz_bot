import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_html(
        rf'Hi {user.mention_html()}! I am your Eco Bot. Use /help to see available commands.',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Available commands:\n'
                              '/start - Start the bot\n'
                              '/tips - Get eco-friendly tips\n'
                              '/news - Get the latest environmental news')

def tips(update: Update, context: CallbackContext) -> None:
    eco_tips = [
        "Reduce, Reuse, Recycle.",
        "Use reusable bags instead of plastic ones.",
        "Save water by taking shorter showers.",
        "Turn off lights when you leave a room.",
        "Plant a tree to help combat deforestation."
    ]
    update.message.reply_text("\n".join(eco_tips))

def news(update: Update, context: CallbackContext) -> None:
    # For simplicity, here are static news items. In a real bot, fetch news from an API.
    environmental_news = [
        "The Great Green Wall Initiative in Africa is restoring degraded landscapes.",
        "New study shows the impact of plastic pollution on marine life.",
        "Countries pledge to reduce carbon emissions by 2030.",
        "Innovative startups are turning waste into energy."
    ]
    update.message.reply_text("\n".join(environmental_news))

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("7374004152:AAE_THg9kxd_3FoKS-qEDZ9WyRB3w-IC-2s")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("tips", tips))
    dispatcher.add_handler(CommandHandler("news", news))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
