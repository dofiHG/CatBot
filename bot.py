import telebot 
import types
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    mes = (f'<b>Привет, <u>{message.from_user.first_name}</u></b>,  это тестовый бот, посвящённый котикам. Чтобы узнать, что может бот, нужно ввести "/info"\n')
    bot.send_message(message.chat.id, mes, parse_mode='html')

@bot.message_handler(commands=['info'])
def info(message):
    mesinf = ('Вот что может бот \n'
    '1) чтобы получать случайную картинку: команда /photo (всего 5 картинок, собери все!) \n'
    '2) чтобы послушать мурчание: комада /mrrr \n'
    '3) чтобы получить случайное видео: команда /video (всего 3 видео, собери все!)\n'
    '4) для обратной связи: команда /send (отправка сообщения мне на почту)\n\n'
    'Если возникают трудности, нажмите на значок сбоку от чата или введите "/" для просмотра команд'
    )
    bot.send_message(message.chat.id, mesinf, parse_mode='html')

@bot.message_handler(commands=['photo'])
def photo(message):
    photo1 = open('img/cat1.jpeg', 'rb')
    photo2 = open('img/cat2.jpg', 'rb')
    photo3 = open('img/cat3.jpg', 'rb')
    photo4 = open('img/cat4.jpg', 'rb')
    photo5 = open('img/cat5.jpg', 'rb')
    masph = [photo1, photo2, photo3, photo4, photo5]
    bot.send_photo(message.chat.id, masph[randint(0, 4)])

@bot.message_handler(commands=['mrrr'])
def audio(message):
    audio1 = open('audio/mrrr.mp3', 'rb')
    bot.send_audio(message.chat.id, audio1)

@bot.message_handler(commands=['video'])
def video(message):
    video1 = open('video/vid1.mp4', 'rb')
    video2 = open('video/vid2.mp4', 'rb')
    video3 = open('video/vid3.mp4', 'rb')
    masvid = [video1, video2, video3]
    bot.send_video(message.chat.id, masvid[randint(0, 2)])

@bot.message_handler(commands=['send'])
def func(message):
    bot.send_message(message.chat.id, 'Введите отзыв')


@bot.message_handler()
def send_email(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        fromaddr = 'LOGGIN_FROM'
        toaddr = 'LOGGIN_TO'
        mypass = 'PASS_FROM'
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Отправитель: Telegram bot: "   + username
        body = "Message: Telegram_bot \n\n" + message.text
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        bot.reply_to(message, "Сообщение отправлено!")
    except Exception:
        bot.reply_to(message, "ERROR")
   
bot.polling(none_stop=True)