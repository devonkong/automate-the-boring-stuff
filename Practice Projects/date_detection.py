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
test_string = "Testing regex with 01/01/1000, 31/02/2020, 31/04/2021 and 31/12/2999, which are technically valid dates, and some impossible dates: 00/01/2020, 01/00/2020, 32/01/2020 and 01/13/2020."
print(test_string, end = '\n\n')

extracted_dates = date_regex.findall(test_string)
print('Dates found:')
for match in extracted_dates:
    print(match[0])


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

        # Validate February on non-leap years, which has 28 days
        elif match[2] == "02":
            if int(match[1]) <= 28:
                valid_dates.append(match[0])
            else:
                print(f"{match[0]} is not a valid date.")

        # TODO: Check for leap year

        else:
            valid_dates.append(match[0])

    print(valid_dates)

date_validator(extracted_dates)


# TODO: Match and validate from clipboard