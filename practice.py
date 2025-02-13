# list1 = [5, 33, 16, 70]
# for number in list1:
#  print(number, end= " ")

# print(" and today's date is ")
# print('11','06','2024', sep='/')

# Dictionaries to be merged

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# # Merging dictionaries
# merged_dict = dict1 | dict2

# print(merged_dict)

# my_list = ['']

# if my_list == True:
#     print("The list is not empty")
# else:
#     print("The list is empty")
# print(len(my_list))



# import calendar
# year = calendar.isleap(2024)
# if year == True:
#     print("Yes")
# else:
#     print("No")
# Year and month for which the calendar is to be displayed
# year = 2024
# month = 6

# Create a plain text calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)
# month_calendar = cal.formatmonth(year, month)

# print(month_calendar)


# from datetime import datetime

# Get current date and time

# now = datetime.now()

# Format the date and time

# current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# print("Current Time and Date:", current_time)



# list1 = [2, 5, 6, 8, 1, 8, 9, 11]

# list2 = ["Kenya","USA","Tanzania", "Egypt", "Cambodia"]
# list1.sort(reverse=True)
# list2.sort(reverse=True)
# print(list1)
# print(list2)


# x, y = 20, 30
# x, y = y, x

# print('x is', x)
# print('y is', y)

# Another way of swapping variables
# s = 20
# t = 30

# s ^= t

# t ^= s

# s ^= t
# print(f'x is: {s}')
# print(f'y is: {t}')


# from collections import Counter 


# list1 = ['John','Kelly', 'Peter', 'Moses', 'Peter'] 

# count_kelly = Counter(list1).get("Kelly") 

# print(f'The name Kelly appears in the list ' 
# f'{count_kelly} times.') 





# list1 = [[1, 2, 3], [4, 5, 6]]

# flat_list= [i for j in list1 for i in j]

# print(flat_list)



# Absolute value of a Number


# todays_temperature = -13
# absolute_value = abs(todays_temperature)

# print("Absolute value of", todays_temperature, "is", absolute_value)


# Find the index of the largest number
# Way 1
# x = [12, 45, 67, 89, 34, 67, 13]
# max_number = max(enumerate(x, start=0), key = lambda x: x[1])

# print('Way 1: The index of the largest number is', max_number[0])

# # Way 2
# max_num = max(x)
# max_index = x.index(max_num)
# print('Way 2: The index of the largest number is', max_index)

# # # Find the index of the smallest number
# # Way 1
# y = [56, 74, 19, 45, 9, 21, 37]
# min_number = min(enumerate(y, start=0), key = lambda y: y[1])

# print('\nWay 1: The index of the smallest number is', min_number[0])

# # Way 2
# numbers = [10, 3, 5, 1, 9, 2]

# min_number = min(numbers)
# min_index = numbers.index(min_number)

# print('Way 2: The index of the smallest number is', min_index)


# my_list = [3452735, 4272538, 4528342, 46237428]

# new_list = [f"{num:,}" for num in my_list]

# print(new_list)


# todays_list = ['Flora','Gabriel','James','Steve','Gareth','Joseph','Joyce','Jesse']

# for x in todays_list:
#     new_list1 = [x for x in todays_list if x.startswith('J')]
#     new_list2 = [x for x in todays_list if x.endswith('e')]
#     new_list3 = [x for x in todays_list if x not in new_list1 and new_list2]

# print(new_list1)
# print(new_list2)
# print(new_list3)
    


# Using nlargest

# import heapq

# list1 = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]

# print(heapq.nlargest(5, list1))

# # Using nsmallest

# list2 = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]


# print(heapq.nsmallest(5, list2))



# Checking for Anagram
# from collections import Counter

# string1 = "listen"
# string2 = "silent"

# # Way 1
# result1 = Counter(string1) == Counter(string2)

# if result1:
#     print('Anagrams')
# else:
#     print('Not Anagrams')


# # Way 2
# result2 = sorted(string1) == sorted(string2)

# if result2:
#     print('Anagrams')
# else:
#     print('Not Anagrams')


# import speedtest

# def check_internet_speed():
#     # Create a Speedtest object
#     st = speedtest.Speedtest()

#     # Retrieve a list of available servers
#     servers = st.get_servers()
#     print(dict(servers))
    
#     # Find the best server based on ping
#     best_server = st.get_best_server()
#     print(f"Best server based on ping: {best_server['host']} located in {best_server['name']}")

