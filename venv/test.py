my_file = open("C:/Users/Настя/PycharmProjects/untitled/eng.txt", 'r')

eng_row = my_file.readlines()
print(eng_row)
key = []
rus_word = []
for i in eng_row:
    if i[-1] == "\n" :
        key.append(i)
        eng_row.remove()

print(eng_row)
print(key)


