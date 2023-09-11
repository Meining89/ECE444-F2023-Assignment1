import numpy

class utils:
    def reversed(num):
        
        if(num.isnumeric() == True ):

            if(num < 0):
                reversed_num = abs(num)
            else:
                reversed_num = -num

            return reversed_num

        else: print("Input is not a int number")


    def formatter(num):
        if(num.isnumeric() == True):

            binary = bin(num)
            octal = oct(num)

            return binary, octal
        else: print("Input is not a int number")

