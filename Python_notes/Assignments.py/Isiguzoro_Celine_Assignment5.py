# 1. Write a code that will print all the days of a particular month. 
# The system should be able to prompt you for the year and month.
# The value of the month should either be a number or the month name.

import calendar


def print_month_calendar():

    # 1. Create a simple mapping for month names to numbers
    # We only include the full lowercase names to keep it simple
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }

    # 2. Prompt for year
    year_str = input("Enter the year (e.g., 2024): ")

    # 3. Prompt for month
    month_input = input("Enter the month (e.g., 'July' or '7'): ")


    # First, clean up the user's input
    cleaned_input = month_input.strip().lower()

    month_num = 0  # Initialize to 0 (an invalid month)

    # Check if the cleaned input is a digit (like "7")
    if cleaned_input.isdigit():
        month_num = int(cleaned_input)

    # Otherwise, check if it's in our map (like "july")
    elif cleaned_input in month_map:
        month_num = month_map[cleaned_input]


    # 4. Validate the result and print
    # We check if the number is between 1 and 12
    if 1 <= month_num <= 12:
        # month >= 1 or month <= 12
        # If the month is valid, convert the year to a number
        # Note: This line will crash if the user typed "abc" for the year
        year = int(year_str)

        # Print the calendar
        print("\nHere is the calendar:")
        print(calendar.month(year, month_num))
    else:
        # If month_num is still 0 or an invalid number (like "13")
        print(f"Error: '{month_input}' is not a valid month.")

# print_month_calendar_basic()
