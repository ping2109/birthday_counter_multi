import os
import telegram
from telegram import Sticker, PhotoSize, TelegramError, StickerSet, MaskPosition, Bot
from telegram.error import BadRequest

bot_token = os.getenv('TOKEN')
channel = os.getenv('TG_ID')

def send_sticker():
    try:
        telegram_notify = telegram.Bot(bot_token)
        telegram_notify.send_sticker(chat_id=channel, sticker='CAACAgUAAxkBAAEFMqtixFUN45DlPrBIny5sE0ig2Jb0xgACUgYAAhMaeFV4MXTgwgaQOikE')
    except Exception as ex:
        print(ex)

send_sticker()
