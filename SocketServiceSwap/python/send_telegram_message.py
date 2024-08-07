# coding: utf-8

import sys, traceback
from telegram_bot import TelegramBot, BotToken, ChatIDs
from logger import get_logger


def main(logger, message):
    botID = BotToken.ACDRD7_Call_bot
    chatID = ChatIDs.MahjongServiceNotify

    try:
        if isinstance(message, unicode):
            message = message.encode('utf-8')
        else:
            message = str(message)

        bot = TelegramBot(botID)
        bot.send_group_text(chatID, message)
        return 0
    except:
        logger.error(traceback.format_exc())
        return 1


if __name__ == "__main__":
    logger = get_logger('send_telegram_message')
    if len(sys.argv) > 1:
        result = main(logger, sys.argv[1])
        print(result)
    else:
        logger.error('no message to send')
        print(1)
