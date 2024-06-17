import os
import sys
import urllib.request
import random
# import a module for internet access
from urllib import request


# ---------------------------------------------------------------------------------------------------------------------

def reverse_name1():

    # input a string and convert it to a list and each charecter is one item of this list
    # masoud sakkaki
    name = list(input(">>"))

    # reverse the item of list
    name.reverse()

    # ['i', 'k', 'a', 'k', 'k', 'a', 's', ' ', 'd', 'u', 'o', 's', 'a', 'm']
    print(name)

    # ikakkas duosam
    name_r = "".join(name)
    print(name_r, "-----")

# ---------------------------------------------------------------------------------------------------------------------

def reverse_name2():

    name = input("your name\n")
    print(name[::-1])


# ---------------------------------------------------------------------------------------------------------------------


# a function to make a table from a to b and in c columns
def table(a, b, c):
    for s in range(a, b):
        print(s, end="\t")
        if s % c is 0:
            print("")

# ---------------------------------------------------------------------------------------------------------------------


# a function to take any number of variables and return the sum
def nasser(*variables):
    total = 0
    for s in variables:
        total += s
    return total


# ---------------------------------------------------------------------------------------------------------------------

# make a function to dl images
def download_web_image(url):
    # make a random number
    name = random.randrange(1, 1000)
    # make a name for the file
    fullname = str(name) + ".jpg"
    # call a function (urlretrieve) to download an image file
    # first url and then name to save it
    urllib.request.urlretrieve(url, fullname)

# ---------------------------------------------------------------------------------------------------------------------


# generate a random file
def write_random_to_file(esm, amount, number, groups):
    random_file = random.randrange(1, esm)
    fw = open(str(random_file) + ".txt", "w")
    for s in range(1, amount):
        fw.write(str(random.randrange(1, number)) + "\t")
        if s % groups is 0:
            fw.write("\n")
    fw.close()

# ---------------------------------------------------------------------------------------------------------------------


# generate some text files with random number
def write_random_to_files(a, b, c, d, e):
    for s in range(1, a):
        write_random_to_file(b, c, d, e)


# ---------------------------------------------------------------------------------------------------------------------


# print all prime numbers from 2 to the last number and Also put all data in a text file
def new_prime(last=3000, column=15):

    fw = open("prime_file2.txt", "w")
    fw.write("The Prime numbers from 2 to " + str(last)+"\n\n")
    counter1 = 0
    counter2 = 0
    for first in range(2, last):
        prime = True
        for second in range(2, first):
            if first % second == 0:
                prime = False
        if prime:
            counter2 += 1
            print(first, end="\t\t")
            fw.write(str(first) + "\t")
            counter1 += 1
            if counter1 % column is 0:
                fw.write("\n")
                print("")
    fw.write("\n\n")
    fw.write("The number of prime numbers are " + str(counter2))
    print("\n")
    print(counter2)

# ---------------------------------------------------------------------------------------------------------------------


# a file for coding
def code(original_file_name, coded_file_name):
    fr = open(original_file_name, "r")
    reading_1 = fr.read()
    fwx = open(coded_file_name, "w")
    for line in reading_1:
        if line == "a":
            fwx.write("b")
        elif line == "b":
            fwx.write("c")
        elif line == "c":
            fwx.write("d")
        elif line == "d":
            fwx.write("e")
        elif line == "e":
            fwx.write("f")
        elif line == "f":
            fwx.write("a")
        else:
            fwx.write(line)
    fwx.close()

# ---------------------------------------------------------------------------------------------------------------------


# a file for decoding
def decode(coded_file_name, decoded_file_name):
    fr = open(coded_file_name, "r")
    khundan = fr.read()
    fwx = open(decoded_file_name, "w")
    for line in khundan:
        if line == "b":
            fwx.write("a")
        elif line == "c":
            fwx.write("b")
        elif line == "d":
            fwx.write("c")
        elif line == "e":
            fwx.write("d")
        elif line == "f":
            fwx.write("e")
        elif line == "a":
            fwx.write("f")
        else:
            fwx.write(line)
    fwx.close()

# ---------------------------------------------------------------------------------------------------------------------


# a file for coding
def code_new(original_file_name, coded_file_name):

    # dictionary code
    dic_code = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "j", "j": "k",
                "k": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u",
                "u": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": " ", " ": "\n", "\n": "a"}

    # open original file for reading
    fr = open(original_file_name, "r")

    # read file and put into variable
    reading = fr.read()

    # create a new file to write
    fwx = open(coded_file_name, "w")

    # make a loop and put every single letter of reading variable into a letter variable
    for letter in reading:

        # check whether letter in dic_code
        if letter in dic_code:

            # if the letter in dictionary-key write the value of applicable dictionary-key
            fwx.write(dic_code[letter])
        # for other character write the same ones
        else:
            fwx.write(letter)
    fwx.close()

# ---------------------------------------------------------------------------------------------------------------------


# a file for decoding
def decode_new(coded_file_name, decoded_file_name):
    dic_code = {"b": "a", "c": "b", "d": "c", "e": "d", "f": "e", "g": "f", "h": "g", "i": "h", "j": "i", "k": "j",
                "l": "k", "m": "l", "n": "m", "o": "n", "p": "o", "q": "p", "r": "q", "s": "r", "t": "s", "u": "t",
                "v": "u", "w": "v", "x": "w", "y": "x", "z": "y", " ": "z", "\n": " ", "a": "\n"}
    fr = open(coded_file_name, "r")
    reading = fr.read()
    fwx = open(decoded_file_name, "w")
    for letter in reading:
        if letter in dic_code:
            fwx.write(dic_code[letter])
        else:
            fwx.write(letter)
    fwx.close()
