import random
#list comprehension = [new_item for item in list if test] square brackets
#dict comprehension = {new_key:new_value for (key, value) in dict.items if test} squiggly brackets

nums = [1, 2, 3, 4, 5, 6]
print(nums)
new_nums = [n * 3 for n in nums] #multiply each by 3
print(new_nums)

name = "Whitmore"
print(name)
letters_list = [letter for letter in name] #split each individual char
print(letters_list)

new_nums_2 = [n * 10 for n in range(1, 6 + 1)]
print(new_nums_2) # multiply each by 10 in the given range

names = ["Hugo", "Waverly", "Annabeth", "Donna", "Kobe", "Thompson"]
print(names)
short_names = [n for n in names if len(n) < 5]
print(short_names) #names with less than 5 chars
upper_names = [n.upper() for n in names if len(n) > 5]
print(upper_names) #names with more than 5 chars to be upper-cased

numbers_to_square = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(numbers_to_square)
squared_numbers = [n * n for n in numbers_to_square] #multiply by itself
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
print(list_of_strings)
numbers_to_int = [int(n) for n in list_of_strings]
result_int = [n for n in numbers_to_int if n % 2 == 0] #check for even nums from list
print(result_int)

list1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
print(list1)
list2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
print(list2)
match = [int(n) for n in list1 if n in list2]
print(match)

names2 = ["Martha", "Donahue", "Lorne", "Stu", "Burke", "Melanie", "Kath"]
scores = {n:random.randint(50, 100) for n in names2} #gen a random score val from 50 to 100
print(scores)
passed = {n:score for (n, score) in scores.items() if score >= 75} #only those with score 75 or greater passed
print(passed)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result_s = {word:len(word) for word in sentence.split()} #each word's length
print(result_s)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
print(weather_c)
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)
