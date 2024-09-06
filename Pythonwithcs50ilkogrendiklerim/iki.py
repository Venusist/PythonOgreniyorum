"""  x = float(input("Whats x?"))
y = float(input("Whats y?"))
z= round(x+y)
print(z)  """
#
"""
x = int(input("Whats x?"))
y = int(input("Whats y?"))

print(x + y)
"""
#
"""
x = float(input("Whats x?"))
y = float(input("Whats y?"))
z= round(x+y)

print(f"{z:,.2f}")
"""
#
def main():
    x=int(input("Whats x?"))
    print("x squared is",square(x))

def square(n):
    return n*n

main()