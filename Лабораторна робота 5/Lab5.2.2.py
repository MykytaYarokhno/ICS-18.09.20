
 
filename = 'CallOfCtulhu.txt'
 
def counting_chars_with_space():
    
    file = open(filename, 'r')
    data = file.read()
    amount = len(data)
    
    file.close()

    return amount



def counting_chars_without_spaces():

 num_chars = 0

 with open(filename, 'r') as f:
    for line in f:
        for letter in line:
            for i in letter:
                 if(i != ' ' and i != '\n'):
                    num_chars += 1

 return num_chars
print(counting_chars_with_space())
print(counting_chars_without_spaces())
