import sys

from telethon.tl.functions.channels import JoinChannelRequest

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .funcs.logger import logging
from .funcs.session import deadlyub
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("Deadly")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    deadlyub.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class DeadlyCheck:
    def __init__(self):
        self.sucess = True


Deadlycheck = DeadlyCheck()
# Join Deadly X Channel after deploying 🤐😅
# Why not come here and chat??
async def hehn():
    try:
        await deadlyub(JoinChannelRequest("@deadly_techy"))
    except BaseException:
        pass


async def startup_process():
    check = await ipchange()
    if check is not None:
        Deadlycheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("Yay your deadly-userbot Userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if deadlyub is live\
        \nIf you need assistance, head to https://t.me/deadly_userbot"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Deadlycheck.sucess = True
    return


deadlyub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    deadlyub.disconnect()
elif not Deadlycheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        deadlyub.run_until_disconnected()
    except ConnectionError:
        pass
