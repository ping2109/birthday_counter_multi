import os
import time
import datetime
import telegram
from telegram import Sticker, PhotoSize, TelegramError, StickerSet, MaskPosition, Bot
from telegram.error import BadRequest

bot_token = os.getenv('TOKEN')
channel = os.getenv('TG_ID')

username = os.getenv('USERNAME8')

def get_user_birthday():
    year = int(os.getenv('YEAR8'))
    month = int(os.getenv('MONTH8'))
    day = int(os.getenv('DATE8')) + 1
    birthday = datetime.datetime(year, month, day)
    return birthday

def compute_birthday_difference(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    difference = date1 - date2
    days = int(difference.total_seconds()/60/60/24)
    return days

def main():
    bday = get_user_birthday()
    now = datetime.datetime.now()
    days = compute_birthday_difference(bday, now)
    days2 = int(365)
    ogbday = bday.strftime("%x")
    while days < 0:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""{username}'s birthday is in {format(-days)} days.""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
    if days > 0:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""{username}'s birthday is in {days2 - days} days.""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
    else:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""*Happy birthday to {username}!\nMake a wish 🥳\n\nHis/Her date of birth: {ogbday}*""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
        
main()