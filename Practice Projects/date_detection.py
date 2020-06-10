# Chapter 7: Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.

import re


# Regex that matches DD/MM/YYYY
date_regex = re.compile(r"""(
    (0[1-9] | [1|2]\d | 31)            # Day
    /                                  # Separator
    (0[1-9] | 1[1|2])                  # Month
    /                                  # Separator
    ([1|2]\d{3})                       # Year
    )""", re.VERBOSE)


# Test regex
test_string = "Testing regex with 01/01/1000, 31/02/2020, 29/02/2020, 31/04/2021 and 31/12/2999, which are technically valid dates, and some impossible dates: 00/01/2020, 01/00/2020, 32/01/2020 and 01/13/2020."
print(test_string, end = '\n\n')

extracted_dates = date_regex.findall(test_string)
print('Dates found:')
[print(match[0]) for match in extracted_dates]


# Function to check if date is valid
def date_validator(dates):
    valid_dates = []
    months_with_30_days = ['04', '06', '09', '11']

    print('\nValidating dates...')
    for match in dates:
        # Validate months with 30 days
        if match[2] in months_with_30_days:
            if int(match[1]) <= 30:
                valid_dates.append(match[0])
            else:
                print(f"{match[0]} is not a valid date.")

        # Validate February, which has 28 days during non-leap years and 29 days during leap years
        elif match[2] == "02":
            # Check if days are 29 or less during leap year
            if int(match[3]) % 4 == 0 and (int(match[3]) % 100 != 0 or int(match[3]) % 400 == 0) and int(match[1]) <= 29:
                valid_dates.append(match[0])
            # Check if days are 28 or less during non-leap year
            elif int(match[1]) <= 28:
                valid_dates.append(match[0])
            else:
                print(f"{match[0]} is not a valid date.")
        else:
            valid_dates.append(match[0])

    # Print out valid dates
    print("\nValid dates:")
    [print(date) for date in valid_dates]

    
# Run date validator function
date_validator(extracted_dates)