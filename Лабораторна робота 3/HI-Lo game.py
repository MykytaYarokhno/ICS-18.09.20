import random

guesses = 1
num = random.randint(1, 100)
print("It's a Hi-Lo game.")
print(" ")
player_num = int(input("Enter a number between 1-100: "))
while player_num != num:
    if player_num > num:
            print("Too high.")
    else:
        print("Too low.")
    player_num = int(input("Enter a number between 1-100: "))
    guesses += 1
else:
    print("Well done!")
    print("It took you %i guesses."  % guesses)
