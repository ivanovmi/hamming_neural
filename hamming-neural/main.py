#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'


def selection(list21, start):
    for i in range(start, len(list21)/2):
        print list21[2*i]
    print '==========='



def code(input):
    break_word = True
    i = 0
    indexes = []
    array = list(input)
    while break_word is not False:
        array.insert(2**i-1, '0')
        indexes.append(i)
        if 2**(i+1) > len(array):
            break_word = False
        i += 1

    print indexes

    #for i in indexes:
    selection(array, 2**2-1)
    #print '=========================='
    #for i in range(0, len(array), 2):
    #    print i
    #print '=========================='
    #for i in range(1, len(array), 4):
    #    print i, i+1
    #print '=========================='
    #for i in range(3, len(array), 8):
    #    print i, i+1, i+2, i+3
    #print '=========================='

    return array, indexes
    #ham_code =
    #return ham_code

a = 'd'
b = 'D'
a = ''.join(format(ord(x), 'b') for x in a)
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
