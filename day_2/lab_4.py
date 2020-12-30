# Richard Farr
# PDX Code Guild 
# Day 2 - Lab 4
# 12/29/2020

# Anagram Checker

'''
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirtyroom.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

Convert the strings into lists (list)
Sort the letters of each word (sort)
Check if the two are equal
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
'''

# 1. Get input from user
word1 = input("enter the first word: ")
word2 = input("enter the second word: ")

# 2. Convert the strings into lists (list) & sort

word1_l = list(word1)
word1_l.sort()
print(word1_l)

word2_l = list(word2)
word2_l.sort()
print(word2_l)

# 3. check to see if each word is equal & print the results
if word1_l == word2_l:
    print(f'{word1} and {word2} are anagrams')
else:
    print("Those 2 words are not annagrams")





'''
Advanced Version 1
Convert each word to lower case (lower)
Remove all the spaces from each word by replacing them with empty strings (replace)


Advanced Version 2
Make your program ignore punctuation when checking anagrams.

Advanced Version 3
Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
'''