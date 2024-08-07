# coding: utf-8
__author__ = 'duyhsieh'

import requests
import traceback
'''
---------- Bot limitations --------------

When sending messages inside a particular chat, avoid sending more than one message per second. 
We may allow short bursts that go over this limit, but eventually you'll begin receiving 429 errors.

If you're sending bulk notifications to multiple users, the API will not allow more than 30 messages per second or so.
Consider spreading out notifications over large intervals of 8—12 hours for best results.

Also note that your bot will not be able to send more than 20 messages per minute to the same group.
'''


####################  Bot Tokens: use token to control corresponding bot to send messages ####################
class BotToken(object):
    HoyeahBotTest001 = '885248820:AAHHAwPemHe18b_OtHwZ2puhWw3WcW3oyss'  # Hoyeah_Test_001
    Hoyeah001 = '519504172:AAGJZMvsgA-2FXM_nlGps-jXRXvJxCZPIps'
    RD7_WarningBot = '966476948:AAHRh3avKqjCOnxjDEdbFBdDIre5ADA68G4'
    RD7_ListBot = '1938081185:AAEGmtBRokgYMACtAdIKZHEYiw3fCjHtPu0'
    ACDRD7_Call_bot = '5127676114:AAGd1q2KxcCJLWhXcCd_RMWF7klvm4M2MRw'

##################### chat ids : specify the group to send message #####################
class ChatIDs(object):
    HoyeahMonitorTest = -374579232
    # HoyeahMonitor     = 411757777 # Bot001 id
    HoyeahMonitor = -387572820
    Analysis_CRM = -1001583511374
    Notify_User_Reward = -505362107
    BlackDiamond = -578108793
    ActivitySettingSync = -508658873
    CoinPusherServiceAlert = -746566555
    MahjongServiceNotify = -4220121946
    TestMessageDaLuanDou = -466971060


class TelegramBot(object):
    def __init__(self, bot_token, logger=None):
        self.request_url_prefix = 'https://api.telegram.org/bot{}'.format(bot_token)
        self.logger = logger

    def __get_request(self, method, extra_args=None):
        url = '{}/{}'.format(self.request_url_prefix, method)

        if isinstance(extra_args, dict):
            for k, v in extra_args.items():
                s = '{}={}'.format(k, v)
                url = url + '&' + s
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True, r.content
            return False, r
        except:
            if self.logger != None:
                self.logger.error(
                    '[TelegramBot] __get_request exception:method={},cs={}'.format(method, traceback.format_exc()))
            return False, None

    def __post_request(self, method, payload, extra_args=None):
        url = '{}/{}'.format(self.request_url_prefix, method)
        try:
            if isinstance(extra_args, dict):
                for k, v in extra_args.items():
                    payload[k] = v
            # payload['parse_mode'] = 'HTML'
            r = requests.post(url=url, data=payload, headers={'application': 'json'}, timeout=2)
            if r.status_code == 200:
                return True, r.content
            return False, r
        except:
            if self.logger != None:
                self.logger.error(
                    '[TelegramBot] __post_request exception:method={},payload={},cs={}'.format(method, payload,
                                                                                               traceback.format_exc()))
            return False, None

    def send_group_text(self, chat_id, text, tag_list=None, extra_args=None):
        # telegram tag名單
        if tag_list is not None and tag_list != []:
            tag_text = ''
            for tag in tag_list:
                tag_text += '@' + (tag if isinstance(tag, str) else tag.encode('utf-8')) + ' '
            tag_text += '\n'
            text = tag_text + text
        payload = {'chat_id': chat_id, 'text': text}
        return self.__post_request('sendMessage', payload, extra_args=extra_args)

    def get_updates(self):
        return self.__get_request('getUpdates')

    def get_bot_info(self):
        return self.__get_request('getMe')


if __name__ == "__main__":
    botID = BotToken.ACDRD7_Call_bot
    bot = TelegramBot(botID)

    chatID = ChatIDs.MahjongServiceNotify
    message = u"""
        <a href="https://tw.news.yahoo.com/">yahoo news</a>
    """
    extra_args = {'parse_mode': 'HTML'}

    print(bot.send_group_text(chatID, message, extra_args=extra_args))
    # print bot.get_updates()
    # print bot.get_bot_info()