#     # Perform a download speed test
#     download_speed = st.download() / 1_000_000  # Convert to Mbps
#     print(f"Download speed: {download_speed:.2f} Mbps")

#     # Perform an upload speed test
#     upload_speed = st.upload() / 1_000_000  # Convert to Mbps
#     print(f"Upload speed: {upload_speed:.2f} Mbps")

#     # Get ping time
#     ping = st.results.ping
#     print(f"Ping: {ping} ms")

#     # Get a URL to an image of the results
#     result_url = st.results.share()
#     print(f"Speedtest result image URL: {result_url}")

# # Checking the internet speed
# check_internet_speed()


# Reserved Keywords in Python
# import keyword

# # Way 1

# print(help('keywords'))

# # Way 2

# def list_reserved_keywords():
#     reserved_keywords = keyword.kwlist
#     for kw in reserved_keywords:
#         print(kw)

# list_reserved_keywords()



# Properties and Methods
# import datetime

# print(dir(datetime))



# Opening a website using Python

# import webbrowser

# url = ('https://www.linkedin.com/feed/')

# open_web =  webbrowser.open(url)

# print(open_web)


# Most Frequent in a String
# Way 1

# my_name = 'Steve'

# most_frequent = max(my_name, key=my_name.count)

# print(f'The most frequent element is, ' f'{most_frequent}')


# Way 2

# from collections import Counter as C

# a = 'recklessness'

# most_frequent = C(a).most_common(1)

# print(f'The most frequent element is, ' f'{most_frequent}')


# Memory size check

# import sys


# a = ['Winter', 'Summer', 'Spring', 'Autumn']
# b = {'Winter', 'Summer', 'Spring', 'Autumn'}
# c = ('Winter', 'Summer', 'Spring', 'Autumn')


# print(f'The memory size of a list is 'f'{sys.getsizeof(a)}')

# print(f'The memory size of a set is 'f'{sys.getsizeof(b)}')

# print(f'The memory size of a tuple is 'f'{sys.getsizeof(c)}')



# Accessing dictionary keys

#  Way 1
# Using the set comprehension

# dict_1 = {
#     "name":"Steve",
#     "age":12,
#     "height":"166 cm",
#     "hobby":"football",
#     "language":"Python"
# }

# print({key for key in dict_1.keys()})


# Way 2
# Using the set() function

# print(set(dict_1))


# Way 3
# Using the sorted() function

# sorted_dict = sorted(dict_1)

# print(sorted_dict)




# Iterable or Not using the iter() function


# seasons = ['Winter', 'Summer', 'Spring', 'Autumn']



# try:
#     iter_check = iter(seasons)
# except TypeError:
#     print('Object '  + str(seasons) + ' is not iterable')
# else:
#     print('Object ' + str(seasons) + ' is iterable')


# Sorting a List of Tuples using the itemgetter class
# from operator import itemgetter


# cars = [('Volkswagen', 'Tiguan'),('Honda', 'Prologue'),('Mercedes', 'Benz'),
#                 ('Volvo', 'S90'),('Nissan', 'Patrol'),('Toyota','Landcruiser'),('Ford', 'Ranger')]

# # Sort by first name of the car
# sorted_cars1 = sorted(cars, key=itemgetter(0))

# # Sort by last name of the car
# sorted_cars2 = sorted(cars, key=itemgetter(1))

# # Sort by first and last names of the car
# sorted_cars3 = sorted(cars, key=itemgetter(0,1))

# print('Sorted by first car name\n', sorted_cars1)

# print('Sorted by last car name\n', sorted_cars2)

# print('Sorted by first and last car names\n', sorted_cars3)


# Sort List with Sorted & Lambda

# sort descending
# list1 = ['Mary', 'Peter', 'Kelly']
# a = lambda x: x[-1]

# y = sorted(list1, key=a)

# print(y)

# # sort ascending

# b = lambda x: x[:1]

# x = sorted(list1, key=b)

# print(x)


# # default sorting

# z = sorted(list1)

# print(z)



# Access News using Python
# from newspaper import Article

# news = Article('https://www.citizen.digital/')

# news.download()

# news.parse()

# print(news.authors)
# print("\n")
# print(news.title)
# print("\n")
# print(news.text)
# print("\n")
# print(news.images)

# Drone control script
# from dronekit import connect, VehicleMode
# import time

# # Connection string (replace with your actual connection details)
# connection_string = 'tcp:127.0.0.1:14550'

# # Connect to the vehicle
# vehicle = connect(connection_string, wait_ready=True)

