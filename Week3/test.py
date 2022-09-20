BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex2bin(hexString):
    return bin(int(hexString, 16))[2:]


def bin2dec(binString):
    h = 0;
    value = 1;

    for letter in reversed(binString):
        if letter == '1':
            h += value

        value *= 2

    return h

def hex2base64(hexString):
    '''
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    '''
    binaryString = ""
    finalString = ""

    for letter in hexString:
        binaryString += hex2bin(letter).zfill(4)

    if len(binaryString)%6==0:
        aux=len(binaryString)
    else:
        aux=len(binaryString)+(6-(len(binaryString)%6))
        aux2=(int)((6-(len(binaryString)%6))/2)

    binaryString = binaryString.ljust(aux, '0')


    for i in range(0, int(len(binaryString) / 6)):
        finalString += BASE64_CHARS[bin2dec(binaryString[:6])]
        binaryString = binaryString[6:]

    finalString += aux2 * '='

    return finalString