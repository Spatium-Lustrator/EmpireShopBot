import telebot
from telebot import types
###
first_prod = None
token = ""
zero = 0
bot = telebot.TeleBot(token)

all_data1 = {'1': 'tie_fig', '2': 'tie_def', '3': 'tie_int', 'now_id': 1}

all_data = {'last_order_id': 0, 'counts': 0, 'now_id': None, 'now_prod': None, 'now_price': None, 'now_del': None,
            'mesid': None}

place = {1: 'Татуин, Мос Эйсли, пл. №14',
         2: 'Корусант, Бывший Храм Джедаев, пл. №3',
         3: 'Лотал, столица, пл. №9'}

product_data = {'tie_fig': {'beat_name': 'TIE-fighter', 'price': 500, 'desc': 'Обычный истребитель'},
                'tie_def': {'beat_name': 'TIE-defender', 'price': 600, 'desc': 'Улучшенный истребитель, проект предложен гранд-адмиралом Трауном'},
                'tie_int': {'beat_name': 'TIE-intereceptor', 'price': 650, 'desc': 'Резвый истребитель в Ваши ряды!'}}


check_markup = types.InlineKeyboardMarkup(row_width=2)
but8 = types.InlineKeyboardButton('Да, все верно', callback_data='right')
but9 = types.InlineKeyboardButton('Нет, не так', callback_data='un_right')
check_markup.add(but8, but9)

markup1 = types.InlineKeyboardMarkup(row_width=3)  # меню TIE типа
but1 = types.InlineKeyboardButton('TIE-fighter', callback_data='tie1')
but2 = types.InlineKeyboardButton('TIE-defender', callback_data='tie2')
but3 = types.InlineKeyboardButton('TIE-interceptor', callback_data='tie3')
bu5 = types.InlineKeyboardButton('>>>', callback_data='>')
bu6 = types.InlineKeyboardButton('<<<', callback_data='<')
markup1.add(but1, but2, but3, bu6, bu5)

delete_markup = types.InlineKeyboardMarkup(row_width=2)
delete_markup1 = types.InlineKeyboardMarkup(row_width=2)
delete_markup2 = types.InlineKeyboardMarkup(row_width=2)
del1 = types.InlineKeyboardButton('Удалить', callback_data='del1')
del_all = types.InlineKeyboardButton('Очистить корзину', callback_data='delall')
delete_markup.add(del1)
delete_markup1.add(del1, del_all)
delete_markup2.add(del1, del_all)

adresses_markup = types.InlineKeyboardMarkup(row_width=2)
butt5 = types.InlineKeyboardButton('Татуин, Мос Эйсли, пл. №14', callback_data='place1')
but6 = types.InlineKeyboardButton('Корусант, Бывший Храм Джедаев, пл. №3', callback_data='place2')
but7 = types.InlineKeyboardButton('Лотал, столица, пл. №9', callback_data='place3')
adresses_markup.add(butt5, but6, but7)


