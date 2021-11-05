import random


def get_words(f, letters):
    with open(f, 'rt') as file:
        words = []
        for line in file:
            word = line.strip().lower()
            if len(word) >= 4 and letters[4] in word:
                bad_letters = False
                for letter in word:
                    if letter not in letters or word.count(letter) > letters.count(letter):
                        bad_letters = True
                        break

                if not bad_letters:
                    words.append(word)
    
    return list(set(words))


def get_user_words():
    user_words = []
    while True:
        word = input('Enter word: ')
        if word == '^D':
            break
        user_words.append(word)

    return user_words


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


def generate_grid():
    letters = random.choices('abcdefghijklmnopqrstuvwxyz'.upper(), k=9)
    return [letters[:3], letters[3:6], letters[6:]]

    
def results():
    game_grid = generate_grid()
    with open('result.txt', 'wt') as file:
        file.write('Game results')
    return results

print(get_words('en.txt', [el for el in 'jniarnoah']))