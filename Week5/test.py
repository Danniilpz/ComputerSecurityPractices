
#TASK 1

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


def string2hex(initialString):
    finalHex=""
    for i in range(0,len(initialString)):
        auxDec=ord(initialString[:1])
        auxBin=bin(auxDec)
        auxHex=hex(int(auxBin,2))[2:]
        finalHex += auxHex
        initialString=initialString[1:]
    return finalHex

def bin_add(initialBin1,initialBin2):
    finalBin1=initialBin1
    finalBin2=initialBin2
    finalAdd=""
    carry=0
    i=7
    while i>=0:
        aux=str((int)(finalBin1[i])+(int)(finalBin2[i])+carry)
        if aux=='0':
            carry=0
        elif aux=='1':
            carry=0
        elif aux=='2':
            aux='0'
            carry=1
        elif aux=='3':
            aux='1'
            carry=1
        finalAdd=aux+finalAdd
        i-=1
    if carry==1:
        finalAdd='1'+finalAdd
    return finalAdd

def mod256(initialBin):
    if len(initialBin)>8:
        initialBin=initialBin[len(initialBin)-8:]
    return initialBin

def encrypt_by_add_mod (initialHex,initialKey):
    '''
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    '''
    auxKey=dec2bin(initialKey).rjust(8,'0')
    auxHex=string2hex(initialHex)
    finalEncrypt=""

    for i in range(0,(int)(len(auxHex)/2)):
        auxDigit=hex2bin(auxHex[:2]).rjust(8,'0')
        auxEncrypt=bin_add(auxDigit,auxKey).rjust(8,'0')
        finalEncrypt+=mod256(auxEncrypt)
        auxHex=auxHex[2:]
    finalEncrypt=hex2string(bin2hex(finalEncrypt))
    return finalEncrypt