def oplata(message):
    try:
        import requests
        import json
        import sqlite3
        from random import randint

        phone = str(message.text)
        sum = shop_bd.basket['all_price']
        random_code = randint(100000, 999999)

        conn = sqlite3.connect('db.db')
        c = conn.cursor()

        QIWI_TOKEN = '33a620d083281a4a3641f7845563bc5b'
        QIWI_ACCOUNT = '79109024495'

        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
        parameters = {'rows': '50'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments', params=parameters)
        req = json.loads(h.text)

        c.execute("CREATE TABLE IF NOT EXISTS payment_query(user_id INTEGER, phone TEXT, sum INTEGER, code INTEGER)")


        c.execute(f"INSERT INTO payment_query VALUES(?, ?, ?, ?)", (message.from_user.id, phone, sum, random_code))
        conn.commit()

        result = c.execute(f"SELECT * FROM payment_query WHERE user_id = {message.chat.id}").fetchone()  # достаем данные из таблицы

        phone = result[1]
        random_code = result[3]
        sum = result[2]

        print(phone, random_code, sum)

        bot.send_message(message.chat.id, phone, random_code, sum)
    except Exception as e:
        print('ERROR')


def set_count(message):
    try:
        all_data['counts'] = message.text
        print(all_data['now_prod'])
        if all_data['now_prod'] == 'tie_fig':
            user.add_fighter(self=True, user_id=message.from_user.id, count=int(all_data['counts']))
            if shop_bd.datas['error'] == True:
                send = bot.send_message(message.from_user.id, 'Оххх, вы не так ввели запрос!')
                shop_bd.datas['error'] = False
                bot.register_next_step_handler(send, set_count)
            else:
                bot.send_message(message.from_user.id, 'Успешно добавлено  в корзину')

        elif all_data['now_prod'] == 'tie_def':
            user.add_defender(self=True, user_id=message.from_user.id, count=int(all_data['counts']))
            if shop_bd.datas['error'] == True:
                send = user.send_message(message.from_user.id, 'Оххх, вы не так ввели запрос!')
                shop_bd.datas['error'] = False
                bot.register_next_step_handler(send, set_count)
            else:
                bot.send_message(message.from_user.id, 'Успешно добавлено  в корзину')

        elif all_data['now_prod'] == 'tie_int':
            user.add_interceptor(self=True, user_id=message.from_user.id, count=int(all_data['counts']))
            print(all_data['counts'])
            if shop_bd.datas['error'] == True:
                send = bot.send_message(message.from_user.id, 'Оххх, вы не так ввели запрос!')
                shop_bd.datas['error'] = False
                bot.register_next_step_handler(send, set_count)
            else:
                bot.send_message(message.from_user.id, 'Успешно добавлено  в корзину')

        all_data['counts'] = None
        all_data['now_prod'] = None

    except Exception as er:
        shop_bd.datas['error'] = True

    if shop_bd.datas['error'] == True:
        send = bot.send_message(message.from_user.id, 'Введите пожалуйста только число:')
        shop_bd.datas['error'] = False
        bot.register_next_step_handler(send, set_count)


def delete_fromb(message):
    all_data['now_id'] = message.from_user.id
    all_data['counts'] = message.text

    if all_data['now_del'] == '1':
        user.delete_from_basket(self=True, user_id=all_data['now_id'], counts=all_data['counts'], numb=all_data['now_del'])
        if shop_bd.datas['error'] == True:
            send = bot.send_message(message.from_user.id, 'Введите пожалуйста только число, не превышающее количество,'
                                                         'уже присутствующее в Вашей корзине: ')
            shop_bd.datas['error'] = False
            print('III')
            bot.register_next_step_handler(send, delete_fromb)
            print('XXX')
            breakpoint()


    elif all_data['now_del'] == '2':
        user.delete_from_basket(self=True, user_id=all_data['now_id'], counts=all_data['counts'],
                                       numb=all_data['now_del'])
        if shop_bd.datas['error'] == True:
            send = bot.send_message(message.from_user.id, 'Введите пожалуйста только число:')
            shop_bd.datas['error'] = False
            print('III')
            bot.register_next_step_handler(send, delete_fromb)
            print('XXX')
            breakpoint()

    elif all_data['now_del'] == '3':
        shop_bd.delete_from_basket(self=True, user_id=all_data['now_id'], counts=all_data['counts'],
                                       numb=all_data['now_del'])
        if shop_bd.datas['error'] == True:
            send = bot.send_message(message.from_user.id, 'Введите пожалуйста только число:')
            shop_bd.datas['error'] = False
            print('III')
            bot.register_next_step_handler(send, delete_fromb)
            print('XXX')
            breakpoint()

    all_data['now_id'] = None
    all_data['counts'] = None
    all_data['now_del'] = None
    shop_bd.basket2 = []

def clear_bask(message):
    pass

def basket_1(message, mo):
    if mo == 1:
        user.basket(self=True, user_id=message.from_user.id)
        if shop_bd.basket['empty'] == False:
            bot.send_message(message.from_user.id, 'Ваша корзина не пуста')
            couel = len(shop_bd.basket1)
            print(couel, shop_bd.basket1)
            for x in range(0, couel):
                bot.send_message(message.from_user.id, '%s. %s * %s\n'
                                                      'Итого за %s: %s' % (
                                x + 1, product_data[shop_bd.basket1[x]]['beat_name'],
                                shop_bd.basket[shop_bd.basket1[x]],
                                product_data[shop_bd.basket1[x]]['beat_name'],
                                product_data[shop_bd.basket1[x]]['price'] * shop_bd.basket[shop_bd.basket1[x]]))
                print(shop_bd.basket1[x])
                all_data['now_price'] = product_data[shop_bd.basket1[x]]['price'] * shop_bd.basket[shop_bd.basket1[x]]

            if couel == 1:
                bot.send_message(message.from_user.id, 'Итого: %s' % shop_bd.basket['all_price'], reply_markup=delete_markup)

            elif couel == 2:
                bot.send_message(message.from_user.id, 'Итого: %s' % shop_bd.basket['all_price'], reply_markup=delete_markup1)

            elif couel == 3:
                bot.send_message(message.from_user.id, 'Итого: %s' % shop_bd.basket['all_price'], reply_markup=delete_markup2)

            # bot.send_message(message.from_user.id, 'Итого: %s' % all_data['now_price'], reply_markup=delete_markup)
            all_data['now_price'] = None
            user.basket1 = []

        elif shop_bd.basket['empty'] == True:
            bot.send_message(message.from_user.id, 'Ваша корзина пуста')

    elif mo == 2:
        pass


@bot.message_handler(commands=['start'])
def handler_start(message):
    if(not user.check_user(self=True, user_id=message.from_user.id)):
        user.add_user(self=True, user_id=message.from_user.id, order_id=all_data['last_order_id'], taken=False, delivar=False, paid=False, tie_def=0, tie_fig=0, tie_int=0, all_price=0)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('💵Каталог','📦Корзина', '☎Контакты')
        user_markup.row('Оформление заказа')
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}🤖!\nВы можете зайти в каталог и выбрать товар себе по душе', reply_markup=user_markup)
    else:
        bot.send_message(message.chat.id, 'Привет, снова вернулся за покупаками?\nМы всегда тебе рады!')
        print(2)

