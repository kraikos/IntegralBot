import telebot
import datetime
import random

token = ("5720355601:AAE_Xv49an_fSuiZAfit9EhOBC9p24DQNRM")

bot = telebot.TeleBot(token)

id = int()
name = str()
username = str()
chat =int()
today = int()
day = int()
info = str()
vac = int()
vaclist_send = str()
a = int()
b = int()
admin = 1004923094
#admin = 1465233793
settext = str()
chat_id = -1001660016221

group = []
vac_list = []

class student ():
 def init(self, id, name, usename, chat):
  self.id = id
  self.name = name
  self.username = username
  self.chat = chat
  
Ananich = student()
Ananich.id = 1
Ananich.name = 'Самуил'
Ananich.username = '@'
Ananich.chat = 0
group.append(Ananich)

Andreychuk = student()
Andreychuk.id = 2
Andreychuk.name = 'Андрейчук Артем'
Andreychuk.username = '@pailey54'
Andreychuk.chat = 0
group.append(Andreychuk)

Bova = student()
Bova.id = 3
Bova.name = 'Олег'
Bova.username = '@hdjejxb'
Bova.chat = 5623686910
group.append(Bova)

Vrabiy = student()
Vrabiy.id = 4
Vrabiy.name = 'Врабий Павел'
Vrabiy.username = '@vubus'
Vrabiy.chat = 1339070626
group.append(Vrabiy)

Golumbyauskas = student()
Golumbyauskas.id = 5
Golumbyauskas.name = 'Дейвидас'
Golumbyauskas.username = '@puuuulpp'
Golumbyauskas.chat = 1198577161
group.append(Golumbyauskas)

Grechannikov = student()
Grechannikov.id = 6
Grechannikov.name = 'Гречанников Никита'
Grechannikov.username = '@Pypsik_oo'
Grechannikov.chat = 0
group.append(Grechannikov)
\
Dulep = student()
Dulep.id = 7
Dulep.name = 'Дулеп Артем'
Dulep.username = '@VivaLasDeLaVegan'
Dulep.chat = 0
group.append(Dulep)

Karnopel = student()
Karnopel.id = 8
Karnopel.name = 'Егор'
Karnopel.username = '@'
Karnopel.chat = 5082526731
group.append(Karnopel)

Kartavitskiy = student()
Kartavitskiy.id = 9
Kartavitskiy.name = 'Алексей'
Kartavitskiy.username = '@'
Kartavitskiy.chat = 1021321634
group.append(Kartavitskiy)

Kachan = student()
Kachan.id = 10
Kachan.name = 'Качан Владислав'
Kachan.username = '@Vla_dik0'
Kachan.chat = 1266481080
group.append(Kachan)

Korenkov = student()
Korenkov.id = 11
Korenkov.name = 'Николай'
Korenkov.username = '@'
Korenkov.chat = 2138951517
group.append(Korenkov)

Kraiko = student()
Kraiko.id = 12
Kraiko.name = 'Крайко Станислав'
Kraiko.username = '@kraikos'
Kraiko.chat = 1465233793
group.append(Kraiko)

Kurjan = student()
Kurjan.id = 13
Kurjan.name = 'Курьян Артем'
Kurjan.username = '@boulingball'
Kurjan.chat = 1004923094
group.append(Kurjan)

Kuang = student()
Kuang.id = 14
Kuang.name = 'Лаи Куанг'
Kuang.username = '@'
Kuang.chat = 987563741
group.append(Kuang)

Leonov = student()
Leonov.id = 15
Leonov.name = 'Леонов Даниил'
Leonov.username = '@mamlyuk76'
Leonov.chat = 1435016959
group.append(Leonov)

Makas = student()
Makas.id = 16
Makas.name = 'Макась Даниил'
Makas.username = '@abeme55'
Makas.chat = 1145469722
group.append(Makas)

Malishevskiy = student()
Malishevskiy.id = 17
Malishevskiy.name = 'Малишевский Никита'
Malishevskiy.username = '@'
Malishevskiy.chat = 0
group.append(Malishevskiy)

Moroz = student()
Moroz.id = 18
Moroz.name = 'Иван'
Moroz.username = '@Craithed'
Moroz.chat = 1179193435
group.append(Moroz)

NovikovArt = student()
NovikovArt.id = 19
NovikovArt.name = 'Новиков Артем'
NovikovArt.username = '@Nowl2'
NovikovArt.chat = 1243401572
group.append(NovikovArt)

NovikovDan = student()
NovikovDan.id = 20
NovikovDan.name = 'Новиков Даниил'
NovikovDan.username = '@Nyakori'
NovikovDan.chat = 818005764
group.append(NovikovDan)

Petrovskiy = student()
Petrovskiy.id = 21
Petrovskiy.name = 'Кирилл'
Petrovskiy.chat = 1459840499
Petrovskiy.username = '@Kirichkaz'
group.append(Petrovskiy)

Ryzhkovskiy = student()
Ryzhkovskiy.id = 22
Ryzhkovskiy.name = 'Андрей'
Ryzhkovskiy.username = '@Sadboy666665'
Ryzhkovskiy.chat = 1296351988
group.append(Ryzhkovskiy)

Savchin = student()
Savchin.id = 23
Savchin.name = 'Владимир'
Savchin.username = '@Sairus_Demon'
Savchin.chat = 961147939
group.append(Savchin)

