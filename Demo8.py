#lamda functions with filter function
l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter((lambda no : no %2 == 0),l1)))