@bot.message_handler(content_types=['text'])
def message_tovar(message):
    if message.text == '💵Каталог':
        send = bot.send_message(message.from_user.id, '%s' % product_data['tie_fig']['desc'])
        all_data['mesid'] = send.message_id
        bot.send_photo(chat_id=message.chat.id, photo=open('images/%s.jpg' % all_data1[str(all_data1['now_id'])], 'rb'),
                      reply_markup=markup1)
    elif message.text == 'Оформление заказа':
        user.basket(self=True, user_id=message.from_user.id)
        if shop_bd.basket['empty'] == False:
            bot.send_message(message.from_user.id, 'Ваша корзина не пуста')
            couel = len(shop_bd.basket1)
            print(couel, shop_bd.basket1)
            for x in range(0, couel):
                bot.send_message(message.from_user.id, '%s. %s * %s\n'
                                                      'Итого за %s: %s' % (
                                x + 1, product_data[shop_bd.basket1[x]]['beat_name'],
                                shop_bd.basket[shop_bd.basket1[x]], product_data[shop_bd.basket1[x]]['beat_name'],
                                product_data[shop_bd.basket1[x]]['price'] * shop_bd.basket[shop_bd.basket1[x]]))
                print(shop_bd.basket1[x])
            bot.send_message(message.from_user.id, 'Итого: %s' % shop_bd.basket['all_price'])
            bot.send_message(message.from_user.id, 'Проверьте, верно ли составлен Ваш заказ', reply_markup=check_markup)

        elif shop_bd.basket['empty'] == True:
            bot.send_message(message.from_user.id, 'Эээ нет, погоди-ка. У тебя в корзине ведь ничего нет!!')
    elif message.text == '📦Корзина':
        basket_1(message=message, mo=1)
    elif message.text == 'Статус заказа':
        markup_stat = telebot.types.InlineKeyboardMarkup(row_width=3)
        but1 = telebot.types.InlineKeyboardButton(text='Оплачено', callback_data='paid')
        but2 = telebot.types.InlineKeyboardButton(text='Доставлено', callback_data='delivr')
        but3 = telebot.types.InlineKeyboardButton(text='Получено', callback_data='taken')
        markup_stat.add(but1, but2, but3)
        bot.send_message(message.chat.id, 'Какой статут заказа хотите поставить?', reply_markup=markup_stat)
    elif message.text == '☎Контакты':
        bot.send_message(message.chat.id, '===☎Контакты===\n\nГлавный разработчик\n@Spatium_Lustrator\nГлавный менеджер\n@Space_Scout_1')
    else:
        pass


