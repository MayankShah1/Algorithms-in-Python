import random

def punishment(sentence, number_of_times):
    for i in range(number_of_times):
        sentence_list = list(sentence)
        for j in range(8):
            pos = random.randrange(len(sentence_list))
            sentence_list[pos] = 'x'
        temp = ''.join(sentence_list)
        print(temp)

punishment('I will never spam my friends again.',4)
