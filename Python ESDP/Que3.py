set1 = {10,20,30,40,50}
set2 ={30,40,50,60,70}
set3 = {}
print(type(set3))
set4 = set1.union(set2)
set3 = set1.intersection(set2)
set5 = set2.difference_update(set1)
print(set5)
#print(set3)
#print(set4)