import telebot
from telebot import types
import random
import os

Token = '665567135:AAGdohyS5FcrQ5sVvQEMcQPqV6k8G-tbH-I'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                 ['Расписание', 'Химия',
                  'Пара в данный момент','Поиск инсты(только в ЛС)',
                  'Platonus', 'Прочее']])
    msg = bot.send_message(message.chat.id, 'Привет, я бот созданный для учебы АТТ 17-01 \n'
                                            'Выберите нужную вам функцию ниже:', reply_markup=keyboard)
#Для поиска инсты\Для поиска инсты\Для поиска инсты\Для поиска инсты\Для поиска инсты\Для поиска инсты
def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands = ['suicide'])
def start(message):
    pistol = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/Pistol.jpg'
    pistolyou = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/Pistolyou.jpg'
    emoji = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/semoji.png'
    uganda = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/suganda.png'
    jaba = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/Jaba.jpg'
    duck = 'https://github.com/Maka5000/Akeno/blob/master/img/sd/DDuck.gif'
    suicide = [pistol, pistolyou, emoji, uganda
               , jaba, duck]
    bot.send_message(message.chat.id, random.choice(suicide))


#ФУНКЦИЯ ЛИНЕЙНОЙ КЛАВИАТУРЫ ФУНКЦИЯ ЛИНЕЙНОЙ КЛАВИАТУРЫ ФУНКЦИЯ ЛИНЕЙНОЙ КЛАВИАТУРЫ ФУНКЦИЯ ЛИНЕЙНОЙ КЛАВИАТУРЫ
@bot.callback_query_handler(func = lambda call: call.data)
def inline(call):
    if call.data == 'Расписание':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name)for name in
                       ['2-курс', '3-курс',
                        'Главная']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите курс:',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Поиск инсты(только в ЛС)':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Главная', callback_data='Главная')])
        bot.edit_message_text(chat_id= call.message.chat.id,
                              message_id= call.message.message_id,
                              text = 'Напишите название аккаунта инсты \n'
                                     'Ввиде @(название аккаунта)',
                              parse_mode = 'Markdown',
                              reply_markup=keyboard)

        @bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
        def at_answer(message):
            texts = message.text.split()
            at_text = find_at(texts)
            bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))

    if call.data == 'Пара в данный момент':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data= name) for name in
                       ['Пн', 'Вт', 'Ср',
                        'Чт', 'Пт',
                        'Главная']])
        bot.edit_message_text(chat_id= call.message.chat.id,
                              message_id= call.message.message_id,
                              text = 'Выберите день:',
                              parse_mode= 'Markdown',
                              reply_markup= keyboard)
    #Пара в данный момент\Пара в данный момент\Пара в данный момент\Пара в данный момент\Пара в данный момент\Пара в данный момент\
    #ПонедельникПонедельникПонедельникПонедельникПонедельникПонедельникПонедельникПонедельникПонедельникПонедельник
    if call.data == 'Пн':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Пн 8:00', 'Пн 9:00', 'Пн 10:00',
                        'Пн 11:00', 'Пн 12:00', 'Пн 13:00',
                        'Назад']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите время(Пн)',
                              parse_mode='Markdown',
                              reply_markup=keyboard)


    if call.data == 'Пн 8:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Машиностроительное черчение \n'
                                   'Аудитория 4402',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пн 9:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Машиностроительное черчение \n'
                                   'Аудитория 4402',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пн 10:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Машиностроительное черчение \n'
                                   'Аудитория 4402',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пн 11:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Технология Конструкционных Материалов \n'
                                   'Аудитория 3214',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пн 12:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Физическая культура \n'
                                   'Дене шынықтыру',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пн 13:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пн')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Физическая культура \n'
                                   'Дене шынықтыру',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    #ВторникВторникВторникВторникВторникВторникВторникВторникВторникВторникВторникВторникВторникВторникВторник
    if call.data == 'Вт':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Вт 8:00', 'Вт 9:00', 'Вт 10:00',
                        'Вт 11:00', 'Вт 12:00',
                        'Назад']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите время(Вт)',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Вт 8:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Вт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Химия(Лекция)\n'
                                   'Аудитория 3214',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Вт 9:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Вт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Электротехника(Лекция)\n'
                                   'Аудитория 1117',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Вт 10:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Вт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Казахский язык\n'
                                   'Аудитория 4302',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Вт 11:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Вт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Казахский язык\n'
                                   'Аудитория 4302',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Вт 12:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Вт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Кураторский час\n'
                                   'Аудитория 3106a',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    #СредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСредаСреда
    if call.data == 'Ср':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Ср 8:00', 'Ср 9:00', 'Ср 10:00',
                        'Ср 11:00', 'Ср 12:00',
                        'Назад']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите время(Ср)',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Ср 8:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Ср')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Технология Конструкционных Материалов\n'
                                   'ТКМ(Лабораторка)\n'
                                   'Аудитория 4504',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Ср 9:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Ср')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Технология Конструкционных Материалов\n'
                                   'ТКМ(Лабораторка)\n'
                                   'Аудитория 4504',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Ср 10:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Ср')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Инженерная математика\n'
                                   'Аудитория 4312',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Ср 11:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Ср')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Инженерная математика\n'
                                   'Аудитория 4312',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Ср 12:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Ср')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Религоведение(Лекция)\n'
                                   'Аудитория 1223',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    #Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг#Четверг
    if call.data == 'Чт':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Чт 8:00', 'Чт 9:00', 'Чт 10:00',
                        'Чт 11:00',
                        'Назад']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите время(Чт)',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Чт 8:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Чт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='ТеорМех(Практика)\n'
                                   'Аудитория 4406',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Чт 9:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Чт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='ТеорМех(Лекция)\n'
                                   'Аудитория 1117',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Чт 10:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Чт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Энергосбережение(Лекция)\n'
                                   'Аудитория 3214',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Чт 11:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Чт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Религоведение(Практика)\n'
                                   'Аудитория 4202',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    #ПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятницаПятница
    if call.data == 'Пт':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Пт 8:00', 'Пт 9:00', 'Пт 10:00',
                        'Пт 11:00',
                        'Назад']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите время(Пт)',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Пт 8:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Энергосбережение(Практика)'
                                   'Аудитория 3215',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Пт 9:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Электротехника(Практика)\n'
                                   'Аудитория 4313',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Пт 10:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='ТеорМех(Лабораторка)\ Химия(Лабораторка)\n'
                                   'Аудитория 4406\ 2313',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Пт 11:00':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Пт')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='ТеорМех(Лабораторка)\ Химия(Лабораторка)\n'
                                   'Аудитория 4406\ 2313',
                              parse_mode='Markdown',
                              reply_markup=keyboard)


    #кнопки навигациикнопки навигациикнопки навигациикнопки навигациикнопки навигациикнопки навигациикнопки навигациикнопки навигации
    if call.data == 'Назад':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Пн', 'Вт', 'Ср',
                        'Чт', 'Пт',
                        'Главная']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите день:',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'Главная':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Расписание', 'Химия', 'Кальулятор',
                        'Пара в данный момент', 'Поиск инсты(только в ЛС)',
                        'Platonus']])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Привет, я бот созданный для учебы АТТ 17-01 \n'
                                    'Выберите нужную вам функцию ниже:',
                              parse_mode='Markdown',
                              reply_markup=keyboard)


    #ПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонусПлатонус
    if call.data == 'Platonus':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = 'Перейти на platonus', url = 'http://platonus.kazatu.kz/')
        keyboard.add(url_button)
        keyboard.add(*[types.InlineKeyboardButton(text = 'Главная', callback_data='Главная')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Нажмите чтобы перейти',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    #Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия#Химия
    if call.data == 'Химия':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data=name)for name in
                       ['Срс 6', 'Срс 7']])
        keyboard.add(*[types.InlineKeyboardButton(text='Главная', callback_data='Главная')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Химия СРС',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Срс 7':
        bot.send_document(call.message.chat.id, open('docs\SSW7.docx', 'rb'))
    if call.data == 'Срс 6':
        bot.send_document(call.message.chat.id, open('docs\SSW6.docx', 'rb'))


    #2-курс#2-курс#2-курс #2-курс #2-курс #2-курс #2-курс
    if call.data == '2-курс':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data= name) for name in
                       ['1 семестр', '2-семестр',]])
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='Расписание')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите семестр:',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == '1 семестр':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Пары', 'Экзамен']])
        keyboard.add(*[types.InlineKeyboardButton(text = 'Назад', callback_data='2-курс')])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите пожалуйста:',
                              parse_mode='Markdown',
                              reply_markup=keyboard)
    if call.data == 'Пары':
        bot.send_photo(call.message.chat.id, open('img/Lessons.jpeg', 'rb'))
    if call.data == 'Экзамен':
        bot.send_photo(call.message.chat.id, open('img/sd/DDuck.gif', 'rb'))

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

