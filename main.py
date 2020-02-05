import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 67

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Would yah rather nicely guess a number, preferably between 1 and {}?: ".format(range))
        if not number.isdigit():
            print("Please follow my simple directions, yah should know rudeness makes me shiver with frustration!")
        else:
            number = int(number)
            count = count + 1
            print("No, not quite")
            if number > random_number:
                print("Too up in sky, that guess!")
            elif number <random_number:
                print("Too down below for my tastes.")
    print("Congrats on yer luck!")
    print("Yah got it in {} tries!".format(count))
    play_again = input("\nCould you be enticed to play again (yes or no)?")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nThanks for playing! See you later!")