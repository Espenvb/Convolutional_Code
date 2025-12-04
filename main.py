from Encoder_7_5 import Conv_7_5_enc
from Decoder_7_5 import Conv_7_5_dec
import numpy as np

def sum_mod4(a, b):
    return (a + b)%4

bitstream = np.array([1, 0, 1, 0, 1, 1, 0, 0])

encoder = Conv_7_5_enc()
decoder = Conv_7_5_dec(10, 4)

code = encoder.encode_symbol(bitstream, len(bitstream))

print(code) 
e = np.array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0])
r = sum_mod4(code, e)

output, values = decoder.decode_symbol(r)
print(output)
print(values)
print("Equal Output:", values==bitstream)

