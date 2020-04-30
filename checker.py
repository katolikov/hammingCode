from math import *

def funcLan(__f__):
    """
    Поиск проверочных символов
    """
    return ceil(log2(__f__ + 1 + ceil(log2(__f__ + 1))))

def invert(__bool__):
    """
    Функция инвертирования
    """
    return 0 if __bool__ == 1 else 1

def isEven(__num__):
    """
    функция проверки на четность
    """
    return 0 if __num__ % 2 == 0 else 1

def search(__index__, __mas__, __bin__):
    """
    Функция для нахождения едениц в разряде
    """
    return isEven(sum(list(__mas__[__bin__.index(i)] for i in __bin__ if i[__index__] == "1")))

def place(__pos__):
    """
    Функция для вставки и шагов
    """
    __pos__ += 1
    __step__ = funcLan(__pos__)
    __newPos__ = (__pos__+__step__) - 1
    return __newPos__

def errorGet(__error__, __code__):
    """
    Функция для проверки наличия ошибки
    """
    if __error__ == 0:
        print("Decode: ", __code__)
        exit()
    else:
        return 0
