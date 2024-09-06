"""
def main():
    x=get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x=int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    
main()
"""
#ya da 

def main():
    x=get_int()
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
            print("x is not an integer") 
            # or you can just write pass print yerine ve loopda kalmasını sağla hiç bi şey demeden

       
main()
