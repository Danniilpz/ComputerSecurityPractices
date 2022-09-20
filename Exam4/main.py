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

def swap_every_second_bit(initialByte):
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

print(encrypt_with_power_and_swap_every_second_bit('Hello',123,'encrypt'))
print(encrypt_with_power_and_swap_every_second_bit(encrypt_with_power_and_swap_every_second_bit('Hello',123,'encrypt'),123,'decrypt'))
print('Hello')