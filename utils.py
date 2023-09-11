class utils:
    def reversed(num):
        if(num < 0):
            reversed_num = abs(num)
        else:
            reversed_num = -num

        return reversed_num


    def formatter(num):
        binary = bin(num)
        octal = oct(num)

        return binary, octal