# # Define the target altitude
# target_altitude = 5  # meters

# def arm_and_takeoff(target_altitude):
#   """
#   Arms and takes off the drone to a target altitude.
#   """
#   print("Arming...")
#   vehicle.armed = True

#   while not vehicle.armed:      
#     print("Waiting for pre-arm checks...")
#     time.sleep(1)

#   print("Taking off!")
#   vehicle.simple_takeoff(target_altitude)

#   # Wait until the drone reaches a safe height
#   while vehicle.location.global_relative_frame.alt < target_altitude * 0.95:
#     print("Reaching target altitude...")
#     time.sleep(1)

#   print("Target altitude reached!")

# def land_drone():
#   """
#   Lands the drone.
#   """
#   print("Landing...")
#   vehicle.mode = VehicleMode('LAND')
#   # Wait until the drone lands
#   while vehicle.mode != 'LAND':
#     print("Waiting for landing...")
#     time.sleep(1)
#   print("Landed!")

# # Arm and takeoff
# arm_and_takeoff(target_altitude)

# # Land the drone
# land_drone()

# # Close connection
# vehicle.close()
# print("Completed!")





# A List of Tuples with Enumerate

# days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


# list_of_tuples = list(enumerate(days_of_the_week, start=1))

# print(list_of_tuples)





# Assertion

# items = ['Pen','pencil','ruler','rubber', 43]

# lower_items = []

# for item in items:
#     assert type(item) == str, 'non-string items are in the list' 
#     if item.islower():
#         lower_items.append(item)

# print(lower_items)





# Print Colored Text

# Way 1
# class Colors():
#  Black = '\033[30m' 
#  Green = '\033[32m' 
#  Blue = '\033[34m' 
#  Magenta = '\033[35m' 
#  Red = '\033[31m' 
#  Cyan = '\033[36m' 
#  White = '\033[37m' 
#  Yellow = '\033[33m' 
 
 
# print(f'{Colors.Red} Warning: {Colors.Magenta} ' 
#  f'Love Don\'t live here anymore')


# Way 2

# from colorama import Fore, Style, init

# # Initialize colorama
# init()

# # Print colored texts
# print(Fore.RED + "This is red text")
# print(Fore.GREEN + "This is green text")
# print(Fore.BLUE + "This is blue text")
# print(Style.RESET_ALL)  # Reset to default color

# # Combine styles and colors
# print(Fore.YELLOW + Style.BRIGHT + "This is bright yellow text")
# print(Fore.CYAN + Style.DIM + "This is dim cyan text")
# print(Style.RESET_ALL)  # Reset to default color


# Find Index Using Enumerate


# my_name = 'Steve'

# for index, value in enumerate(my_name):
#     if value == 'v':
#         print(f"The index of v in {my_name} is {index}")


# Multithreading in Python

# import threading
# import time


# def print_numbers(thread_name):
#     for i in range(1, 10):
#         time.sleep(1)
#         print(f"{thread_name}: {i} ")


# thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
# thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Both threads and have finished execution")

# from scipy import stats

# def q_critical(k, n, alpha):

#   df_error = (k * n) - k
#   q_value = stats.studentized_range.ppf(1 - alpha, k, df_error)
#   return q_value

# k = 3  # Number of groups
# n = 4  # Observations per group
# alpha = 0.05  # Significance level

# q_crit = q_critical(k, n, alpha)
# print(q_crit)



# Creating a class using type()
# MyClass = type('MyClass', (object,), {'x': 5, 'show': lambda self: print(self.x)})

# # Using the dynamically created class
# obj = MyClass()
# obj.show()  

# Checking if a String is Empty

# my_name = ''

# if not my_name:
#     # print('This string is empty')
#     my_name = ('Steve')
#     print(my_name)
# else:
#     print('The string is not empty')


# Flattening a nested list

# Way 1 - Using the sum() function

# odd_numbers = [[1, 3, 5], [7, 9, 11]]

# new_list1 = sum(odd_numbers,[])

# print(new_list1)


# # Way 2 - Using the reduce() function of the functools module
# from functools import reduce

# new_list2 = reduce(lambda x, y: x + y, odd_numbers)

# print(new_list2)


# # Way 3 - Using the List Comprehension

# flat_list = [item for sublist in odd_numbers for item in sublist]

# print(flat_list)


# Checking if a File Exists
# import os


# file = os.path.exists('thisfile.txt')

# if file:
#     print("This file exists!")
# else:
#     print("This file does not exist!")


