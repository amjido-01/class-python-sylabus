# price per ft
# company name
# total cost
# function



price_per_ft = 0.87
company_name = 'Sir_Man Global Tech'
total_cost = int(input('Enter total installed: '))

def cal_total_fiber_cable(price_per_ft, company_name, total_cost):
    result = price_per_ft * total_cost
    print(f' { company_name } installed { total_cost } fibre cable and the total price is { result }')    
cal_total_fiber_cable(price_per_ft, company_name, total_cost)