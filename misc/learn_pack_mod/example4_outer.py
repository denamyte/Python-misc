import os
import sys


print(os.path.dirname(__file__))
fpath = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(fpath)
print(sys.path)

import length
txt = "Hello World!"
res_len = length.get_length(txt)
print("The length of the string is: ", res_len)
