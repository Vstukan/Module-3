calls = 0
def string_info():
   string = input('Введите слово: ')
   print('(', len(string), ", '", string.upper(), ", '", string.lower(), "'", ')')
   global calls
   calls = calls + 1
def is_contains():
    string = input('Введите ещё слово: ')
    list_to_search = list(input('Введите слова для сравнения: '))
    stringUP = string.upper()
    str_to_search = ''.join(list_to_search)
    str_to_searchUP = str_to_search.upper()
    if stringUP in str_to_searchUP:
        print(True)
    else:
       print(False)
    global calls
    calls = calls + 1
def count_calls():
    global calls
    print(calls)

string_info()
string_info()
is_contains()
is_contains()
count_calls()