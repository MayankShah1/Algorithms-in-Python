import random

def birthday_paradox(num_people):
    birthdays = []
    for i in range(num_people):
        birthdays.append(random.randint(1,365))
    birthday_clash = num_people - len(set(birthdays)) + 1
    print('probability : ',birthday_clash/num_people)
    if (birthday_clash / num_people) > 0.5:
        return True
    return False

for i in range(5,101,5):
    print('no of people : ',i, 'paradox ? : ',birthday_paradox(i))