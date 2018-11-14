#using map function with multiple  iterator
l1 =[10,20,30,40,50]
l2 =[1,2,3,4,5]
print(list(map((lambda  l1,l2:l1*l2),l1,l2)))