cost_per_ft = 0.87
company_name = input('Enter company name: ')
company_total_supply = int(input('Enter amount: '))

def calculate_total_fiber(cost_per_ft, company_name, company_total_supply):
    result = cost_per_ft * company_total_supply
    print(f' {company_name} installed  {company_total_supply} fiber cable and total cost is {result}!')
    
calculate_total_fiber(cost_per_ft, company_name, company_total_supply)