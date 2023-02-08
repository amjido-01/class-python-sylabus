values = [];
def my_fun(start, end):
    for value in range(start, end + 1):
        if value % 5 == 0 and value % 7 == 0:
            values.append(value)
    print(values)

my_fun(1500, 2700);




year = int(input('Enter the year: '))

def is_leap_year(year):
    if (year % 4 == 0) or (year % 400 == 0 or year % 100 == 0):
        print(f' {year} is a leap year')
    else:
        print(f'{year} is not a leap year')
        
is_leap_year(year)




# cost_fiber = 0.87;
# company_name = 'KUST LMD'
# company_ft_length = int(input('Enter amount: '));

# def abdul(cost_fiber, company_name):
#     print(company_name)
#     result = company_ft_length * cost_fiber;
#     print(f'{company_name} comapany installed {company_ft_length} fiber optic cable and the total cost is {result} pr ft')
    
# abdul(cost_fiber, company_name)










