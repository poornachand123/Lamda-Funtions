#example on one arguments

res = lambda no :print("Given No is  =",no)
res(100)
res(1000)
print("=========")
#example on default  arguments
res = lambda no = 0 :print("Given No is  =",no)
res()
res(100)
res(1000)