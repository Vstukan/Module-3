calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    str_tup = (len(string), string.upper(), string.lower())
    return (str_tup)

def is_contains(string, list_to_search):
    count_calls()
    stringUP = string.upper()
    str_to_search = ''.join(list_to_search)
    str_to_searchUP = str_to_search.upper()
    if stringUP in str_to_searchUP:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

