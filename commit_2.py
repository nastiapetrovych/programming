def get_pure_user_words(user_words, letters, words_from_dict):
    correct_words = []
    for word in user_words:
        word = word.lower()
        if len(word) >= 4 and letters[4] in word and word not in words_from_dict:
            bad_letters = False
            for letter in word:
                if word.count(letter) > letters.count(letter):
                    bad_letters = True
                    break

            if not bad_letters:
                correct_words.append(word)

    return correct_words
