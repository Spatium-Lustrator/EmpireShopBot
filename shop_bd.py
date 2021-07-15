import sqlite3


order_id = None
ad = {'nci': None, 'None': 0, 'np': None}
datas = {'error': False, 'paid': False}
ties = ['tie_fig', 'tie_def', 'tie_int']
basket = {'tie_fig': None, 'tie_def': None, 'tie_int': None, 'all_price': None, 'end_prise': None,'empty': False}
basket1 = []
basket2 = []


class user:

    def add_user(self, order_id, user_id, paid, delivar, taken,  tie_def, tie_int, tie_fig, all_price):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        curs.execute('INSERT or IGNORE INTO stat_order(order_id, user_id, paid, delivar, taken) VALUES(?, ?, ?, ?, ?)', (order_id, user_id, paid, delivar, taken, ))
        curs.execute('INSERT or IGNORE INTO order_basket(order_id, user_id, tie_def, tie_int, tie_fig, all_price) VALUES(?, ?, ?, ?, ?, ?)', (order_id, user_id, tie_def, tie_int, tie_fig, all_price))
        curs.execute('INSERT or IGNORE INTO User(order_id, user_id) VALUES(?, ?)', (order_id, user_id, ))
        curs.execute('INSERT or IGNORE INTO payment_query(user_id) VALUES(?)', (user_id,))
        connect.commit()
        connect.close()

    def check_user(self, user_id):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        result = curs.execute('SELECT * FROM User WHERE  user_id = ?', (user_id, )).fetchall()
        print(result)
        return result

    def delete_from_basket(self, user_id, counts, numb):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        try:
            if numb == '1':
                if basket2[0] == 'tie_fig':
                    nc = cursor.execute('SELECT `tie_fig` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        print('It`s ok')
                        cursor.execute('UPDATE `order_composition` SET `tie_fig` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 500, user_id))
                    else:
                        datas['Err'] = True
                        return AttributeError

                elif basket2[0] == 'tie_def':
                    nc = cursor.execute('SELECT `tie_de` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_de` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 600, user_id))

                elif basket2[0] == 'tie_int':
                    nc = cursor.execute('SELECT `tie_int` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_int` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 650, user_id))

            elif numb == '2':
                if basket2[1] == 'tie_fig':
                    nc = cursor.execute('SELECT `tie_fig` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_fig` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 500, user_id))

                elif basket2[1] == 'tie_def':
                    nc = cursor.execute('SELECT `tie_de` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_de` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 600, user_id))

                elif basket2[1] == 'tie_int':
                    nc = cursor.execute('SELECT `tie_int` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_int` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 650, user_id))

            elif numb == '3':
                if basket2[2] == 'tie_fig':
                    nc = cursor.execute('SELECT `tie_fig` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_fig` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 500, user_id))

                elif basket2[2] == 'tie_def':
                    nc = cursor.execute('SELECT `tie_de` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_de` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 600, user_id))

                elif basket2[2] == 'tie_int':
                    nc = cursor.execute('SELECT `tie_int` FROM `order_composition` WHERE `user_id` = ?',
                                        (user_id,)).fetchone()
                    if nc[0] >= int(counts):
                        cursor.execute('UPDATE `order_composition` SET `tie_int` = ? WHERE `user_id` = ?',
                                       (int(nc[0]) - int(counts), user_id))
                        nc = cursor.execute('SELECT `all_price` FROM `order_composition` WHERE `user_id` = ?',
                                            (user_id,)).fetchone()
                        cursor.execute('UPDATE `order_composition` SET `all_price` = ? WHERE `user_id` = ?',
                                       (nc[0] - int(counts) * 650, user_id))

        except Exception as er:
            print(er)
            datas['error'] = True

        conn.commit()
        conn.close()

    def clear_basket(self, user_id):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE `order_basket` SET `tie_fig` = 0, `tie_def` = 0, `tie_int` = 0 WHERE user_id = ?',
                       (user_id, ))
        conn.commit()
        conn.close()

    def add_defender(self, user_id, count):
        try:
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            nc = cursor.execute('SELECT `tie_def` FROM `order_basket` WHERE `user_id` = ?', (user_id, )).fetchone()
            print(nc[0])
            cursor.execute('UPDATE `order_basket` SET `tie_def` = ? WHERE `user_id` = ?', (count+nc[0], user_id))
            nc = cursor.execute('SELECT `all_price` FROM `order_basket` WHERE `user_id` = ?', (user_id, )).fetchone()
            cursor.execute('UPDATE `order_basket` SET `all_price` = ? WHERE `user_id` = ?', (count * 600 + nc[0], user_id))
            conn.commit()
            conn.close()
        except Exception as e:
            datas['error'] = True

    def add_fighter(self, user_id, count):
        try:
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            nc = cursor.execute('SELECT `tie_fig` FROM `order_basket` WHERE `user_id` = ?', (user_id, )).fetchone()
            print(nc[0])
            cursor.execute('UPDATE `order_basket` SET `tie_fig` = ? WHERE `user_id` = ?', (count+nc[0], user_id))
            nc = cursor.execute('SELECT `all_price` FROM `order_basket` WHERE `user_id` = ?', (user_id, )).fetchone()
            cursor.execute('UPDATE `order_basket` SET `all_price` = ? WHERE `user_id` = ?', (count * 500 + nc[0], user_id))
            conn.commit()
            conn.close()
        except Exception as e:
            datas['error'] = True

    def add_interceptor(self, user_id, count):
        try:
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            nc = cursor.execute('SELECT `tie_int` FROM `order_basket` WHERE `user_id` = ?', (user_id,)).fetchone()
            print(nc)
            cursor.execute('UPDATE `order_basket` SET `tie_int` = ? WHERE `user_id` = ?', (count+nc[0], user_id))
            nc = cursor.execute('SELECT `all_price` FROM `order_basket` WHERE `user_id` = ?',
                                (user_id,)).fetchone()
            cursor.execute('UPDATE `order_basket` SET `all_price` = ? WHERE `user_id` = ?',
                           (count * 650 + nc[0], user_id))

            conn.commit()
            conn.close()
        except Exception as er:
            datas['Err'] = True

    def paid(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `paid` = 1 WHERE `user_id` = ?', (user_id, ))
        a = curs.execute('SELECT ``')
        conn.commit()
        conn.close()


    def delivared(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `delivared` = 1 WHERE `user_id` = ?', (user_id, ))
        conn.commit()
        conn.close()

    def carried(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `taken` = 1 WHERE `user_id` = ?', (user_id, ))
        res = curs.execute('SELECT `taken` FROM `stat_order` WHERE `user_id` = ?', (user_id, )).fetchone()
        print(res)
        conn.commit()
        conn.close()

    def check_stat(self, taken):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        result = curs.execute('SELECT taken FROM stat_order WHERE taken = ?', (taken, )).fetchone()
        print(result)
        return result

    def basket(self, user_id):
        basket['empty'] = False
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM `order_basket` WHERE user_id = ?', (user_id,)).fetchone()
        print(result)
        for i in range(0, 3):
            if result != None:
                basket[ties[i]] = result[i+3]
                print(basket)
                print(i)
                print(ties[i])

        for i in range(0, 3):
            if basket[ties[i]] == 0:
                print('This is dict', basket[ties[i]])
                ad['None'] += 1
                print(ad['None'])
            else:
                if ties[i] not in basket1 and basket[ties[i]] > 0:
                    basket1.append(ties[i])
                    print(basket1)
                    basket2.append(ties[i])


        if ad['None'] >= 3:
            basket['empty'] = True
        ad['None'] = 0
        basket['all_price'] = result[5]

    def set_place(self, user_id, place):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE `stat_order` SET `place` = ? WHERE user_id = ?', (place, user_id))
        conn.commit()
        conn.close()
