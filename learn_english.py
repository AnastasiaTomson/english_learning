import random
import os


def cls():
    os.system('clear')


def read_file(file_name):
    input_file = open(file_name, 'r', encoding='utf-8-sig')
    return input_file.readlines()


def write_file(file_name):
    input_file = open(file_name, 'w', encoding='utf-8-sig')
    return input_file


def answer(learn_now):
    print('Готовы проверить свои знания?\nЕсли готовы, нажмите Enter')
    true = 0
    if input() == '':
        cls()
        for key, val in sorted(learn_now.items(), key=lambda x: random.random()):
            print('Переведите: {}'.format(val))
            count = 0
            word = ''
            while word != key:
                word = str(input()).lower()
                print('Ответ: {}'.format(word))
                if word == key:
                    true += 1
                    print('ВЕРНО!)')
                    learning = write_file('learning.txt')
                    learning.write('{}-{}\n'.format(key, val))
                else:
                    count += 1
                    print('Не верно. Попробуйте еще раз!')
                if count >= 5:
                    print('Показать ответ? Если да, нажмите Enter.')
                    if input() == '':
                        not_learning = write_file('not_learning.txt')
                        not_learning.write('{}-{}\n'.format(key, val))
                        print('Ответ: {}'.format(key))
                        word = key
    return true


def show_words(words):
    learn_now = dict()
    for i, (key, val) in enumerate(sorted(words.items(), key=lambda x: random.random())):
        if i == 10:
            break
        print(key + ': ' + val)
        learn_now[key] = val
        words.pop(key)
    return answer(learn_now)


def main():
    while True:
        print('Если Вы хотите продолжить обучение нажмите +\nЕсли Вы хотите начать заново нажмите -')
        a = str(input())
        if a == '-':
            file_name = 'english.txt'
        elif a == '+':
            file_name = 'not_learning.txt'
        else:
            break
        en = read_file(file_name)
        en_word = {}

        while len(en) != 2:
            row_list = en[0].split('-')
            en_word[row_list[0].replace('\n', '').lower()] = row_list[1].replace('\n', '').lower()
            en.remove(en[0])
        true = show_words(en_word)

        print('Введено правильно: {}\nВведено не правильно: {}'.format(true, 10-true))
        print('Статистика: {} из {}'.format(true, 10))


if __name__ == '__main__':
    main()
