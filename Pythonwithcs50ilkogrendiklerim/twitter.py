
"""
url = input ("URL: ").strip()

username=url.replace("https://twitter.com/","")
print(f"username: {username}")
"""
"""
url = input ("URL: ").strip()

username=url.removeprefix("https://twitter.com/")
print(f"username: {username}")

"""

import re

url=input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username: {username}")