@bot.callback_query_handler(func=lambda call: True)
def answer1(call):
    if call.data == 'back':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('💵Каталог','📦Корзина', '☎Контакты')
        user_markup.row('Оформление заказа')
        bot.send_message(call.message.chat.id, '✅Вы в главном меню', reply_markup=user_markup)

    elif call.data == 'right':
        bot.send_message(call.message.chat.id, 'Выберете место доставки:', reply_markup=adresses_markup)

    elif call.data == 'un_right':
        basket_1(call.message, mo=2)

    elif call.data == 'place1':
        user.set_place(self=True, place=1, user_id=call.message.chat.id)
        send = bot.message_handler(call.message.chat.id, 'Напишите ваш номер телефона\nВ формате +79998887766')
        bot.register_next_step_handler(send, oplata)

    elif call.data == 'place2':
        user.set_place(self=True, place=2, user_id=call.message.chat.id)
        send = bot.message_handler(call.message.chat.id, 'Напишите ваш номер телефона\nВ формате +79998887766')
        bot.register_next_step_handler(send, oplata)

    elif call.data == 'place3':
        user.set_place(self=True, place=3, user_id=call.message.chat.id)
        send = bot.message_handler(call.message.chat.id, 'Напишите ваш номер телефона\nВ формате +79998887766')
        bot.register_next_step_handler(send, oplata)

    elif call.data == 'delall':
        user.clear_basket(self=True, user_id=call.message.from_user.id)
        bot.send_message(call.message.chat.id, 'Ваша корзина очищена!')
        all_data['counts'] = None
        all_data['now_prod'] = None
    elif call.data == 'tie1':
        send = bot.send_message(call.message.chat.id, 'Введите кол-во необходимого товара')
        all_data['now_prod'] = 'tie_fig'
        bot.register_next_step_handler(send, set_count)
    elif call.data == 'tie2':
        send = bot.send_message(call.message.chat.id, 'Введите кол-во необходимого товара')
        all_data['now_prod'] = 'tie_def'
        bot.register_next_step_handler(send, set_count)
    elif call.data == 'tie3':
        send = bot.send_message(call.message.chat.id, 'Введите кол-во необходимого товара')
        all_data['now_prod'] = 'tie_int'
        bot.register_next_step_handler(send, set_count)
    elif call.data == 'paid':
        user.paid(self=True, user_id=call.message.from_user.id)
        all_data['now_id'] = call.message.chat.id
        bot.send_message(call.message.chat.id,'✅Теперь ваш статус - "оплачено"!')
    elif call.data == '>':
        if (all_data1['now_id'] + 1) < 4:
            all_data1['now_id'] += 1
        else:
            all_data1['now_id'] -= 2
            print('!?')

        print('!?!')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=all_data['mesid'],
                             text='%s' % product_data[all_data1[str(all_data1['now_id'])]]['desc'])
        bot.edit_message_media(
            media=types.InputMedia(type='photo', media=open('images/%s.jpg' % all_data1[str(all_data1['now_id'])], 'rb')),
            chat_id=call.message.chat.id, message_id=call.message.message_id,
            reply_markup=markup1)
    elif call.data == '<':
        if (all_data1['now_id'] - 1) > 0:
            all_data1['now_id'] -= 1
        else:
            all_data1['now_id'] += 2

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=all_data['mesid'],
                             text='%s' % product_data[all_data1[str(all_data1['now_id'])]]['desc'])
        bot.edit_message_media(
            media=types.InputMedia(type='photo', media=open('images/%s.jpg' % all_data1[str(all_data1['now_id'])], 'rb')),
            chat_id=call.message.chat.id, message_id=call.message.message_id,
            reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def otvet_na_vse(message):
    bot.send_message(message.chat.id, 'Выберете пожалуйста действие на клавиатуре🤔')

bot.polling(none_stop=True, interval=0)

