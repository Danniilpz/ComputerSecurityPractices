
from Crypto.Cipher import AES

def decrypt_aes_ecb(bytes,key):
    '''
    >>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
    >>> decrypt_aes_ecb(bytes([215, 221, 59, 138, 96, 94, 155, 69, 52, 90, 212, 108, 49, 65, 138, 179]),key)
    b'lovecryptography'
    >>> decrypt_aes_ecb(bytes([147, 140, 44, 177, 97, 209, 42, 239, 152, 124, 241, 175, 202, 164, 183, 18]),key)
    b'!!really  love!!'
    '''
    aes = AES.new(key, AES.MODE_ECB)
    orig = aes.decrypt(bytes)
    return orig

def xor_byte_arrays(bytes1,bytes2):
    '''
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([2,3,4,5]))
    b'\\x03\\x01\\x07\\x01'
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([]))
    b'\\x01\\x02\\x03\\x04'
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([1,2]))
    b'\\x01\\x02\\x02\\x06'
    >>> xor_byte_arrays(bytes([1,2,4,8,16,32,64,128]),bytes([1,1,1,1,1,1,1,1]))
    b'\\x00\\x03\\x05\\t\\x11!A\\x81'
    '''
    auxBytes1=bytes1.decode('utf-8')
    auxBytes2=bytes2.decode('utf-8')
    finalBytes=''
    length=min(len(auxBytes1),len(auxBytes2))
    for i in range(0,length):
        aux1=ord(auxBytes1[i])
        aux2=ord(auxBytes2[i])
        aux3=aux1^aux2
        finalBytes+=chr(aux3)

    if(len(auxBytes1)>len(auxBytes2)):
        finalBytes+=auxBytes1[length:]
    else:
        finalBytes += auxBytes2[length:]

    return finalBytes.encode('utf-8')

print(xor_byte_arrays(bytes([1,2,3,4]),bytes([2,3,4,5])))