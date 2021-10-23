# !!! Only with the environment variable $PYTHONPATH set to contain the current directory:
# > echo $PYTHONPATH
# :/home/denamyte/projects/study/misc/python-misc/misc/learn_pack_mod/utils

# import os
# import sys


# print(os.path.dirname(__file__))
# fpath = os.path.join(os.path.dirname(__file__), 'utils')
# sys.path.append(fpath)
# print(sys.path)

import length
txt = "Hello World!"
res_len = length.get_length(txt)
print("The length of the string is: ", res_len)
