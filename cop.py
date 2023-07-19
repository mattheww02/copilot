# for loop from 1 to 10 which prints the square of each number
for i in range(1, 11):
    print(i, i**2)  # print the number and its square

# program taking input from user and printing fibonacci series of that length
n = int(input("Enter the length of fibonacci series: "))
a = 0
b = 1
print(a, b, end=" ")
for i in range(2, n):
    c = a+b
    print(c, end=" ")
    a = b
    b = c
print()

# dictionary program that takes word as input and prints its meaning
d = {"abandon": "cease to support or look after",
        "abate": "become less intense or widespread",   
        "aberration": "a departure from what is normal, usual, or expected, typically one that is unwelcome",
        "abhor": "regard with disgust and hatred",
        "abide": "accept or act in accordance with (a rule, decision, or recommendation)",
        "abject": "experienced or present to the maximum degree",
        "abjure": "solemnly renounce (a belief, cause, or claim)",
        "abnegation": "the action of renouncing or rejecting something",
        "abominate": "detest; loathe",
        "abridge": "shorten (a book, movie, speech, or other text) without losing the sense",
        "abrogate": "repeal or do away with (a law, right, or formal agreement)",
        "abscond": "leave hurriedly and secretly, typically to avoid detection of or arrest for an unlawful action such as theft"}
# uses d to print meaning of word from user input
word = input("Enter the word: ")
print(d[word])

# regex string accepting "zebra", "koala" or any string beginning with "abab"
import re
s = input("Enter the string: ")
if re.search(r"^(zebra|koala|abab)", s):
    print("Match found")
else:
    print("Match not found")

# regex string accepting accepting any UK landline number
s = input("Enter the string: ")
if re.search(r"^(01|02|03|07|08)[0-9]{9}", s):
    print("Match found")
else:
    print("Match not found")

# regex string accepting any UK car registration number
s = input("Enter the string: ")
if re.search(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}", s):
    print("Match found")
else:
    print("Match not found")

# regex string accepting any UK car registration number for a car that was made in 2005
s = input("Enter the string: ")
if re.search(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}2005", s):
    print("Match found")
else:
    print("Match not found")
# that didn't work can you try again please
# the previous code snippet
s = input("Enter the string: ")
if re.search(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}2005", s):
    print("Match found")
else:
    print("Match not found")
# a reformatted version of the previous code snippet using switch case
s = input("Enter the string: ")
switcher = {
    1: "Match found",
    2: "Match not found"
}
if re.search(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}2005", s):
    print(switcher.get(1))
else:
    print(switcher.get(2))
# the previous code snippet but using select case
s = input("Enter the string: ")
select case s
    case re.search(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}2005", s):
        print("Match found")
    case else:
        print("Match not found")