Topalov = student()
Topalov.id = 24
Topalov.name = 'Максим'
Topalov.username = '@Makasidinaxyi'
Topalov.chat = 0
group.append(Topalov)

Truhanovich = student()
Truhanovich.id = 25
Truhanovich.name = 'Труханович Владислав'
Truhanovich.username = '@Vlados2456'
Truhanovich.chat = 826207068
group.append(Truhanovich)

FilipovichVal = student()
FilipovichVal.id = 26
FilipovichVal.name = 'Валерий'
FilipovichVal.username = '@reactswagga'
FilipovichVal.chat = 0
group.append(FilipovichVal)

FilipovichEug = student()
FilipovichEug.id = 27
FilipovichEug.name = 'Евгений'
FilipovichEug.username = '@Jemma_got_2936'
FilipovichEug.chat = 0
group.append(FilipovichEug)

Harashkevich = student()
Harashkevich.id = 28
Harashkevich.name = 'Харашкевич Никита'
Harashkevich.username = '@rezeroname'
Harashkevich.chat = 1126441064
group.append(Harashkevich)

Shapovalov = student()
Shapovalov.id = 29
Shapovalov.name = 'Шаповалов Павел'
Shapovalov.username = '@'
Shapovalov.chat = 5178094064
group.append(Shapovalov)

Unitskiy = student()
Unitskiy.id = 30
Unitskiy.name = 'Юницкий Станислав'
Unitskiy.username = '@stas2050'
Unitskiy.chat = 5657017477
group.append(Unitskiy)

def obj(message):
     global day
     global today
     global a
     a = 0
     for student in group:
      if today == student.id:
       for vac_ in vac_list:
        if int(vac_) == int(student.id):
         today = today + 1
         obj()
         a = 1
       if a == 0:
        a = random.uniform(1, 8)
        a = round(a)
        if a == 1:
         settext = 'Сегодня дежурный'
        if a == 2:
         settext = 'Сегодня пашет'
        if a == 3:
         settext = 'Heute arbeit'
        if a == 4:
         settext = 'Сегодня толкает землю'
        if a == 5:
         settext = 'Смена караула'
        if a == 6:
         settext = 'Дворецкий -'
        if a == 7:
         settext = 'Невольный рабочий'
        if a == 8:
         settext = 'Горничная только'
        to_pin = bot.send_message(chat_id, f'<b>{settext} {student.name} ({student.username})</b>', parse_mode = 'html').message_id
        bot.pin_chat_message(chat_id = message.chat.id, message_id = to_pin, disable_notification=False)
        #chat_id = student.chat
        #if not(chat_id == 0):
         #bot.send_message(chat_id, f'<b>Сегодня ты дежурный</b>', parse_mode = 'html')
        today = today + 1
        if today == 30:
         today = 1
        break

@bot.message_handler(commands=['start'])
def start(message):
 global today
 global a
 a = 0
 while True:  
  time = datetime.datetime.now()
  time = time.time()
  if time.hour == (7) and time.minute == (0) and time.second == (0) and time.microsecond < 10 and not(datetime.datetime.today().weekday() == 6):
   obj(message)      
 
@bot.message_handler(commands=['vac'])
def vac(message):
 global vac_list
 if message.from_user.id == admin:
  vac = message.text.replace('/vac ', '')
  vac_list.append(vac)
 else:
  bot.send_message(message.chat.id,  f'<b>Ты не админ</b>', parse_mode = 'html')
   
@bot.message_handler(commands=['revac'])
def revac(message):
 if message.from_user.id == admin:
     vac = message.text.replace('/revac ', '')
     for vac_ in vac_list:
        if vac_ == vac:
            vac_list.remove(vac_)
 else:
  bot.send_message(message.chat.id, f'<b>Ты не админ</b>', parse_mode = 'html')
   
@bot.message_handler(commands=['vaclist'])
def vaclist(message):
 if message.from_user.id == admin:
  global vaclist_send
  for vac_ in vac_list:
   vaclist_send = str(vaclist_send + str(vac_) + '\n')
  bot.send_message(message.chat.id, ('Болеющие: \n' + vaclist_send))
  vaclist_send = ''
 else:
  bot.send_message(message.chat.id, f'<b>Ты не админ</b>', parse_mode = 'html')
  
@bot.message_handler(commands=['help'])
def help(message):
 if message.from_user.id == admin:
  bot.send_message(message.chat.id, 
  '<b><i>/start</i> - запуск бота</b>\n' +
  '<b><i>/setup</i> - назначение дежурного на следующий день</b>' 
  '<b><i>/vac (id учащегося)</i> - скип</b>\n' + 
  '<b><i>/revac (id учащегося)</i> - дескип</b>\n' +
  '<b><i>/vaclist</i> - скипнутые</b>\n' + 
  '<b><i>/set - (id учащегося / next)</i> - моментальное объявление по id / следующего по списку</b>',
  parse_mode = 'html'
  )
 else:
  bot.send_message(message.chat.id, f'<b>Ты не админ</b>', parse_mode = 'html')

@bot.message_handler(commands=['set'])
def set(message): 
 global today
 if message.from_user.id == admin:
  if message.text == '/set next':
   today = today + 1
   obj(message)
  else:
   today = int(message.text.replace('/set ', ''))
   obj(message)
 else:
    bot.send_message(message.chat.id, f'<b>Ты не админ</b>', parse_mode = 'html')
    
@bot.message_handler(commands=['setup']) 
def setup(message):
 today = message.text.replace('/setup  ', '')
      
bot.polling()
