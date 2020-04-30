import checker
import hammingCode
from sys import argv

if __name__ == '__main__':
    if len (argv) == 2: #Проверяем длинну внешних аргументов
    
        __data__ = hammingCode.charsToBin(argv[1])

        __list__ = hammingCode.getList(__data__)
        print("data in  list: ", __list__)

        k,p,__maxLong__,n,x = hammingCode.getParam(__list__)

        code = hammingCode.codeCreater(__list__,x)
        newBinaraList, binaraList = hammingCode.getBinlist(__maxLong__,code,x,p)

        encodeCode = hammingCode.encodeMsg(code, newBinaraList, p)
        print("Encode: ", encodeCode)

        decodeCode = hammingCode.errorBit(__list__, code, binaraList, p)

        hammingCode.printDecodeMsg(decodeCode, p)
