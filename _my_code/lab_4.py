# Richard Farr
# December 11th, 2020
# PDX Code Guild
# Programming 102
# Lab 4

'''
Let's write an anagram checker.

Anagram
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirtyroom.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

Convert the strings into lists (list)
Sort the letters of each word (sort)
Check if the two are equal
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
Advanced Version 1
Convert each word to lower case (lower)
Remove all the spaces from each word by replacing them with empty strings (replace)
Advanced Version 2
Make your program ignore punctuation when checking anagrams.

Advanced Version 3
Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
'''

def main():

    print(" ") # start with an empty line to clean things up
    print("This is an anagram checker. You are going to need to enter 2 words to be checked.")
    word1 = input("enter the first word: ").lower().replace(" ", "")
    # print(word1)
    word2 = input("enter the second word: ").lower().replace(" ", "")
    # print(word2)

    word1_sorted = word1
    
    word1_sorted = list(word1_sorted)
    # word1.sorted = word1_sorted.replace(" ", "")
    # print(word1_sorted)
    word1_sorted.sort()
    # word1_sorted.replace(" ", "")
    # print(word1_sorted)

    word2_sorted = word2
    
    word2_sorted = list(word2_sorted)
    # word2_sorted = word2_sorted.replace(" ", "")
    # print(word2_sorted)
    word2_sorted.sort()
    
    # print(word2_sorted)

    if word1_sorted == word2_sorted:
        print(f"{word1} and {word2} are anagrams \n")
    else:
        print(f"{word1} and {word2} are not anagrams \n")



main()