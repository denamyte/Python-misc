import os
import sys


fpath = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(fpath)

import length
import upper
import lower

txt = "Hello World!"

res_len = length.get_length(txt)
print("The length of the string is: ", res_len)

res_up = upper.to_upper(txt)
print("Uppercase txt: ", res_up)

res_low = lower.to_lower(txt)
print("Uppercase txt: ", res_low)
