#Creating empy list
my_list = []

#Appending Values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value '15' at index 1
my_list[1] = 15

#Extending my_list
ext_list = [50, 60, 70]
my_list.extend(ext_list)

#Removing last element
del my_list[len(my_list) - 1]

#Sorting the list in ascending order
my_list.sort(reverse = False)

#Finding and printing the index of value '30'
for i in my_list:
	if i == 30:
		print(my_list.index(i))

