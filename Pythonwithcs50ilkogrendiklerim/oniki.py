#anlamadım çok amacı
"""
import sys

if len(sys.argv)<2:
    sys.exit("Too few arguements")
elif len(sys.argv)>2:
    sys.exit("Too many arguements")

print("Hello my name is",sys.argv[1])
"""
#

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:]:
    print("Hello,my name is",arg)