# Set Comprehension

# list1 = [23, 56, 23, 73, 10, 17]


# set1 = {num for num in list1}

# print(set1)




# Python *args and **Kwargs

# def my_function1(*kids):
#     print("The youngest child is " + kids[2])


# my_function1("Tobias","Diana","Esther")

# def my_function2(**dish):
#     print("Her favorite dish is " + dish["dish2"])

# my_function2(dish1 = "Fries", dish2 = "Chicken")


# The filter() function

# cars = ["Toyota","Honda","volkswagen","bmw","audi"]

# cars2 = list(filter(lambda x: x.islower(), cars))

# print(cars2)









# Dictionary Comprehension

# dict_1 = {'height':70, 'weight': 50, 'length': 20}

# dict_2 = {k : float(v) for(k, v) in dict_1.items()}

# print(dict_2)


# DataFrame from Two Lists

# import pandas as pd

# list1 = ["Jackie","Vale","Diana"]
# list2 = [78, 87, 98]

# df = pd.DataFrame(list(zip(list1,list2)), index=[1, 2, 3], columns=["Names","Marks"])
# print(df)
# print("\n")

# # Adding a Column to a DataFrame

# df['Age'] = [17, 16, 18]
# print(df)
# print("\n")

# # Dropping  a Column from a DataFrame

# df.drop('Marks', inplace=True, axis=1)

# print(df)



# Timer Decorator

# import time

# def timer(func):
#  def inner():
#     start = time.perf_counter()
#     func()
#     end = time.perf_counter()
#     print(f'Run time is {end-start:.2f} seconds')
#  return inner


# @timer
# def range_tracker():
#  my_list = []
#  for i in range(10000000):
#     my_list.append(i**2)
# range_tracker()


# List Comprehension vs Generators

# import timeit
# import sys


# # function to check time execution
# def timer(_, code):
#    exc_time = timeit.timeit(code, number=1000)
#    return f'{_}: execution time is {exc_time:.2f}' 
 
# # function to check memory allocation 
# def memory_size(_, code):
#    size = sys.getsizeof(code)
#    return f'{_}: allocated memory is {size}' 
 
# one = 'Generator' 
# two = 'list comprehension' 
 
# print(timer(one, 'sum((num**2 for num in range(10000)))'))
# print(timer(two, 'sum([num**2 for num in range(10000)])'))
# print(memory_size(one,(num**2 for num in range(10000))))
# print(memory_size(two,[num**2 for num in range(10000)]))


# import mysql.connector


# db_config = {
#     "host":"your_host",
#     "username":"your_username",
#     "password":"your_password",
#     "database":"db_name"
# }

# db_connection = mysql.connector.connect(**db_config)

# print(db_connection.server_host)

# db_cursor = db_connection.cursor()

# query = "SELECT * FROM girls"

# db_cursor.execute(query)
# results = db_cursor.fetchall()

# for student in results:
#     print(student)






# Writing to File

# names = ['John James', 'Tacy Wangari', 'Kimberly Mogeni']

# with open('names.csv', 'w') as file:
#     for name in names:
#         file.write(name)
#         file.write('\n')


# # reading CSV file
# with open ('names.csv', 'r') as file:
#  print(file.read())


# Merge PDF files

# import PyPDF2
# from PyPDF2 import PdfMerger, PdfReader


# # Create a list of files to merge
# list1 = ['file1.pdf', 'file2.pdf']
# merge = PdfMerger(strict=True)

# for file in list1:
#  merge.append(PdfReader(file,'rb+'))

# # Merge the files and name the merged file
# merge.write('mergedfile.pdf')
# merge.close()


# # Reading the created file
# created_file = PdfReader('mergedfile.pdf')
# print(created_file)



# Return vs Yield

# def num1(n: int) -> int:
#     for i in range(n):
#         return i

# print("Function 1 returns: " + str(num1(10)))    


# def num2(n: int):
#     for i in range(n):
#         yield i
    
# gen = num2(10)

# print("\nFunction2 yields: ")
# for i in gen:
#     print(i, sep='')
    

# High-order functions

# cars = [('Toyota','Landcruiser'),('Lamborgini','Murcielago'),
#  ('Volkswagen','Tiguan'), ('Ford','Ranger')]

# sorted_cars = sorted(cars, key= lambda x: x[0])

# print('The sorted list of cars is ',sorted_cars)


# Grammar Errors

# from gramformer import Gramformer 

