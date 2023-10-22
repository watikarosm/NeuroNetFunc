import numpy as np
import operator as op
import itertools as it
from functools import reduce

randBits = np.random.randint(0, 2, 16)
randBits1 = np.random.randint(0, 2, 16)
enumBits = enumerate(randBits)
listBits = list(enumBits)

print("Bits: ", randBits)
print("Bits 1: ", randBits1)
print("Enum Bits: ", enumBits)
print("List Bits: ", listBits)
choseBits = [i for (i, b) in enumerate(randBits) if b]
print("Chose bits: ", choseBits)

xorBits = []
i = 1
for i in range (0, len(randBits)):
    j = i-1
    xorBits.append(op.xor(randBits[i], randBits[j]))
print("XOR Bits: ", xorBits)
reducedChoseBits = reduce(op.xor, [i for (i, b) in enumerate(choseBits) if b])
print("Reduced Chose Bits: ", reducedChoseBits)
reducedBits = reduce(op.xor, [i for (i, b) in enumerate(randBits) if b])
print("Reduced Bits: ", reducedBits)

def hummingCode(bits):
    return reduce(
        # reduce by xor
        #---> lambda x, y: x ^ y,   # without importing xor function
        # OR
        op.xor,
        # all indices of active bits
        [i for (i, b) in enumerate(bits) if b]
    )

print("Reduced Randdome Bits: ", hummingCode(randBits))

byteStr0 = bytes(b'abc')
byteStr1 = bytes(b'11110000')
byteStr2 = bytes(b'00001111')  # 15 
byteStr3 = bytes(b'01010101')  # 85 
print(byteStr0, " ", byteStr1, " ", byteStr2, " ", byteStr3)

byte0 = int('00001101', 2)  # 13
byte1 = int('11110000', 2)  # 240 
byte2 = int('00001111', 2)  # 15 
byte3 = int('01010101', 2)  # 85 

print(byte0, " ", byte1, " ", byte2, " ", byte3)
print(hummingCode(byteStr1))
print(hummingCode(byteStr2))
print(hummingCode(byteStr3))
