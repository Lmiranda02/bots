from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

def get_url():
    contenido = requests.get('https://random.dog/woof.json').json()
    url = contenido['url']
    return url

def get_image_url():
    extensiones = ['jpg','jpeg','png']
    extensionArchivo = ''
    while extensionArchivo not in extensiones:
        url = get_url()
        extensionArchivo = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('2100424095:AAHCuv2fjvKRVxYgOuhYMVcXq8a_tCbOhQ8', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
