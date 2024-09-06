"""names=[]

for _ in range(3):
    names.append(input("Whats your name?"))


for name in sorted(names):
    print(f"hello,{name}")
    """
#
#saving inputs
"""
name=input("Whats your name")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()
"""
#
"""
name=input("Whats your name")

with open("names.txt","a") as file:
    file.write(f"{name}\n")

#otomatik olarak kapatmasını sağlar 
"""
#
"""
with open("names.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

"""
#

with open("names.txt","r") as file:
    for line in file:
        print("Hello,",line.rstrip())

