"""
import re
name=input("Whats your name?").strip()

matches= re.search(r"^(.+), (.+)$", name)
if matches:
    last, first=matches.groups()
    name= f"{first} {last}"
print(f"hello, {name}")
"""
#
"""
import re
name=input("Whats your name?").strip()

matches= re.search(r"^(.+), (.+)$", name)
if matches:
    last=matches.group(1)
    first=matches.group(2)
    name= matches.group(2) + " " + matches.group(1)


print(f"hello, {name}")
"""

import re
name=input("Whats your name?").strip()

if matches := re.search(r"^(.+), (.+)$", name):

    name=matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
