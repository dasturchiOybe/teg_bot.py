import telebot
from telebot import types

bot = telebot.TeleBot('7145638793:AAGkZEtgcjWvtUAc5e0aNYxk6XA_lPaEepQ')

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.from_user.id, 'Salom ' + name, reply_markup=get_main_keyboard())

@bot.message_handler(content_types=['text'])
def send(message):
    text = message.text.lower()
    if text == 'python':
        send_python_video(message.from_user.id)
    elif text == 'java':
        send_java_video(message.from_user.id)
    elif text == 'php':
        send_php_video(message.from_user.id)
    elif text == 'c#':
        send_csharp_video(message.from_user.id)
    else:
        bot.send_message(message.from_user.id, 'Uzur, men sizi tanimayman 😑😂', reply_markup=get_main_keyboard())

def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Python')
    button2 = types.KeyboardButton('Java')
    button3 = types.KeyboardButton('Php')
    button4 = types.KeyboardButton('C#')
    keyboard.add(button1, button2, button3, button4)
    return keyboard

def send_python_video(chat_id):
    video_path = 'C:\Users\Oybek\Desktop\teg_bot_c#\teg_bot\498c9e3ed900e770b4412acefe9becbada24d82cf6506fc9f64beaee43fff115.mp4'  # Replace with the actual path of the Python video file
    video = open(video_path, 'rb')
    bot.send_video(chat_id, video)

def send_java_video(chat_id):
    video_id = 'C:\Users\Oybek\Desktop\teg_bot_c#\teg_bot\498c9e3ed900e770b4412acefe9becbada24d82cf6506fc9f64beaee43fff115.mp4'  # Replace with the video ID or URL of the Java video you want to send
    bot.send_video(chat_id, video_id)

def send_php_video(chat_id):
    video_id = 'C:\Users\Oybek\Desktop\teg_bot_c#\teg_bot\498c9e3ed900e770b4412acefe9becbada24d82cf6506fc9f64beaee43fff115.mp4'  # Replace with the video ID or URL of the Php video you want to send
    bot.send_video(chat_id, video_id)

def send_csharp_video(chat_id):
    video_id = 'C:\Users\Oybek\Desktop\teg_bot_c#\teg_bot\498c9e3ed900e770b4412acefe9becbada24d82cf6506fc9f64beaee43fff115.mp4'  # Replace with the video ID or URL of the C# video you want to send
    bot.send_video(chat_id, video_id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True)