import sys

if len(sys.argv) != 2:
    print("Usage: python leap_year.py <year>")
else:
    year = int(sys.argv[1])

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")