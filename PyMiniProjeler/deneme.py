import time

expires_in = 5 #in seconds    

start = time.time()
test = input("Hey there.\n") #\n is a newline character
end = time.time()

if end - start > expires_in:
    print("Nah your time has expired I'm out anyways.")
elif test == "Hey" or test == "Hi":
    print("Hey there dude.")
elif test == "Go away" or test == "Bye":
    print("Cya dude.")