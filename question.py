# is year a leap or not
# ask for the
# function

year = int(input('Enter the year'))

def is_leap_year(year):
    if (year % 4 == 0) or (year % 400 == 0 or year % 100 == 0):
        print(f' {year} is a leap year')
    else:
        print(f'{year} is not a leap year')
        
is_leap_year(year)