val = int(input("Enter the value: "))
unit = input("Enter Unit: ").lower()
def temperature_converter(val, unit): 
    if unit == "c": 
        test = (val * 9/5) + 32
        print(f"{val} degrees Celsius is equal to {test} degrees Fahrenheit")
    elif unit == "f":
        test = (val - 32) * 5/9
        print(f"{val} degrees Fahrenheit is equal to {test} degrees Celsius")
    else:
        print("Invalid temperature scale. Please use 'c' for Celsius or 'f' for Fahrenheit.")

temperature_converter(val, unit)