import os
import random

list1 = ['Hard', 'Easy', 'Impossible']
list2 = ['game', 'stage', 'test']
list3 = ['for you', 'for me', 'for us']

listOfStringList = [list1, list2, list3]

def randomPhrase():
    result_string = ""
    for i in range(0, 3):
        random_index = random.randrange(0, 3)
        result_string = result_string + \
            listOfStringList[i][random_index] + " "
    return result_string
print(randomPhrase())
