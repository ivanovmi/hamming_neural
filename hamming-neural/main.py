#!/usr/bin/env python
# -- coding: utf-8 --

import itertools

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


def selection_for_code(list21, cond):
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

    return flag


def code(input):
    """
    Функция для получения кода Хэмминга из исходной последовательности 0 и 1
    :param input: Массив, последовательность 0 и 1 (одна буква)
    :return: Код Хэмминга, основаный на нечетности контролируемых бит
    """
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

    for i in indexes:
        flag = selection_for_code(array, 2**i)
        if flag:
            array[2**i-1] = 1

    ham_code = array
    return ham_code


def selection_for_decode(list21, cond):
    appendix = []
    for i in range(cond-1, len(list21), cond*2):
        try:
            appendix.append(list21[i:i+cond])
        except IndexError:
            pass
    return appendix


def recover(indexes, array):
    for i in reversed(indexes):
        del array[i]
    return array

# Нужна проверка, является ли это число ошибочным

def decode(input):
    i = 0

    array = list(input)
    indexes = []
    while 2**i < len(input):
        indexes.append(2**i-1)
        i += 1

    recovered_array = code(recover(indexes, array))
    summary = 1
    for i in indexes:
        if input[i] != recovered_array[i]:
            summary += i

    if summary != 0:
        if recovered_array[summary] == 0:
            recovered_array[summary] = 1
        else:
            recovered_array[summary] = 0

    recovered_array = code(recover(indexes, recovered_array))

    decoded_from_ham = recovered_array
    return decoded_from_ham


#a = 'd'
#a = ''.join(format(ord(x), 'b') for x in a)
#print a
#print code(a)#''.join(str(i) for i in code(a))
# After running code, d = 11111001100
#print chr(int('11111001100', 2))
# Wrong d = 11011001100
a = '11011001100'
#print a
print decode(map(int, list(a)))

#print ''.join(format(ord(x), 'b') for x in b)

