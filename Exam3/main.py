def hex2bin(hexString):
    return bin(int(hexString, 16))[2:]

def bin2hex(binString):
    return hex(int(binString, 2))[2:].rjust((int)(len(binString)/4),'0')

def dec2bin(decString):
    return bin((int)(decString))[2:]

def bin2dec(binString):
    h = 0;
    value = 1;
    for letter in reversed(binString):
        if letter == '1':
            h += value
        value *= 2
    return h

def hex2string(initialHex):
    finalString=""
    for i in range(0,(int)(len(initialHex)/2)):
        finalString += chr(int(initialHex[:2],16))
        initialHex=initialHex[2:]
    return finalString


def string2hex(message):
    ret = ""
    for c in message:
        ret += hex(ord(c))[2:].rjust(2,'0')
    return ret

def mod256(initialBin):
    return dec2bin(bin2dec(initialBin)%256).rjust(8,'0')

def hex_xor(initialHex1,initialHex2):
    length=max(len(initialHex1),len(initialHex2))
    finalHex1=hex2bin(initialHex1).rjust(length*4,'0')
    finalHex2=hex2bin(initialHex2).rjust(length*4,'0')
    finalXor=""
    for i in range(0,len(finalHex1)):
        finalXor+=str((int)(finalHex1[i])^(int)(finalHex2[i]))

    finalHexXor=bin2hex(finalXor)
    return finalHexXor

def swap_every_second_bit(initialByte):
    '''
    >>> swap_every_second_bit(1)
    2
    >>> swap_every_second_bit(2)
    1
    >>> swap_every_second_bit(4)
    8
    >>> swap_every_second_bit(16)
    32
    >>> bin(swap_every_second_bit(0b1010))
    '0b101'
    >>> bin(swap_every_second_bit(0b01010110))
    '0b10101001'
    '''
    if str(initialByte)[:2]=='0b':
        auxByte=initialByte[2:].rjust(8,'0') #if byte is binary I remove "0b" and extend to 8 bits
    else:
        auxByte=dec2bin(initialByte).rjust(8,'0') #if byte is decimal I convert it to binary and extend to 8 bits
    finalByte=""
    for i in range(0,4):
        aux1=auxByte[0] #I select the first two bits
        aux2=auxByte[1]
        finalByte+=str(aux2)+str(aux1) #and swap them in the final byte
        auxByte=auxByte[2:]
    return bin2dec(finalByte)
