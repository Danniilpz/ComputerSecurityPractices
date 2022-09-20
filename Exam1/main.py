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

def encrypt_with_power(initialString,initialKey):
    '''
    >>> encrypt_with_power('Hello',250)
    '²A|lo'
    >>> string2hex(encrypt_with_power('Hello',250))
    'b2417c6c6f'
    >>> string2hex(encrypt_with_power(hex2string('acc5522cca'),250))
    '56e1422cca'
    >>> string2hex(encrypt_with_power(hex2string('acc5522cca'),123))
    'd7dc23cd0b'
    >>> string2hex(encrypt_with_power('I love Cryptography!!!',23))
    '5e314d2ef7642142737871756e667360716978202020'
    >>> encrypt_with_power('I love Cryptography!!!',0)
    'I love Cryptography!!!'
    >>> encrypt_with_power('With key 0, it will not be changed!!!',0)
    'With key 0, it will not be changed!!!'
    >>> encrypt_with_power(encrypt_with_power('Hello',123),123)
    'Hello'
    >>> encrypt_with_power(encrypt_with_power('Cryptography',10),10)
    'Cryptography'
    '''
    auxKey = dec2bin(initialKey).rjust(8, '0') #key to binary
    auxHex = string2hex(initialString) #text to hexadecimal
    finalEncrypt = ""
    for i in range(0,(int)(len(auxHex)/2)):
        auxDigit=hex2bin(auxHex[:2]).rjust(8,'0') #each character of the text
        auxEncrypt=hex_xor(auxDigit,auxKey).rjust(8,'0') #encryt each letter with the key
        auxKey=mod256(dec2bin(bin2dec(auxKey)**2).rjust(8,'0')) #update the key
        finalEncrypt+=auxEncrypt
        auxHex=auxHex[2:]
    finalEncrypt=hex2string(bin2hex(finalEncrypt)) #cipher text from binary to string
    return finalEncrypt