# # Create a Gramformer instance
# gf = Gramformer()

# # Text to be corrected
# text = "This sentance has a misspellig."

# # Correct the text
# corrected_text = gf.correct(text)

# print(corrected_text) 



# The Zen of Python
# import this

# print(this)


# Sorted by Pprint
# Sort a dictionary by key
# import pprint

# my_dict = {'x':2, 'd':34, 'f':23, 'e':10, 'l':2}

# pp = pprint.PrettyPrinter(sort_dicts=True)

# pp.pprint(my_dict)


# Convert Picture to Grey Scale

# import cv2 as cv

# img = cv.imread('python.jpeg')

# # show the original image

# img1 = cv.imshow('Original', img)
# cv.waitKey(5)

# # Converting image to Gray

# grayed_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Show grayed-out image

# img2 = cv.imshow('grayed_image', grayed_img)
# cv.waitKey(5000)

# #Save image
# cv.imwrite('grayed.jpg', grayed_img)


# Time it with timeit

# import timeit


# def timer(code):
#     tm = timeit.timeit(code,number=10000)
#     return f'Execution time is {tm:.2f} seconds.' 
 
# if __name__ == "__main__":
#  print(timer('sum(num**2 for num in range(10000))'))


# Shortening URL with Python

# import pyshorteners


# def shorter_Url(s: str):
#     ps = pyshorteners.Shortener()
#     short_url = ps.tinyurl.short(s)
#     return "The shorter url is ", short_url

# print(shorter_Url('https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#SecurityGroups:'))


# The Round Function
# import math

# num = 367.2781

# print(round(num, 1))

# # Round up to the nearest integer
# print(math.ceil(num))

# # Round down to the nearest integer
# print(math.floor(num))


# Convert PDF Files to Doc
# from pdf2docx import Converter 

# # path to your pdf file
# pdf = 'file1.pdf'

# # path to where your doc file will be saved
# word_file = 'file1.docx'

# #instantiate converter
# cv = Converter(pdf)
# cv.convert(word_file)

# #close file
# cv.close()


#  Text from PDF File
# import PyPDF2

# # Open a pdf file
# pdf_file = open('file1.pdf', 'rb')

# # Read pdf reader 
# read_file = PyPDF2.PdfReader(pdf_file)

# # Read from a specified page 
# page = read_file.pages[2]

# # extracting text from page 
# print(page.extract_text())

# # closing pdf file
# pdf_file.close()



#  Libraries Locations

# import pyshorteners

# print(pyshorteners)





# Create a Barcode

# from barcode import ISBN13
# from barcode.writer import ImageWriter
# from PIL import Image


# num = '979113445319' 

# # saving image as png
# bar_code = ISBN13(num, writer=ImageWriter())


# # save image
# bar_code.save('bar_code')


# #read the image using pillow
# img = Image.open("bar_code.png")
# img.show()


# Indices Using Len & Range Functions

# cars_list = ['Ferrari', 'Honda', 'Mercedes']

# for car in range(len(cars_list)):
#     print(car, cars_list[car])




# Convert Text to Emoji
# Convert Emoji to Text

# import demoji
# import emoji


# emoji_str = "I love playing Need For Speed Most Wanted🚘🚘🚘. It makes me happy!😎"

# emoji_example = "I love :orange_heart: learning Python :snake: on a daily basis!, what about you? :smiling_face_with_smiling_eyes:"

# emoji1 = emoji.emojize(emoji_example)

# print(emoji1)

# print("\n")

# list1 = list(demoji.findall(emoji_str))
# print(list1)

# emoji_list = list(emoji.EMOJI_DATA.keys())

# for emoji_char in emoji_list:
#     print(emoji_char)

# emoji_names = list(emoji.EMOJI_DATA.values())

# for emoji_name in emoji_names:
#     print(emoji_name)


# import requests

# # Define the function for currency conversion
# def currency_converter():
#     # Enter the amount to convert
#     amount = int(input("Please enter amount to convert: "))

#     # currency code of the amount to convert
#     from_currency = input("Enter the currency code of the amount you are converting: ").upper()

#     # currency code of the amount to convert to
#     to_currency = input("Enter the currency code you are converting to: ").upper()

#     # Make a request to a currency API
#     url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    
#     try:
#         # Get the conversion rate 
#         response = requests.get(url, verify=True)
#         data = response.json()

