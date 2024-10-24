equipement = [
    'меч',
    'лук',
    'топор',
    'щит',
    'зелье'
]

print(f'Ассортимент:\n{";\n".join(equipement)}.')

choices = []

def make_choice(n):
    choice_list = input(f'Авантюрист {n}, выберите от 1 до 3 предметов. Напишите их названия через пробел: ').lower().split()
    for choice in choice_list:
        if not choice in equipement:
            print(f'Такого предмета "{choice}" нет в нашем ассортименте.')
            make_choice(n)
    return choice_list

for venturer in range(3):
    choices.append(make_choice(venturer + 1))

count = 0
for item in equipement:
    if any(item in choice for choice in choices[0]) and any(item in choice for choice in choices[1]) and any(item in choice for choice in choices[2]):
        count += 1


print(count)