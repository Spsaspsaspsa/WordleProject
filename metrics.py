import wordle
import matplotlib.pyplot as plt


def get_mark(hidden_word: str, test: str) -> str:
    non_zero_letters = {}
    for letter in hidden_word:
        non_zero_letters[letter] = non_zero_letters.get(letter, 0) + 1
    mark = []
    spaces = []
    for i in range(wordle.WORD_LENGTH):
        if test[i] not in hidden_word:
            mark.append('0')
        elif test[i] == hidden_word[i]:
            mark.append('2')
            non_zero_letters[hidden_word[i]] -= 1
        else:
            mark.append(' ')
            spaces.append(i)
    for i in spaces:
        if non_zero_letters[test[i]] > 0:
            mark[i] = '1'
            non_zero_letters[test[i]] -= 1
        else:
            mark[i] = '0'
    return ''.join(mark)


def get_attempts_count(hidden_word: str) -> int:
    variants = wordle.read_word_list()
    n = 0
    while len(variants) > 1:
        test = variants[-1]
        mark = get_mark(hidden_word, test)
        variants = list(filter(lambda word: wordle.is_suitable(test, mark, word), variants))
        n += 1
    if len(variants) == 0 or variants[0] != hidden_word:
        return -1
    else:
        return n


if __name__ == "__main__":
    word_list = wordle.read_word_list()
    # for word in word_list:
    #     n = get_attempts_count(word)
    #     d[n] = d.get(n, 0) + 1
    # print(d)

    d1 = {1: 29, 2: 456, 3: 995, 4: 641, 5: 206, 6: 39, 7: 14}  # если test = variants[0]
    d2 = {3: 897, 4: 734, 2: 315, 5: 295, 1: 22, 6: 83, 7: 22, 8: 12}  # если test = random.choice(variants)
    d3 = {5: 620, 6: 338, 3: 454, 4: 640, 10: 4, 7: 123, 8: 34, 2: 137, 9: 15, 1: 15}  # если test = variants[-1]

    x = d1.keys()
    y = d1.values()
    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    plt.title('Распределение количества попыток')
    plt.show()
