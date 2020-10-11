
def one():
	print(2 + 3 * 4) # 14
	print((2 + 3) * 4) # 20
	print(2 ** 10) # 1024
	print( 6/3) # 2
	print( 7/3) # 2.3
	print(7//3) # 2
	print(7%3) # 1
	print(3//6) # 0
	print(3 % 6) # 3
	print(2 ** 100) # overflow



def two():

    print(5==10) #false
    print(10>5) #true
    print((5>=1) and (5<=10))#true

# two()

def three():
	my_list = [1,2,3,4]
	big_list = [my_list] * 3
	print(big_list) 
	my_list[2] = 45
	print(big_list)

# three()

def four():
	my_list = [1024, 3, True, 6.5]
	my_list.append(False)
	print(my_list)
	my_list.insert(2,4.5)
	print(my_list)
	print(my_list.pop())
	print(my_list)
	print(my_list.pop(1))
	print(my_list)
	my_list.pop(2)
	print(my_list)
	my_list.sort()
	print(my_list)
	my_list.reverse()
	print(my_list)
	print(my_list.count(6.5))
	print(my_list.index(4.5))
	my_list.remove(6.5)
	print(my_list)
	del my_list[0]
	print(my_list)

# four()

def str_func():
	name = 'shivani'
	# print(name)
	# print(name.upper())
	# print(name)
	# split, join, len, strip, find, statswith, endswith, isnum, isalpha,
	print(name.split())
	print(name.split('i'))
	state = 'My name is an amigo altra'
	print(state.split())
	print(state.split('a'))

	print('  dfe dkfj kk '.strip())

	joined = ' '.join(['shivani', 'pathak', 'is', 'my', 'name'])
	print(joined)

	print(joined.find('pathak'))


# str_func()

def tup_func():
	my_tuple = (2, True, 4.96)
	print(my_tuple)
	# (2, True, 4.96)
	print(len(my_tuple))
	# 3
	print(my_tuple[0])
	# 2
	my_tuple * 3
	# (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
	print(my_tuple[0:2])
	# my_tuple[1] = False

# tup_func()


def set_func():
	my_set = {3, 6, "cat", 4.5, False}
	print(my_set)
	print(len(my_set))
	print({1,34} <= ({1, 34, 12}))

# set_func()

def dic_func():
	capitals = {'iowa': "des moines", "wiscosin": "madison"}
	print(capitals["iowa"])
	capitals["utah"] = "salt lake city"
	print(capitals)
	for k in capitals:
		print(capitals[k], "is the capitals of", k)

# dic_func()	