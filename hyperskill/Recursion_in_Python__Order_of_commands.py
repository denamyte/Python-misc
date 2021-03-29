vowels = {'a', 'e', 'i', 'o', 'u'}


def find_apostrophe(word, start):
    i = word.index("'", start)

    if i == -1:
        log("1")
        return -1

    if i == 0:
        log("2")
        return find_apostrophe(word, 1)

    elif i == len(word) - 1:
        log("3")
        return -1

    else:
        previous_char = word[i - 1]
        if previous_char in set(vowels):
            log("4")
            return i

        else:
            log("5")
            return find_apostrophe(word, i + 1)


def log(s: str):
    print(s, end='')


correct_index = find_apostrophe("'w'ord'", 0)