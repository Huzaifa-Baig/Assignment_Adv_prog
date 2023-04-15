import random
number = random.randint(1, 100)

while True:
    number = int(input("pick a number between 1 and 100: "))
    guess = 0
    if guess < number:
        print("This number is too low,try again")
    elif guess > number:
        print("This number is higher than required, try again ")
    else:
        print("well done, you have won an electric car!")

