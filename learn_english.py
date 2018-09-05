#--------------------------------------------------------------Подготовка файла
import random
import re

print('Продолжить обучение или начать заново? +/-')
a = str(input())
value_word = []
value_word_random = []
while True:
    if a == '-':
        input_file = open('engl.txt', 'r+')
        engl = input_file.readlines()
        print('1', engl)

    if a == '+':
        input_file = open('no_learned_word.txt', 'r+')
        engl = input_file.readlines()


    no_learned_words = open('no_learned_word.txt', 'w+')
    learned_words = open('learned_word.txt', 'a+')
    k1 = 20
    x1 = 0
    k2 = 20
    x2 = 0
    x = 0
    k = 20

    engl_word = {}

#----------------------------------------------------------------Вывод значения

    for i in range(x, k, 2):
        print(engl[i]+engl[i+1])
        en = engl[i]
        ru = engl[i+1]
        engl.remove(en)
        engl.remove(ru)
        engl.insert(i, en[0:-1] + '1')
        engl.insert(i+1, ru[0:-1] + '1')
    x = i
    k += 20
    print('------------------------------------------------------------------------------------------------')


# -----------------------------------------------------------Сохранение данных
    st = ' '
    for i in engl:
        if i[-1] != '1':
            no_learned_words.write(i)

        elif i[-1] == '1':
            value_word_random.append(i)
    for i in range(0, 20, 2):
        a = value_word_random[i]
        b = value_word_random[i+1]
        learned_words.write(a[0:-1] + ':' + b[0:-1] + '\n')
    learned_words.close()



#------------------------------------------------------------------ Выученные слова
    for i in range(x1, k1, 2):
        word = engl[i]
        if word[-1] == '1':
            engl_word.update({engl[i][0:-1]: engl[i + 1][0:-1] for i in range(x1, k1, 2)})
    x1 = i
    k1 += 20


#-------------------------------------------------------------------------Проверка

    for key, value in engl_word.items():
        print(value)
        print('Translate')
        trans_word = str(input())
        if trans_word == key:
            print('Well!')

        else:
            while True:
                print('Please try again incorrectly.')
                print(value)
                print('Translate')
                trans_word = str(input())
                if trans_word == key:
                    print('Well!')

                    break
                else:
                    continue

    print('--------------------------------------------------------------------------------------')

# ----------------------------------------------------------------Проверка выученных слов
    print('-----Повторим ранее выученные слова-----')
    engl_word1 = {}
    learned_words = open('learned_word.txt', 'r+')
    learned_words2 = learned_words.readlines()

    random.shuffle(learned_words2)

    learned_words3 = []
    for i in learned_words2:
        learned_words3.append(re.split(r':', i))

    for i in range(len(learned_words3)):
        f = learned_words3[i]
        engl_word1.update({f[0]: f[1][0:-1] for i in range(len(learned_words3))})

    true = 0
    false = 0
    for key, value in engl_word1.items():
        if true < 10:
            print(value)
            print('Translate')
            trans_word1 = str(input())
            if trans_word1 == key:
                print('Well!')
                true += 1
            else:
                while True:
                    print('Please try again incorrectly.')
                    false += 1
                    print(value)
                    print('Translate')
                    trans_word1 = str(input())
                    if trans_word1 == key:
                        print('Well!')
                        true += 1


                        break
                    else:
                        continue

    print('Введено правильно: ' + str(true) + '\n' + 'Введено не правильно: ' + str(false))
    print('Статистика: ' + str(true-false) + ' из ' + str(true))
    break

#--------------




















