"""x= int(input("Whats x?"))
y= int(input("Whats y?"))

if x<y :
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x is equal to y")
"""
#
"""
x= int(input("Whats x?"))
y= int(input("Whats y?"))
#ya da =! kullan direkt ora hiç gerek olmadan
if x<y or x>y:
    print("x is not equal to y")
else:
print("x is equal to y")
    """
#
score = int(input("Score:"))
if 90 <= score <= 100:
    print("Grade:A")
elif score >= 80 and score < 90:
    print("Grade:B")
elif score >=70 and score <80:
    print("Grade:C")
else:
    print("Grade is F")