WORD_LENGTH = 5


def read_word_list(filename: str = "word_list.tsv") -> list[str]:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip().split('\t')[0] for line in lines[1:]]


def is_suitable(test: str, mark: str, word: str) -> bool:
    for i in range(WORD_LENGTH):
        if mark[i] == "1" and test[i] == word[i]:
            return False
        if mark[i] == "2" and test[i] != word[i]:
            return False

    zero_letters = {}
    non_zero_letters = {}

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

    return all(cnt == 0 for cnt in non_zero_letters.values())


def play(word_list: list[str]) -> None:
    while len(word_list) > 1:
        test = word_list[0]
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


if __name__ == "__main__":
    word_list = read_word_list()
    play(word_list)
