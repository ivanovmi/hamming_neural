#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

# Основываем на нечетности - если количество контролируемых бит, равных единице нечетно, инвертируем контрольный бит.
# Изначально записываем нули на места степени двойки
# +------------+-------------------+
# | variable   |   value           |
# +------------+-------------------+
# | d          | 1100100           |
# +------------+-------------------+
# |dwith_zeros | 00101000100       |
# +------------+-------------------+
# |count_1     | 11111001100       |
# +------------+-------------------+


def selection(list21, cond):
    """
    Функция для выборки контролируемых бит, и подсчета четности/нечетности для инвертирования контрольного бита
    :param list21: Массив, хранящий в себе начальное состояние до конвертации
    :param cond: Параметр, определяющий начальную позицию и шаг выборки
    :return: флаг, говорящий о необходимости конвертации. Равен True, если битов == 1 нечетное количество,
    и False, если битов == 1 четное количество
    """
    # Счетчик единиц в контролируемых битах
    counter = 0
    for i in range(cond-1, len(list21), cond*2):
        try:
            counter += sum(list21[i:i+cond])
        except IndexError:
            pass
    if counter % 2 == 1:
        flag = True
    else:
        flag = False
    print '==========='
    return flag


def code(input):
    break_word = True
    i = 0
    indexes = []
    array = map(int, list(input))
    while break_word is not False:
        array.insert(2**i-1, 0)
        indexes.append(i)
        if 2**(i+1) > len(array):
            break_word = False
        i += 1

    print indexes

    for i in indexes:
        flag = selection(array, 2**i)
        if flag:
            array[2**i-1] = 1
    print '\n=========================='

    ham_code = array
    return ham_code


def decode():
    pass


#a = 'ы'
#b = 'D'
#a = ''.join(format(ord(x), 'b') for x in a)
#print a
#print ''.join(str(i) for i in code(a))
# After running code, d = 11111001100
print chr(int('1101000110001011', 2)) #'11111001100', 2))
# Wrong d = 11011001100
#a = '11011001100'
#print map(int, list(a))

#print ''.join(format(ord(x), 'b') for x in b)

