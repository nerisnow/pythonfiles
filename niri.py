#text=input('enter your text')
#dis=input('enter displacement')

def caesar_cipher(text,dis):
    abc = ''
    sum = 0
    for charc in text:
        if charc != ' ':
            if ord(charc)>64 and ord(charc)<97:

                    x = ord(charc)
                    y = x + int(dis)
                    if (y > 96):
                        diff = y - 97
                        y = diff + 64
                        z = chr(y)
                        abc = abc + z
                    else:
                        z = chr(y)
                        abc = abc + z
            elif ord(charc)>96 and ord(charc)<123:
                    x = ord(charc)
                    y=x+int(dis)
                    if (y>122):
                        diff=y-123
                        y=diff+97
                        z=chr(y)
                        abc = abc + z
                    else:
                        z = chr(y)
                        abc = abc + z
        elif charc==' ':
            abc=abc+' '
    print (abc)

