import checker
import random

def charsToBin(chars, encoding='utf-8', errors='surrogatepass'):
    """
    Функция для преобразования текста в бит
    """
    bits = bin(int.from_bytes(chars.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def getList(__data__):
    """
    Функция для получения листа из входных данных
    """
    __list__ = list(int(i) for i in __data__)
    return __list__

def codeCreater(__list__, x):
    """
    Функция для создания кода
    """
    code = list(i for i in x)
    for j in range(len(__list__)):
        code[checker.place(j)] = __list__[j]
    return code

def getParam(__list__):
    """
    Функция для получения основных параметров
    """
    k = len(__list__)  # количество информационных разрядов
    p = checker.funcLan(k)  # количество проверочных символов
    __maxLong__ = checker.funcLan(k)  # максимальная длина бинарных индексов
    n = k + p  # общая длина закодированного сообщения
    x = "x"*n
    return k,p,__maxLong__,n,x

def getBinlist(__maxLong__, code, x, p):
    """
    Функция для получения бинарного листа
    """
    b = lambda numb: str("{0:0"+"{}".format(__maxLong__)+"b}").format(numb)
    binaraList = list(b(i) for i in range(1, len(code)+1))  # лист бинарных индексов
    newBinaraList = binaraList.copy()
    for i in range(p):
        newBinaraList[(2**i)-1] = "x"*__maxLong__  # лист бинарных индексов без индексов проверочных символов
    return newBinaraList, binaraList

def encodeMsg(code, newBinaraList, p):
    """
    Функция для получения закодированного сообщения
    """
    checkSymbols = list(checker.search(i, code, newBinaraList) for i in range(p))
    checkSymbols.reverse()  # лист проверочных символов
    for i in range(p):
        code[(2**i)-1] = checkSymbols[i]   # закодированное сообщение
    return code

def errorBit(__list__, code, binaraList, p):
    """
    Функция для вставки и получения ошибки
    """
    #error = int(input("Error count: "))
    error = random.randrange(5)
    checker.errorGet(error, __list__)
    errorMsg = code.copy()
    errorMsg[error-1] = checker.invert(code[error-1])

    print("\nError message: ", errorMsg) # сообщение с ошибкой

    syndromList = list(str(checker.search(i, errorMsg, binaraList)) for i in range(p))
    syndrom = "".join(syndromList)  # синдром
    #print("syndrom: ", syndrom)

    ind = binaraList.index(syndrom) + 1  # номер индекса в котором произошла ошибка

    print("\nError in position: ", ind) # номер индекса в котором произошла ошибка

    fixedCode = errorMsg.copy()
    fixedCode[ind-1] = checker.invert(errorMsg[ind-1])   # исправленное сообщение
    #print("fixed  message: ", fixedCode)
    return fixedCode

def printDecodeMsg(fixedCode, p):
    """
    Вывод на экран декодированного сообщения
    """
    for j in list(i for i in range(p))[::-1]:
        del fixedCode[(2**j)-1]
    print("\nDecode: ", fixedCode)
