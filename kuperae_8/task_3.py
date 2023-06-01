# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


def segment(tup1, tup2):
    """
    Возвращает сумму элементов кортежей tup1 и tup2
    :param tup1: tuple
    :param tup2: tuple
    :return:
    """
    try:
        return tup1[0] + tup1[1] + tup2[0] + tup2[1]
    except Exception as e:
        return e.args[0][::-1]


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
