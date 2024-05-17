#словарь популярных лемм русского языка 2.0
nouns = []
five_let = dict()

with open('pop_let.txt', encoding='utf8') as let:
  pop_let_spisok = let.read().split()

b = 9
c = 10
while c<len(pop_let_spisok):
  let_dict[pop_let_spisok[b]] = int(pop_let_spisok[c])
  b+=4
  c+=4

with open('freqrnc2011.csv', encoding='utf8') as f:
  lem_dict = f.read().split('\t')

a = 6
while a<len(lem_dict):
  if lem_dict[a] == 's':
    noun = lem_dict[a-1].split('\n')
    if len (noun[1]) == 5:
      kolvo_let = len(set(noun[1]))
      summa = 0
      for letter in noun[1]:
        summa += let_dict[letter]
      nouns.append([noun[1],summa,kolvo_let])
  a+=5

five_let = sorted(nouns, key = lambda array: (-array[2], -array[1]))

import csv
with open('wordle_dict_5.csv','wt', encoding='utf8') as table:
  csv_writer = csv.writer(table, delimiter='\t')
  csv_writer.writerow(["слово", "сумма частот букв", "кол-во оригинальных букв"])
  for three in five_let:
    csv_writer.writerow (three)
