
#TASK 2

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

def hex_xor(initialHex1,initialHex2):
    length=max(len(initialHex1),len(initialHex2))
    finalHex1=hex2bin(initialHex1).rjust(length*4,'0')
    finalHex2=hex2bin(initialHex2).rjust(length*4,'0')
    finalXor=""
    for i in range(0,len(finalHex1)):
        finalXor+=str((int)(finalHex1[i])^(int)(finalHex2[i]))

    finalHexXor=bin2hex(finalXor)
    return finalHexXor

def encrypt_xor_with_changing_key_by_prev_cipher (initialHex,initialKey,mode):
    auxKey=dec2bin(initialKey).rjust(8,'0')
    auxHex=string2hex(initialHex)
    finalEncrypt=""
    auxEncrypt=""
    for i in range(0,(int)(len(auxHex)/2)):
        if auxEncrypt=="":
            auxEncrypt=auxKey

        auxDigit=hex2bin(auxHex[:2]).rjust(8,'0')
        finalEncrypt+=hex_xor(auxDigit,auxEncrypt)
        if mode=='encrypt':
            auxEncrypt=hex_xor(auxDigit,auxEncrypt)
        elif mode=='decrypt':
            auxEncrypt=auxDigit
        auxHex=auxHex[2:]
    finalEncrypt=hex2string(bin2hex(finalEncrypt))
    return finalEncrypt

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key (initialString,keyList,mode):
    '''
    >>> key_list = [0x20, 0x44, 0x54,0x20]
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
    'A&7D$@P'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
    'A%5B#GW'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'abcdefg'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'Hellobello, it will work for a long message as well'
    '''
    auxString=initialString
    finalEncrypt=""
    auxEncrypt=""
    for i in range(0,(int)(len(initialString))):
        auxKey=keyList[i%4]
        aux=auxString[:1]
        finalEncrypt+=encrypt_xor_with_changing_key_by_prev_cipher(auxString[:1],str(auxKey),mode)
        auxString=auxString[1:]
    return finalEncrypt

key_list = [0x20, 0x44, 0x54,0x20]
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt'))
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt'))
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),key_list,'decrypt'))
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),key_list,'decrypt'))