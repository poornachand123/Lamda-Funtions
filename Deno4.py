#lambda with if and if else Condititon

no1 =int(input("1st NO : "))
no2 =int(input("1st NO : "))
bigno = lambda no1,no2: no1 if no1>no2 else no2
print("Biggest No = ",bigno(no1,no2))

