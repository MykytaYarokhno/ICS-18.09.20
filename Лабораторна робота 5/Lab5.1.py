import csv
import os




os.chdir("D:/ICS-18.09.20/Лабораторна робота 5")

def isFileExisting(filename):
    return os.path.isfile(filename)

def outputFileByName(filename):
    print('File' + filename)
    fd = open(filename, "r")
    
    reader = csv.reader(fd, delimiter ='\t')
    for row in reader :
        print(row)
    fd.close()

G1="Group1.txt"
G2="Group2.txt"


def readFiles():
    fd1 = open(G1, "r")
    reader = csv.reader(fd1, delimiter ="\t")
    print('First group:')
    for row in reader:
        print(row)        
    fd1.close()


    fd2 = open(G2, "r")
    reader = csv.reader(fd2, delimiter ="\t")
    print("\nSecond group:")
    for row in reader:
        print(row)
    fd2.close()

def writeFiles():
    fd1 = open(G1, "w")
    fd1.write("Nik, 87\nJohn, 43")
    fd1.close

    fd2 = open(G2, "w")
    fd2.write("Stan, 45\nKirk, 23")
    fd2.close

def addToFiles():
    fd1 = open(G1, "a")
    fd1.write("\nNik, 87\nJohn, 43")
    fd1.close()

    fd2 = open(G2, "a")
    fd2.write("\nStan, 45\nKirk, 23")
    fd2.close()

def searchFiles(query):
    if(not isFileExisting(query)):
        print("File with name" + query + "does not exist")
    else:
        outputFileByName(query)

def searchTextInFiles(filename, query):
    fd = open(filename, "r")
    reader = fd.resdlines()

    for row in reader:
        if query.lower() in row.lower():
            print(f'Found: {row}')
    fd.close()
        
def sortMarksInFile():
    filename = "Group1.txt"
    dict = {}
    fd1 = open(filename, "r+")
    reader = fd1.readlines()
    for row in reader:
        split_row_by_coma = row.split(',')
        dict[int(split_row_by_coma[1].strip())] = split_row_by_coma[0].strip()


    sorted_keys = list(dict.keys())
    for key in range(0, len(sorted_keys)):

        for j in range(0, len(sorted_keys) - key - 1):

            if sorted_keys[j] > sorted_keys[j+1]:
                sorted_keys[j], sorted_keys[j+1] = sorted_keys[j+1], sorted_keys[j]

    sorted_dict_by_key = {}
    for sorted_key in sorted_keys:
        sorted_dict_by_key[sorted_key] = dict[sorted_key]
    print(sorted_keys)
    print(sorted_dict_by_key)

    

    fd1.close()

    

    

#readFiles()    
#writeFiles()
#addToFiles()
#searchFiles(G1)
#searchTextInFiles(G1, "oli")
#sortMarksInFile(G1)
