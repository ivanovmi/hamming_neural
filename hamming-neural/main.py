#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'


def code(input):
    break_word = True
    i = 0
    indexes = []
    array = list(''.join(format(ord(x), 'b') for x in input))
    while break_word is not False:
        array.insert(2**i-1,'0')
        indexes.append(i)
        if 2**(i+1) > len(array):
            break_word = False
        i += 1
    return array, indexes
    #ham_code =
    #return ham_code

a = 'd'
b = 'D'

print ''.join(code(a)[0])
#print ''.join(format(ord(x), 'b') for x in b)

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
