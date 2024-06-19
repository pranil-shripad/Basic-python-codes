# Vowels or not
letter = input("Enter a letter: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

if letter in vowels:
    print("{} is a vowel.".format(letter))
else:
    print("{} is not a vowel.".format(letter))