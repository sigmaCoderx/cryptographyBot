
import json
import requests
from telebot import TeleBot,types,util
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from telebot.util import user_link

cookies = {
    'JSESSIONID': '0413B01DE1D50EB6E934A4AF3B81FD87',
    '_ga': 'GA1.2.1776143206.1707729555',
    '_gid': 'GA1.2.2126559775.1707729556',
    '_gat_gtag_UA_84736616_3': '1',
    '_ga_HQ38TFJWV2': 'GS1.1.1707729555.1.1.1707729584.0.0.0',
}

headers = {
    'authority': 'www.devglan.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8,ru;q=0.7,am;q=0.6',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'JSESSIONID=0413B01DE1D50EB6E934A4AF3B81FD87; _ga=GA1.2.1776143206.1707729555; _gid=GA1.2.2126559775.1707729556; _gat_gtag_UA_84736616_3=1; _ga_HQ38TFJWV2=GS1.1.1707729555.1.1.1707729584.0.0.0',
    'origin': 'https://www.devglan.com',
    'referer': 'https://www.devglan.com/online-tools/text-encryption-decryption',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


bot = TeleBot("6615646401:AAEcGGhblm1hezvXx3bd9VZEMuEJnnUR61I",parse_mode="HTML")

button = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
button.add(group,channel)

encDec = InlineKeyboardMarkup()
encDec.row_width = 2
encrypt = InlineKeyboardButton(text="Encrypt",callback_data="enc")
decrypt = InlineKeyboardButton(text="Decrypt",callback_data="dec")
group = InlineKeyboardButton(text="Join Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Join Channel",url="t.me/neuralp")
encDec.add(encrypt,decrypt,group,channel)

@bot.message_handler(commands=["start"])
def startMsg(msg):
    user = msg.from_user
    bot.reply_to(msg,f"Hey {user_link(user)} Send me message to encrypt.",reply_markup=button)

@bot.message_handler(func=lambda m:True)
def getText(msg):
    userMsg = msg.text
    bot.send_message(msg.chat.id,userMsg,reply_markup=encDec)

@bot.callback_query_handler(func=lambda m:True)
def encodeDecode(msg):
    userMsg = msg.message.text

    encrypter_data = {
        'textToEncrypt': userMsg,
        'encryptedText': 'yDp5xtfNShn4Ihl/Ru2H0Q==',
        'textToDecrypt': None,
        'decryptedText': None,
        'deSecretKey': None,
        'secretKey': None,
    }

    encrypter = requests.post('https://www.devglan.com/online-tools/text-encryption', cookies=cookies, headers=headers, json=encrypter_data)
    data_enc= json.loads(encrypter.text)
    #print(data_enc)
    encrypted = data_enc['encryptedText']
    #print(encrypted)

    decrypter_data = {
    'textToEncrypt': None,
    'encryptedText': encrypted,
    'textToDecrypt': userMsg,
    'decryptedText': userMsg,
    'deSecretKey': None,
    'secretKey': None,
    }

    decrypter = requests.post('https://www.devglan.com/online-tools/text-decryption', cookies=cookies, headers=headers, json=decrypter_data)
    data_dec = json.loads(decrypter.text)
    #print(data_dec)
    decrypted = data_dec['decryptedText']

    if msg.data == "enc":
        bot.edit_message_text(f"<code>{encrypted}</code>",msg.message.chat.id,msg.message.id,reply_markup=encDec)
    elif msg.data == "dec":
        bot.edit_message_text(f"<code>{decrypted}</code>",msg.message.chat.id,msg.message.id,reply_markup=encDec)

bot.infinity_polling()