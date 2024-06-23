# ['my', 'name', 'is'] = ['My', 'Name', 'Is']

list1 = ['my', 'name', 'is']
list2 = list(map(str.capitalize, list1))
print(list2)