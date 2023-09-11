import numpy

class utils:
    def reversed(num):
        
        if(type(num) == int):

            if(num < 0):
                num = abs(num)
                reversed_num = - int(str(num)[::-1])
            else:
                reversed_num = int(str(num)[::-1])

            return reversed_num

        else: print("Input is not a int number")


    def formatter(num):
        if(num.isnumeric() == True):

            binary = bin(num)
            octal = oct(num)

            return binary, octal
        else: print("Input is not a int number")
