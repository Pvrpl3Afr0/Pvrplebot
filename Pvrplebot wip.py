#First version of Pvrple.
#pvrplebot
import random
#Main page.
prompt = input("Hi, I'm pvrplebot! Ask me A, B or C! ")

if prompt == "a" or prompt == "A":
    print("You pressed A, you will now be redirected to the info page.")
elif prompt == "b" or prompt == "B":
    print("You pressed B, you will now be redirected to the passgen page.")
elif prompt == "c" or prompt == "C":
    print("I don't do much at the moment...")
else:
    print("I said, A B or C! try again..")

#Defining stuff.


def PassgenPage(Password):
    print("Welcome to the password generator, where you will get random characters to use as a password.")
    Password = "abcdefhijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    passlen = int(input("How many characters would you like in your password?"))
    p = "".join(random.sample(Password,passlen ))
    print(p)
    return
PassgenPage(str)

while prompt == "a" or prompt == "A":
    print("This is the info page, where you can learn all about me!")
    print("I was made by Pvrpl3afr0! As of now I don't do much.")
    print("Some of my 'planned' features will include:")
    print("Generating passwords, guessing games, easy calculations, coinflipping and more!")
    print("I'll take you back to the main page now.")

else:
    while prompt == "b" or prompt == "B":
        PassgenPage(str)
