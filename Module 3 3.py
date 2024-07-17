def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 'Wov', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, c = 8)
print_params(6)

values_list = ['пять', 3, False]
values_dict = {'a':True, 'b':7, 'c':'два'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
