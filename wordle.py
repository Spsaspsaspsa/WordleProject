import random

def gadanie(probnyy, spisok, mimo = []):
    print ("Я думаю, загаданное слово — ", probnyy)
    print ("Оцените каждую букву в предложенном слове от 0 до 2:\n0 - этой буквы нет в загаданном слове\n1 - эта буква есть в загаданном слове, но на другой позиции\n2 - эта буква есть в загаданном слове на этой же позиции")
    mark = str(input())
    tochno = {}
    blizko = {}
    for i in range(5):
        if mark[i] == "2":
            tochno[i] = probnyy[i]
        elif mark[i] == "1":
            blizko[i] = probnyy[i]
        else:
            mimo.append(probnyy[i])
    if mark == "22222":
        return "Ура победа"
    else:
        if len(tochno.keys()) != 0:
            variants = []
            for s in spisok:
                sovpadenia = 0
                for i in tochno.keys():
                    if s[i] == tochno[i]:
                        sovpadenia += 1
                if sovpadenia == len(tochno.keys()):
                    variants.append(s)
        else:
            variants = spisok.copy() #если ни одна буква не совпала, на этом этапе подходят все слова
        variants_2 = variants.copy()
        for s in variants:
            for i in blizko.keys():
                if s[i] == blizko[i] and s in variants_2:
                    variants_2.remove(s)
                if blizko[i] not in s and s in variants_2:
                    variants_2.remove(s)
        variants_3 = variants_2.copy()
        for s in variants_2:
            for l in s:
                kolvo_p = s.count(l) #считаем, сколько раз буква встречается в предложенном слове
                kolvo_t = list(tochno.values()).count(l) + list(blizko.values()).count(l) #считаем, сколько раз эта буква ТОЧНО встречается в загаданном слове
                if kolvo_p < kolvo_t and s in variants_3:
                    variants_3.remove(s)
                elif kolvo_p > kolvo_t and l in mimo and s in variants_3:                                                                                                                    
                    variants_3.remove(s)
        print(variants_3)
        if variants_3 == []:
            return str("Я пока не знаю такого слова")
        else:
            return gadanie(variants_3[0], variants_3, mimo)
            
        
with open("слова2.txt", "r", encoding = "utf-8") as f:
    n = random.randint(1, 2380)
    lines = f.readlines()
    spisok = list() #для всех слов без частот
    for line in lines:
        spisok.append(line.strip().split("\t")[0])
    probnyy = spisok[n] #первое случайное пробное слово 
    print(gadanie(probnyy, spisok))
