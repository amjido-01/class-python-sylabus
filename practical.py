#   python program that will find those numbers which are divisible by 7 and multiple of 5 between 1500 and 2700 both inclusive with 10 different ways of clean and efficient ways
# give 10 other ways
numbers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(i)

print(numbers)


#sql
def divisible_by_7_and_multiple_of_5_generator(start, end):
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            yield i

result = list(divisible_by_7_and_multiple_of_5_generator(1500, 2700))
print(result)

###############################33

def divisible_by_7_and_multiple_of_5(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result

result = divisible_by_7_and_multiple_of_5(1500, 2700)
print(result)

###################################################

result = list(map(lambda x: x if x % 7 == 0 and x % 5 == 0 else None, range(1500, 2701)))
result = [i for i in result if i is not None]
print(result)

result = list(filter(lambda x: x % 7 == 0 and x % 5 == 0, range(1500, 2701)))
print(result)

result = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)



#scss
result = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]
print(result)


result = [i for i in (x for x in range(1500, 2701) if x % 7 == 0 and x % 5 == 0)]
print(result)

import pandas as pd
result = pd.Series(range(1500, 2701)).where((pd.Series(range(1500, 2701)) % 7 == 0) & (pd.Series(range(1500, 2701)) % 5 == 0)).dropna().tolist()
print(result)

import numpy as np
result = np.where((np.arange(1500, 2701) % 7 == 0) & (np.arange(1500, 2701) % 5 == 0))[0]
print(result)

import itertools
result = list(itertools.compress(range(1500, 2701), [x % 7 == 0 and x % 5 == 0 for x in range(1500, 2701)]))
print(result)

