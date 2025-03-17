# String Introduction:

# A string is a sequence of characters, and it is one of the most commonly used
# data types in programming. In most programming languages, strings are used
# to represent text. In Python, strings are immutable, meaning that once a string
# is created, it cannot be changed. In Python, a string is a sequence of
# characters enclosed in either single quotes ( ' ), double quotes ( " ), or triple
# quotes ( ''' or """ ). It serves as one of the fundamental data types in Python.

# names_1 = 'santosh'
# names_2 = "santosh should join pyhton class at 6'o clock"
# names_3 = '''santosh camre to mexico at feb 2023 11 at 8'o clock pm :after 2 years i joined in pyhthon class'''
# print(names_1)
# print(names_2)
# print(names_3)

#  String Object Basics:
# In Python, strings are objects of the str class. You can perform various
# operations on strings, such as accessing individual characters, slicing, and
# more.

# 1. Indexing:
# In Python, indexing refers to the process of accessing individual elements in a
# data structure, such as a list, tuple, or string, using their position or index within
# the data structure. The index is a numerical value that represents the position
# of an element in the sequence, and it usually starts from 0.

# names = "santosh"
# print(names[0])
# print(names[5])
# print(names[4])

# Slicing:

# In Python, slicing is a way to extract a portion or a subsequence of elements
# from a sequence (like a list, tuple, or string). The syntax for slicing is generally
# sequence[start:stop:step] , where:
# start : The index of the first element you want in the slice.
# stop : The index of the first element you do not want in the slice (it's an
# exclusive boundary).
# step (optional): The step or interval between elements in the slice. If
# omitted, it defaults to 1.

# names = "santosh stephen"
# print(names[0::])
# print(names[:9 :])
# print(names[: :2])
# print(names[2:12:])

# Negative indexing in Python allows you to access elements from the end of a
# sequence by using negative integers as indices. In other words, with negative
# indexing, you can count elements from the end of the sequence, where -1
# represents the last element, -2 represents the second-to-last element, and so
# on.
# names = "santosh stephen"
# print(names[-1::])
# print(names[:-14 :])
# print(names[: :-2])
# print(names[-1:-12:-1])
# print(names[:-1:])

# skipping char
# names = "santosh stephen"
# print(names[::4])
# print(names[::-1])


# string methods

# str.upper(): Converts all characters in the string to uppercase.

# names = "santosh"
# upper_case = names.upper()
# print(upper_case)

# lower case
# names = "SANTOSH"
# lower_case = names.lower()
# print(lower_case)

# count()

# count(substring): Returns the number of occurrences of the
# specified substring in the given string.

# names = "santosh kumar agepogu"
# count_1 = names.count('s')
# count_2 = names.count('t')
# print(count_1)
# print(count_2)

# strip()

# Returns a copy of the original string with leading
# and trailing whitespaces removed.

# names = "   santosh kumar agepogu:  "
# strip_1 = names.strip()
# print(strip_1)

# length of a string len(): Returns the number of characters (length) in the giv
# en string.
# names = "santosh kumar agepogu"
# lenght_of_string = len(names)
# print(lenght_of_string)

# split()
# split(separator): Splits the string into a list of substrin
# gs based on the specified separator.

# names = "santosh,kumar,agepogu"
# spli_1 = names.split(',')
# spli_2 = names.split('h')
# print(spli_1)
# print(spli_2)

# replace()
# replace(old, new): Returns a copy of the original string wi
# th occurrences of the specified "old" substring replaced wi
# th the "new" substring.

# names = "santosh kumar is funny"
# names_1 = names.replace('funny','awesome')
# print(names_1)

# startswith() and endswith()
# startswith(prefix): Returns True if the string starts with
# the specified prefix.
# endswith(suffix): Returns True if the string ends with the
# specified suffix.

# names = "santosh kumar agepogu"
# opens = names.startswith('sa')
# ends = names.endswith('ag')
# print(opens)
# print(ends)

# find() and index()
# find(substring): Returns the lowest index of the first occu
# rrence of the specified substring. Returns -1 if the substr
# ing is not found.
# index(substring): Returns the lowest index of the first occ
# urrence of the specified substring. Raises a ValueError if
# the substring is not found.

# names = "santosh stephen"
# name_1 = names.find('j')
# # name_2 = names.index('j')
# print(name_1)
# # print(name_2)

# capitalize()
# capitalize(): Returns a copy of the original string with it
# s first character capitalized.

# names = "santosh stephen"
# names_1 = names.capitalize()
# print(names_1)

# isdigit() and isalpha()
# isdigit(): Returns True if all characters in the string are
# digits.
# isalpha(): Returns True if all characters in the string are
# alphabetic.

# names_1 = "12345"
# names_2 = "santoshkumaragepogu"
# print(names_1.isdigit())
# print(names_2.isalpha())

# join()
# join(iterable): Concatenates the elements of an iterable
# (e.g., a list) into a single string, using the specified se
# parator

# names = ['santosh','kumar','agepogu']
# names_1 = ''.join(names)
# print(names_1)

# Splitting and Joining Strings:

# names = "santosh kumar agepogu"
# names_1 = names.split(',')
# names_2 = "-".join(names)
# print(names_1)
# print(names_2)

# formatted strings

# name = input("enter you name :")
# age = int(input("enter your age:" ))
# print(f"name is {name}and age is {age}")

# task_1

# You are given a string sentence . Print the characters at even indices.
# Example:
# sentence = "Python is amazing"
# output_should = "Pto saaig"

# senten = "python is amazing"
# print(senten[::2])

# task_2
# You are given a string s . Replace all spaces in the string with underscores ( _ )
# and print the modified string.

# s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

# s = "Python is fun and powerful"
# name = s.replace(" ","-")
# print(name)

# task_3

# You are given a string s . Check if the string contains only digits.
# Example:
# s = "12345"

# s = "12345"
# print(s.isdigit())

# task_4

# You are given a string s . Print the string in reverse order.
# Example:
# s = "Python is amazing"

# s = "Python is amazing"
# print(s[::-1])

# task_5

# You are given a string s . Capitalize the first letter of each word in the string
# and print the modified string.
# Example:
# s = "python programming is fun"

# s = "python programming is fun"
# result = [" ".join(word.capitalize() for word in s.split())]
# print(result)

