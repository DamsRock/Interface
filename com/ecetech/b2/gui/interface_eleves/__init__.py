import importlib
pmName = input('Enter module name:')
pm = __import__(pmName)
print(dir(pm))
