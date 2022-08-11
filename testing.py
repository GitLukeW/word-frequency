
# file = open('simple-test-file.txt', 'r')
# read = file.readlines()
# # modified = []


# def strip_punctuation(line):
#     for character in read.punctuation:
#         line = line.replace(character, "")
#         return line


# print(modified)

# for line in read:
#     modified.append(line.strip())

# ************************************

# import string


# def strip_punctuations(line):
#     for character in string.punctuation:
#         line = line.replace(character, "")
#         return line


# filepath = "simple-test-file.txt"
# word_count = {}


# with open(filepath, 'r') as file:
#     for line in file:
#         line = strip_punctuations(line)
#         words = line.split()

#         for word in words:
#             word = word.lower()
#             if word not in word_count:
#                 word_count[word] = 0
#             word_count[word] += 1

# list(word_count.keys())
# print(word_count)

# word_list = list(word_count.keys())
# for word in word_list:
#     print('{0:15}{1:d}'.format(word, word_count[word]))


# filepath = "simple-test-file.txt"
# with open(filepath, 'r') as file:
#     for words in filepath.split():
#         print(file)

# file = open('simple-test-file.txt', 'r')
# words = file.readlines()
# print(words)

# for word in readlines.split():
#     print(word)


# filepath = open("simple-test-file.txt", "r")
# for line in filepath:
#     words = line.split(" ")
#     print(filepath)

# ******************************************
# import re

# # dictionary = dict()

# filepath = open("simple-test-file.txt", "r")
# for line in filepath:
#     line = line.strip()
#     print(line)

# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# for words in line:
#     if words in punctuations:
#         line = line.replace(words, "")
#         print(line)

# words = re.sub(r'[^\w\s]', '', line)

# print(words)

# words = words.lower()
# print(words)

# for words in words:
#     if words in dictionary:
#         dictionary[words] = dictionary[words] + 1
#     else:
#         dictionary[words] = 1

#         print(words)


# def count(words):
#     # if there exists a key as "elements" then simply
#     # increase its value.
#     if words in dictionary:
#         dictionary[words] += 1

#     # if the dictionary does not have the key as "elements"
#     # then create a key "elements" and assign its value to 1.
#     else:
#         dictionary.update({words: 1})


# # Declare a dictionary
# dictionary = {}

# # split all the word of the string.
# lst = line.split()

# # take each word from lst and pass it to the method count.
# for words in lst:
#     count(words)

# # print the keys and its corresponding values.
# for allKeys in dictionary:
#     print("Frequency of ", allKeys, end=" ")
#     print(":", end=" ")
#     print(dictionary[allKeys], end=" ")
#     print()

# *****************************************************
# def freq(str):

#     # break the string into list of words
#     str_list = str.split()

#     # gives set of unique words
#     unique_words = set(str_list)

#     for words in unique_words:
#         print('Frequency of ', words, 'is :', str_list.count(words))


# # driver code
# if __name__ == "__main__":

#     str = open("simple-test-file.txt", "r")

#     # calling the freq function
#     freq(str)
# import string

# file = open('simple-test-file.txt', 'r')
# print(file)


# def freq(str):

#     # break the string into list of words
#     str_list = str.split()

#     # gives set of unique words
#     unique_words = set(str_list)

#     for words in unique_words:
#         print('Frequency of ', words, 'is :', str_list.count(words))


# # driver code
# if __name__ == "__main__":

#     str = file

#     # calling the freq function
#     freq(str)

# import string

# with open("simple-test-file.txt", 'r') as file:
#     text_string = file.read().replace('\n', " ").lower()
# list_of_words = text_string.split(' ')
# print(list_of_words)


# # for words in list_of_words:
# #     if words in dictionary
# #     dictionary[words] += 1
# #     else:
# #         dictionary[words] = 1
# #         return dictionary

# # print(words)


# from asyncore import read
import re

dictionary = dict()

filepath = open("simple-test-file.txt", "r")

words = re.sub(r'[^\w\s]', '', filepath.read()).lower().split()

print(words)

for words in words:
    if words in dictionary:
        dictionary[words] = dictionary[words] + 1
    else:
        dictionary[words] = 1

        print(dictionary[words])

for allKeys in dictionary:
    print("Frequency of ", allKeys, end=" ")
    print(":", end=" ")
    print(dictionary[allKeys], end=" ")
    print()


