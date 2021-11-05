import random
a=random.randint(1,100)
while True:
    guess = int(input("Please guess: "))
    if guess>a:
        print("decrease your number")
    elif guess<a:
        print("increase your number")
    else:
        print("CONGRATULATIONS!!!")
        break
