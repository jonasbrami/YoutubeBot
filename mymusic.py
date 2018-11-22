from telegram.ext import Updater
from subprocess import check_output
import subprocess
updater = Updater(token='')

dispatcher = updater.dispatcher


def youtube(bot,update,args):
    cmd="youtube-dl -o '/home/jonas/Music/youtube-dl/%(title)s.%(ext)s' -f bestaudio[ext=m4a] --embed-thumbnail --extract-audio --audio-quality 0 " + args[0]
    print(cmd)
    out=check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    print(out)
    bot.send_message(chat_id=update.message.chat_id, text=out)

from telegram.ext import CommandHandler
start_handler = CommandHandler('youtube', youtube ,pass_args=True)
dispatcher.add_handler(start_handler)

updater.start_polling()
