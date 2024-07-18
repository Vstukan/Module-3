def single_root_words(root_word, *other_words):
    same_words = []
    other_words_list = [*other_words]
    for other_words in other_words_list:
        if root_word.upper() in other_words.upper() or other_words.upper() in root_word.upper():
           same_words.append(other_words)

    print(same_words)

result1 = single_root_words('rich', 'richiest', 'oRichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
