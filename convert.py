def convertToNepaliChar(number):
    temp= ""
    while number!=0:
        last_digit=number%10
        number=number//10
        nep_ascii=last_digit+2406
        temp= chr(nep_ascii)+temp
    return temp

print(convertToNepaliChar(1996))
