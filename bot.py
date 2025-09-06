from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Replace with your bot token and personal Telegram ID
BOT_TOKEN = "8426690338:AAHVKQyeoL2mTBnThXpZMwYhBMWxVIJyf9Y"
MY_CHAT_ID = 6231126068

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Forward the incoming message to your Telegram account
    if update.message:
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text=f"Message from (esmashono gheyr faal kardam khasti byan bego):\n\n{update.message.text}"
        )

# Main function
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Listen to all messages sent to the bot
app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot is running...")
app.run_polling()
