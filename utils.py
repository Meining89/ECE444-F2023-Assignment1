
class utils:
    def reversed(num):
        
        if(type(num) == int ):

            if(num < 0):
                num = abs(num)
                reversed_num = - int(str(num)[::-1])
            else:
                reversed_num = int(str(num)[::-1])

            return reversed_num

        else: false = 'Input is not a int number' 
        return false
        
    


    def formatter(num):
        if(type(num) == int):

            binary = bin(num)
            octal = oct(num)

            return binary, octal
        else: false = 'Input is not a int number'
        return false

'''
utils.reversed(1.2)
'''
#print(utils.reversed(17))
