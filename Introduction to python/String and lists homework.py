print(list_even_num:=[i for i in range(1,299) if (i%2) == 0])
print("The length of the list is equal to ",len(list_even_num))
print("Squared values of the list are ",[x**2 for x in list_even_num])
print("57 is in this list:",57 in list_even_num)