def myfunc(n):
  return lambda a, b : a * n * b

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11, 2)) 
print(mytripler(11, 2))
