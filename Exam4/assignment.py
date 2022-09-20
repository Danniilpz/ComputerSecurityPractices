
#DANIEL LÓPEZ MARQUÉS

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

def encrypt_with_power_and_swap_every_second_bit(initialString,initialKey,mode):
    '''
    >>> encrypt_with_power_and_swap_every_second_bit('Hello',120,'encrypt')
    'üÚùEn'
    >>> encrypt_with_power_and_swap_every_second_bit('Hello',200,'encrypt')
    'LÚùEn'
    >>> string2hex(encrypt_with_power_and_swap_every_second_bit('Hello',250,'encrypt'))
    '7ebe8cf00f'
    >>> string2hex(encrypt_with_power_and_swap_every_second_bit(hex2string('acc5522cca'),250,'encrypt'))
    'a6eeb14e81'
    >>> string2hex(encrypt_with_power_and_swap_every_second_bit(hex2string('acc5522cca'),123,'encrypt'))
    '27d3d0fd04'
    >>> string2hex(encrypt_with_power_and_swap_every_second_bit('I love Cryptography!!!',23,'encrypt'))
    '9101bdde38ec7493f23fe119de1ad6e35155376b2373'
    >>> encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Hello',234,'encrypt'),234,'decrypt')
    'Hello'
    >>> encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Hello',2,'encrypt'),2,'decrypt')
    'Hello'
    >>> encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Hello',2,'encrypt'),62,'decrypt')
    'tello'
    >>> encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''
    auxKey = dec2bin(initialKey).rjust(8, '0') #key to binary
    auxHex = string2hex(initialString) #text to hexadecimal
    #print(auxHex)
    finalEncrypt = ""
    aux=""

    for i in range(0,(int)(len(auxHex)/2)):
        if(mode=="encrypt"):
            auxDigit = hex2bin(auxHex[:2]).rjust(8, '0')  # each character of the text

            if aux != "" and (bin2dec(auxKey) == 0 or bin2dec(auxKey) == 1):  # if it's not the first character and key is 0 or 1
                auxKey = aux  # key is the previous byte or the previous decrypted byte

            aux = auxDigit #in case of 0 or 1, the key is the previous byte

            auxDigit = dec2bin(swap_every_second_bit("0b" + str(auxDigit))) #I swap the actual byte before encrypt
            auxEncrypt = hex_xor(auxDigit, auxKey).rjust(8, '0')  # encrypt each letter with the key
            auxKey = mod256(dec2bin(bin2dec(auxKey) ** 2).rjust(8, '0'))  # update the key

            finalEncrypt += auxEncrypt
            auxHex = auxHex[2:]

        elif(mode=="decrypt"):
            auxDigit = hex2bin(auxHex[:2]).rjust(8, '0')  # each character of the text

            if aux != "" and (bin2dec(auxKey) == 0 or bin2dec(auxKey) == 1):  # if it's not the first character and key is 0 or 1
                auxKey = aux  # key is the previous byte or the previous decrypted byte

            auxEncrypt = hex_xor(auxDigit, auxKey).rjust(8, '0')  # encrypt each letter with the key
            auxEncrypt = dec2bin(swap_every_second_bit("0b" + str(auxEncrypt))).rjust(8,'0') #I swap the result byte after decrypt
            auxKey = mod256(dec2bin(bin2dec(auxKey) ** 2).rjust(8, '0'))  # update the key

            finalEncrypt += auxEncrypt
            aux = auxEncrypt #in case of 0 or 1, the key is the previous decrypted byte
            auxHex = auxHex[2:]


    finalEncrypt=hex2string(bin2hex(finalEncrypt)) #cipher text from binary to string
    return finalEncrypt