# values = [];
# def my_fun(start, end):
#     for value in range(start, end + 1):
#         if value % 5 == 0 and value % 7 == 0:
#             values.append(value)
#     print(values)

# my_fun(1500, 2700);


cost_fiber = 0.87;
company_name = 'KUST LMD'
company_ft_length = int(input('Enter amount: '));

def abdul(cost_fiber, company_name):
    print(company_name)
    result = company_ft_length * cost_fiber;
    print(f'{company_name} comapany installed {company_ft_length} fiber optic cable and the total cost is {result} pr ft')
    
abdul(cost_fiber, company_name)

# user = input('enter your name ')
# if not user.isalpha():
#     print('name must be a string')
# else:
#     print('welcome')

# response = 'yes'
# question = input('can i give you another question')
# if question.lower() == response:
#     print('what is noun')
# else:
#     print('goodbye')



