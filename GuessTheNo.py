import random 
cc=random.randint(1,100)
print("The game begins !!\n Guess the computer choice of number between 1 to 100\nYou have 6 guesses") 
if cc%2==0:
    print("Hint: The number is even")
else:
    print("Hint: The number is odd")
i=1
while i<7:
 user=int(input("The number : "))
 if i==6:
    print("Oops!! Game over ")
    break
 elif user>cc:
    print("The number is too high\n Try again!")
    print("You have",6-i,"guesses left")
    i+=1
 elif cc>user :
    print("Oops! The number is too low\n Try again!")
    print("You have",6-i,"guesses left")
    i+=1
 else :
    print("Hurray !! The guess is correct")
    break   