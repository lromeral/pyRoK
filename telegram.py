import telebot

class telegram_notify:
    def __init__(self) -> None:
        API_TOKEN = '6414179618:AAH2U00A7eaMTo_vtFZGrmydqFPnvdUL2b4'
        self.bot = telebot.TeleBot(API_TOKEN)
        self.__chatid_luis = '118987835'

    def send_message(self,mensaje:str):
        self.bot.send_message(self.__chatid_luis,mensaje)
