import random

WORD_LENGTH = 5

# random.seed(1123)


def is_suitable(test, mark, word):
    for i in range(WORD_LENGTH):
        if mark[i] == "1" and test[i] == word[i]:
            return False
        if mark[i] == "2" and test[i] != word[i]:
            return False

    zero_letters = dict()
    non_zero_letters = dict()
    for i in range(WORD_LENGTH):
        if mark[i] == '0':
            zero_letters[test[i]] = zero_letters.get(test[i], 0) + 1
        else:
            non_zero_letters[test[i]] = non_zero_letters.get(test[i], 0) + 1
    for i in range(WORD_LENGTH):
        if word[i] in non_zero_letters and non_zero_letters[word[i]] > 0:
            non_zero_letters[word[i]] -= 1
        elif word[i] in zero_letters:
            return False
    for cnt in non_zero_letters.values():
        if cnt > 0:
            return False
    return True


def play(word_list):
    while len(word_list) > 1:
        test = random.choice(word_list)
        print("Я думаю, загаданное слово — ", test)
        print("Оцените каждую букву в предложенном слове от 0 до 2:\n"
              "0 - этой буквы нет в загаданном слове\n"
              "1 - эта буква есть в загаданном слове, но на другой позиции\n"
              "2 - эта буква есть в загаданном слове на этой же позиции")
        mark = input()
        word_list = list(filter(lambda word: is_suitable(test, mark, word), word_list))
    if len(word_list) == 0:
        print("Я пока не знаю такого слова")
    else:
        print("Загаданное слово — ", word_list[0])


with open("word_list.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    word_list = list()  # для всех слов без частот
    for line in lines[1:]:
        word_list.append(line.strip().split("\t")[0])
    play(word_list)