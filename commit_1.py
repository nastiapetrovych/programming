def get_user_words():
    user_words = []
    while True:
        word = input('Enter word: ')
        if word == '^D':
            break
        user_words.append(word)

    return user_words