def while_func():
	counter = 1
	while counter <= 5:
		print("hello,world")
		counter =counter+1

def for_func():
    for item in [1, 3, 6, 2, 5]:
	     print(item)

 

 	
def str_func():
	word_list = ["cat", "dog", "rabbit"]
	letter_list = []
	for a_word in word_list:
			for a_letter in a_word:
				letter_list.append(a_letter)
	print(letter_list)



# while_func()
# for_func()
# str_func()