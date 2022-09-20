
def hex2bin(hexString):
    return bin(int(hexString, 16))[2:]

def bin2hex(binString):
    return hex(int(binString, 2))[2:]

def bin2dec(binString):
    h = 0;
    value = 1;

    for letter in reversed(binString):
        if letter == '1':
            h += value

        value *= 2

    return h

def hex2string(initialHex):
    '''
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    '''
    finalString=""
    for i in range(0,(int)(len(initialHex)/2)):
        finalString += chr(int(initialHex[:2],16))
        initialHex=initialHex[2:]
    return finalString


def string2hex(initialString):
    '''
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    '''
    finalHex=""
    for i in range(0,len(initialString)):
        auxDec=ord(initialString[:1])
        auxBin=bin(auxDec)
        auxHex=hex(int(auxBin,2))[2:]
        finalHex += auxHex
        initialString=initialString[1:]
    return finalHex

def hex_xor(initialHex1,initialHex2):
    '''
    >>> hex_xor('aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    '''
    length=max(len(initialHex1),len(initialHex2))
    finalHex1=hex2bin(initialHex1).rjust(length*4,'0')
    finalHex2=hex2bin(initialHex2).rjust(length*4,'0')
    finalXor=""
    for i in range(0,len(finalHex1)):
        finalXor+=str((int)(finalHex1[i])^(int)(finalHex2[i]))

    finalHexXor=bin2hex(finalXor)
    return finalHexXor


def encrypt_single_byte_xor (initialHex,initialKey):
    '''
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    '''
    auxKey=hex2bin(initialKey).rjust(8,'0')
    auxHex=initialHex
    finalEncrypt=""

    for i in range(0,(int)(len(initialHex)/2)):
        auxDigit=hex2bin(auxHex[:2]).rjust(8,'0')
        finalEncrypt+=hex_xor(auxDigit,auxKey).rjust(8,'0')
        auxHex=auxHex[2:]
    finalEncrypt=bin2hex(finalEncrypt)
    return finalEncrypt

print(string2hex('hello'))
aux=encrypt_single_byte_xor(string2hex('hello'),'aa')
print(aux)
print(hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa')))