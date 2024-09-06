def main():
    x=int(input("Whats x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

# ya da return(n%2==0) de ve sadece 1 i ele al çünkü 0a ne gerek var
main()
