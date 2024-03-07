#practical 7-Write Python Program to create application which uses date and time in Python.
'''
This program provides a menu for the user to choose from the following options:

Get Current Date and Time
Get Date and Time from User
Exit
The program uses the datetime module to handle date and time operations. The get_current_date_and_time function returns the current date and time. The get_date_and_time_from_user function prompts the user to enter a date and time, and returns the entered date and time. The display_date_and_time function displays the given date and time in the format "YYYY-MM-DD HH:MM:SS". The main function implements the main loop of the application, which continues until the user chooses the "Exit" option.
'''

import datetime

def get_current_date_and_time():
    current_date_and_time = datetime.datetime.now()
    return current_date_and_time.strftime("%Y-%m-%d %H:%M:%S")

def get_date_and_time_from_user():
    year = int(input("Enter year (YYYY): "))
    month = int(input("Enter month (MM): "))
    day = int(input("Enter day (DD): "))
    hour = int(input("Enter hour (HH): "))
    minute = int(input("Enter minute (MM): "))
    second = int(input("Enter second (SS): "))
    date_and_time = datetime.datetime(year, month, day, hour, minute, second)
    return date_and_time

def display_date_and_time(date_and_time):
    print("Date and Time: ", date_and_time.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("Welcome to the Date and Time Application")
    print("1. Get Current Date and Time")
    print("2. Get Date and Time from User")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    while choice != 3:
        if choice == 1:
            current_date_and_time = get_current_date_and_time()
            display_date_and_time(current_date_and_time)
        elif choice == 2:
            date_and_time = get_date_and_time_from_user()
            display_date_and_time(date_and_time)
        else:
            print("Invalid choice. Please try again.")

        choice = int(input("Enter your choice: "))

    print("Thank you for using the Date and Time Application")

if __name__ == "__main__":
    main()