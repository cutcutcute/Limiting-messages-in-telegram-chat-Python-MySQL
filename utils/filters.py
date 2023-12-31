
from aiogram.types import Message

from botAttr import BotConfig

botCfg : BotConfig = BotConfig()
groupById = botCfg.groupId




def startMessage(message : Message) -> bool:
    return message.text == "/start"



def groupByHandler(message : Message) -> bool:
    return message.chat.id == groupById

def messageForUser(message : Message) -> bool:
    return message.text.startswith("@") and message.chat.id == botCfg.adminId