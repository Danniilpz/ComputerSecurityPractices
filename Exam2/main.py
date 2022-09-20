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
    #print(str(bin2dec(initialBin))+" "+str(bin2dec(initialBin)%256))
    #print(dec2bin(bin2dec(initialBin)%256).rjust(8,'0'))
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

def encrypt_with_power2(initialString,initialKey,mode):
    '''
    >>> encrypt_with_power2('Hello',253,'encrypt')
    'µl=Í.'
    >>> encrypt_with_power2('Hello2',131,'encrypt')
    'Ël=Í.³'
    >>> string2hex(encrypt_with_power2('Hello',250,'encrypt'))
    'b2417c00ff'
    >>> string2hex(encrypt_with_power2(hex2string('acc5522cca'),250,'encrypt'))
    '56e1427e8e'
    >>> string2hex(encrypt_with_power2(hex2string('acc5522cca'),123,'encrypt'))
    'd7dc23cd0b'
    >>> string2hex(encrypt_with_power2('I love Cryptography!!!',23,'encrypt'))
    '5e314d2ef713445331f021d52ee6151091a9f8581040'
    >>> encrypt_with_power2('I am',0,'encrypt')
    'Ii°Ì'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',234,'encrypt'),234,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',2,'encrypt'),2,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',2,'encrypt'),62,'decrypt')
    'tello'
    >>> encrypt_with_power2(encrypt_with_power2('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''
    auxKey = dec2bin(initialKey).rjust(8, '0') #key to binary
    auxHex = string2hex(initialString) #text to hexadecimal
    finalEncrypt = ""
    aux=""
    for i in range(0,(int)(len(auxHex)/2)):
        if mode=="encrypt":
            auxDigit = hex2bin(auxHex[:2]).rjust(8, '0')  # each character of the text

            if aux != "" and (bin2dec(auxKey) == 0 or bin2dec(auxKey) == 1):  # if it's not the first character and key is 0 or 1
                auxKey = aux  # key is the previous byte or the previous decrypted byte

            auxEncrypt = hex_xor(auxDigit, auxKey).rjust(8, '0')  # encryt each letter with the key
            auxKey = mod256(dec2bin(bin2dec(auxKey) ** 2).rjust(8, '0'))  # update the key
            finalEncrypt += auxEncrypt
            aux = auxDigit #the key is the previous byte
            auxHex = auxHex[2:]

        elif mode=="decrypt":
            auxDigit = hex2bin(auxHex[:2]).rjust(8, '0')  # each character of the text
            if aux != "" and (
                    bin2dec(auxKey) == 0 or bin2dec(auxKey) == 1):  # if it's not the first character and key is 0 or 1
                auxKey = aux  # key is the previous byte or the previous decrypted byte
            auxEncrypt = hex_xor(auxDigit, auxKey).rjust(8, '0')  # encryt each letter with the key
            auxKey = mod256(dec2bin(bin2dec(auxKey) ** 2).rjust(8, '0'))  # update the key
            finalEncrypt += auxEncrypt
            aux = auxEncrypt #the previous decrypted byte
            auxHex = auxHex[2:]

    finalEncrypt=hex2string(bin2hex(finalEncrypt)) #cipher text from binary to string
    return finalEncrypt

print(encrypt_with_power2('Hello',250,'encrypt'))