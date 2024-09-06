"""
email=input("What's your email?").strip()

if "@" in email and ". in email":
    print("Valid")
else:
    print("Invalid")

"""
#
"""
email=input("What's your email?").strip()

username,domain=email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""
#

"""
import re

email=input("What's your email?").strip()

if re.search(".+@.+",email):
    # ya da ..*@..* yapabilirdin aynısı olurdu 
    # ya da 
    #çeşitli semboler çeşitli anlama geliyo + . * {5} gibi onu araştırabilirsin

    print("Valid")
else:
    print("Invalid")

"""
#
"""
import re

email=input("What's your email?").strip()

if re.search(r".+@.+\.edu",email):
#r koymamızın sebebi backslashi\ \n gibi vs algılamasın
    print("Valid")
else:
    print("Invalid")
"""
#
"""
import re

email=input("What's your email?").strip()

if re.search(r"^.+@.+\.edu$",email):

    # ^ mathes the start of the string
    # $ matches the end of the string just before the newline at the end of the string
    
    print("Valid")
else:
    print("Invalid")
"""
#
"""
import re

email=input("What's your email?").strip()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    #any character exccept an @ sign == [^@]
    # [] set of characters
    # [^] complementing the set 

    print("Valid")
else:
    print("Invalid")
"""
import re

email=input("What's your email?").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email):
#yani bi sürü yol var 

    print("Valid")
else:
    print("Invalid")

