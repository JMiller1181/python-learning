# print("Hello world!")
import math
import time
import random
# Assigning and working with variables
# name = "Jacob"
# age = 27
# age += 1
# print(name + " is " + str(age))
# height = 5.5
# print("He is " + str(height) + " feet tall")
# last_name, weight, is_adult = "Miller", 165.3, True
# full_name = name + " " + last_name
# print(last_name)
# print(weight)
# print(is_adult)
# Working with strings
# print(last_name.find("l"))
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(last_name.isdigit())
# print(name.isalpha())
# print(last_name.count("l"))
# print(name*3)
# taking input
# string_input = input("Please enter a value: ")
# int_input = int(input("Please enter a value: "))
# print(type(string_input))
# print(type(int_input))
# math methods
# print(round(weight))
# print(math.ceil(weight))
# print(max(height, age, weight))
# print(math.pow(age, 2))
# splitting and slicing strings
# nickname = full_name[0:3:2]
# step_name = full_name[::2]
# reverse_name = full_name[::-1]
# print(nickname)
# print(step_name)
# print(reverse_name)
# search = "http://google.com"
# watch = "http://youtube.com"
# slice = slice(7, -4)
# print(search[slice])
# print(watch[slice])
# if statements
# bad_input = False
# user_age = int(input("Please enter your age: "))
# if user_age >= 18:
#     is_adult = True
# elif 18 > user_age > 0:
#     is_adult = False
# else:
#     bad_input = True
# if is_adult == True and bad_input == False:
#     print("You are an adult")
# elif is_adult == False and bad_input == False:
#     print("You are not an adult")
# else:
#     print("Invalid Age")
# for and while loops
# new_name = None
# while not new_name:
#     new_name = input("Please enter your name:")
#     print(new_name)
# for i in range(age):
#     print(i+1)
# for i in full_name:
#     print(i)
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Count down over!")
# loop control statements
# while True:
#     userInput = input("Give some input")
#     if userInput == "":
#         break
# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     else:
#         print(i, end="")
# lists
# food = ["pizza", "hamburger", "hotdog"]
# print(food[0])
# food[0] = "chicken"
# food.append("fish")
# food.remove("hotdog")
# food.pop()
# food.insert(1, "beef")
# food.sort()
# for x in food:
#     print(x)
# food.clear()
# list1 = ["a", "b", "c"]
# list2 = ["d", "e", "f"]
# list3 = ["g", "h", "i"]
# doubleList = [list1, list2, list3]
# print(doubleList[0][1])
# for x in doubleList:
#     print(x[0])
# tuples
# student = ("Alice", 16, "Junior")
# print(student.count("Alice"))
# print(student.index("Alice"))
# for x in student:
#     print(x)
# if "Junior" in student:
#     print("The student is in their third year")
# sets
# tools = {"wrench", "screwdriver", "hammer", "saw"}
# tools.add("drill")
# tools.remove("hammer")
# for x in tools:
#     print(x)
# hardware = {"nails", "screws", "staples"}
# tools.update(hardware)
# tool_bag = tools.union(hardware)
# dictionaries
# capitals = {"USA":"Washington DC",
#             "France":"Paris",
#             "China":"Beijing",
#             "Italy":"Rome"}
# print(capitals["France"])
# print(capitals.get("USA"))
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# capitals.update({"Japan":"Tokyo"})
# capitals.pop("China")
# for key, value in capitals.items():
#     print(key, value)
# functions
# first_name = "Jacob"
# last_name = "Miller"
# def printNames(first, last):
#     print(first + " " + last)
# printNames(first_name, last_name)
# Exception handling
# try:
#     numerator = int(input("Please enter the numerator: "))
#     denominator = int(input("Please enter the denominator: "))
#     result = numerator / denominator
#     print("The outcome is: " + str(result))
# except ZeroDivisionError:
#     print("Cannot divide by 0")
##############################################################
###      End basic practice code begin test programs       ###
##############################################################
# RPS
# hands = ("rock", "paper", "scissors")
# running = True
#
# while running:
#
#     player = None
#     computer = random.choice(hands)
#
#     while player not in hands:
#         player = input("Enter a choice (rock, paper, scissors): ")
#
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#
#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
#
# print("Thanks for playing!")
#