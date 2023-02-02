sch_materials = ["pen", "biro", "books", "chairs", "board", "ruler"];
num = [1,2,3,4,5]
list_b = [1,23,4,5]
for sule in sch_materials:
    if sule.startswith('b'):
        list_b.append(sule)
print(list_b)
for x in range(0, 101):
    if x % 2 == 0:
        print(x)