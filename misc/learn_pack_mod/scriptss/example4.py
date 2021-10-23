import os
import sys

print()
print(os.path.dirname(__file__), os.pardir, os.path.join(
                  os.path.dirname(__file__),
                  os.pardir), sep='\n')
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
print(PROJECT_ROOT)

sys.path.append(PROJECT_ROOT)

import utils2
print(utils2.get_length("Hello"))
