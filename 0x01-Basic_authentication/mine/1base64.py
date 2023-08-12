#!/usr/bin/env python3
import base64

encoded = base64.b64encode(b'data to be encoded')
print("encoded:",encoded)
# b'ZGF0YSB0byBiZSBlbmNvZGVk'
data = base64.b64decode(encoded)
print("data:",data)
# b'data to be encoded'
