from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Path to the question papers directory
BASE_DIR = "./papers"

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message and instructions."""
    update.message.reply_text(
        "Welcome to the Question Paper Bot! 📚\n"
        "Use the commands below to download question papers:\n"
        "/class9 - Get Class 9 question papers\n"
        "/class10 - Get Class 10 question papers\n"
        "/class11 - Get Class 11 question papers\n"
        "/class12 - Get Class 12 question papers"
    )

def send_papers(update: Update, context: CallbackContext, class_dir: str) -> None:
    """Send question papers for the specified class."""
    papers_path = os.path.join(BASE_DIR, class_dir)
    if os.path.exists(papers_path):
        files = os.listdir(papers_path)
        if files:
            update.message.reply_text("Here are the question papers:")
            for file_name in files:
                file_path = os.path.join(papers_path, file_name)
                context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, 'rb'))
        else:
            update.message.reply_text("No question papers available yet.")
    else:
        update.message.reply_text("Invalid class directory.")

def class9(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "class_9")

def class10(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "class_10")

def class11(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "class_11")

def class12(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "class_12")

def main():
    """Start the bot."""
    # Replace with your BotFather token
    TOKEN = "8198511912:AAFX_Ouz8fFZZTn0b-nNEdOn52o2_sqJjyA"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("class9", class9))
    dispatcher.add_handler(CommandHandler("class10", class10))
    dispatcher.add_handler(CommandHandler("class11", class11))
    dispatcher.add_handler(CommandHandler("class12", class12))

    # Start polling
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
