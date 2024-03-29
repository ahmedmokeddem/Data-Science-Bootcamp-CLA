a = 12
s = "hello"
try:
	print("inside try")
	print(a + s) # will raise TypeError
	print("Printed using original data types")
except TypeError: # will handle only TypeError
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")
except NameError: print("one of the variables is not declared")
except IndentationError: print("The indentation is not respected")
