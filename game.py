import random
answer=random.randint(1,10)
print("Welcome to the guessing game ")
print("Enter Your First Guess \t \t \t \t \t \t \t \t Press 0 to Quit ")
a=int(input())
c=2
print(answer) #TODO:Remove after testing



if a==answer:
     print("Wow You Got It IN First Attempt")
while answer != a and a!=0:
    print("Sorry, You Are Wrong ")
    print("No Problem Here Is Your Next Attempt with a HINT")
    if a<answer:
        print("HINT:GUESS HIGHER than {}".format(a))
    if a>answer:
        print("HINT: GUESS LOWER than {}".format(a))
    a=int(input("Enter Your Attempt Number {}=".format(c)))
    c+=1
if a==0:
    print("You Quit The Game")
print("Thank You For Participating")