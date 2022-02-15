my_list = [1, 5, 4, 6, 8, 11, 3, 12]

#syntax:map(function_name,iterable)
new_list = list(map(lambda x: x * 2 , my_list)) #display list value *2 ex= 1*2=2...using map func

print(new_list)