input("Press ENTER To Start The Game")
print("Welcome To The Guessing Game")
high=int(input("Enter Maximum Limit Of Number I Should Think Of"))
low=int(input("Enter Minimum Limit Of Number I Should Think Of"))
print("Here You Guess a Number Between {} and {} And I Will Guess What You Gussed".format(high,low))
guesses=1

while True:
    guess=low+(high-low)//2
    print("My Guess Is {}".format(guess))
    high_low=input("Enter c if i am correct  h for me to guess higher and l for me to guess lower").casefold()

    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print("I got it yayyy")
        break
    else:
        print("Enter a valid input")
    guess=guesses+1

print("You Got Out Of Programe")