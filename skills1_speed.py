# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    return [num for num in number_list if num % 2 != 0]

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return [num for num in number_list if num %2 == 0]

def word_length(word):
    count = 0
    for letter in word:
        count += 1
    return count

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return [word for word in word_list if word_length(word) >= 4]
def smaller(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    return reduce(smaller, number_list)
def larger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    return reduce(larger, number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return [num / 2 for num in number_list]

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return [word_length(word) for word in word_list]

def sum_nums(num1, num2):
    return num1 + num2

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return reduce(sum_nums, number_list)

def mult(num1, num2):
    return num1 * num2

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return reduce(mult, number_list)

def join_em(word1, word2):
    return word1 + ' ' + word2

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return reduce(join_em, word_list)

def num_count(number_list):
    count = 0
    for num in number_list:
        count += 1
    return count 

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list) / float(num_count(number_list))