#         if to_currency in data['rates']:
#             # Calculate the converted amount
#             converted_amount = amount * data['rates'][to_currency]
#             return f'\nThe amount is {converted_amount:.2f} and the currency is {to_currency}'
#         else:
#             return f'\nCurrency {to_currency} not found!'
    
#     except Exception as e:
#         return f'Error occurred: {str(e)}'

# # Call the function
# print(currency_converter())


# Generate Custom Font

# import pyfiglet as pf

# text = pf.figlet_format("I love Maria", font="puffy")

# print(text)

# To get a list of cool fonts run the below line
# print(pf.FigletFont.getFonts())



# Language Detector

# from langdetect import detect

# language1 = detect('¿Qué te gusta hacer')

# language2 =  detect('Nyasae no omuya')


# print('This is the Spanish language shortened by: ',language1)

# print('This is the Kisii language shortened by: ',language2)



# Refresh URL with Selenium
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# url = "https://www.youtube.com/"

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get(url=url)

# time.sleep(10)
# driver.refresh()


# Substring of a String

# positive_statement = "Python is a multi-purpose, easy-to-learn, enjoyable programming language!"

# # Way 1

# if 'enjoyable' in positive_statement:
#     print('enjoyable is a substring of positive_statement')
# else:
#     print('enjoyable is not a substring of positive_statement')


# # Way 2

# if 'enjoyable' not in positive_statement:
#     print('enjoyable is not a substring of positive_statement')
# else:
#     print('enjoyable is a substring of positive_statement')


# # Let's find the index of the substring in the string given

# print('The index of the substring in the string given is:', positive_statement.find('enjoyable'))


# Difference Between Two Lists

# even_numbers = [0, 2, 4, 6, 8, 10]
# prime_numbers = [2, 3, 5, 7, 11, 13]


# # Way 1

# difference1 = set(even_numbers).difference(set(prime_numbers))

# print(list(difference1))


# print("==============================")

# # Way 2
# # The easiest way

# difference2 = [number for number in even_numbers if number not in prime_numbers]

# print(difference2)



# Sorting a List of Dictionaries
# from operator import itemgetter

# countries = [{"name":"Britain", "population":130000}, {"name":"Kenya", "population":26000},
#              {"name":"Zambia", "population":200000}, {"name":"China", "population":1000000},
#              {"name":"Mauritius", "population":459580}, {"name":"Finland", "population":56093}]

# # Sort according to country's name
# sorted_countries1 = sorted(countries, key=itemgetter('name')) 

# # Sort according to country's population
# sorted_countries2 = sorted(countries, key=itemgetter('population'))

# print(sorted_countries1)
# print("\n")
# print(sorted_countries2)


# Bytes to Strings

# s = b'Practicing Python is a cool way of learning it!'

# print(type(s))


# # Way 1
# str1 = str(s,"UTF-8")
# print("\n")

# print("The string", str1, "is of type", type(str1))

# # Way 2
# str2 = s.decode()
# print("=====================================================")

# print("The string", str2, "is of type", type(str2))


# Multiple Input from User
# import speech_recognition as sr

# your_cars = [name for name in input("Enter multiple cars: ").split(sep=',')]

# print(your_cars)

# def listen_for_input():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something...")
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         print("You said: " + text)
#         return text
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Example usage
# user_input = listen_for_input()
# print("User input:", user_input)




# The _iter_() Function

# cars = ['Volkswagen', "Lamborghini", 'Toyota']

# iter_object = iter(cars)

# while True:
#     try:
#         print(next(iter_object))
#     except:
#         break




# list1 = ['club', 'country']
# list2 = ['Liverpool', 'England']


# dict1 = dict(zip(list1,list2))

# print(dict1)



# from itertools import permutations

# def get_permutations(s: str):
#     arr = []
#     for i in permutations(s):
#         arr.append(''.join(i))

#     return arr

# print(get_permutations('KES'))





# cars = [ 'Mercedes Benz', 'Toyota Landcruiser', 'Volkswagen Touareg’, ‘Nissan Patrol']

# car, *cars_with_v8_engines = cars
# print(car)
# print(cars_with_v8_engines)


# from statistics import *

# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 23, 29, 31]

# mean = mean(data)
# print("The mean of the given data is",mean)

# mode = mode(data)
# print("The mode of the given data is",mode)

# stdev = stdev(data)
# print("The standard deviation of the given data is",stdev)

# variance = variance(data)
# print("The variance of the given data is",variance)



# Python Type Hints
# def greet(name: str) -> str:
#     return f"Hello, {name}!"

# print(greet("Camila"))











