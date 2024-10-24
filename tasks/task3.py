person = ['Энакин Скайуокер',
		  41,
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]


def task1():
    name = person[0].split()
    return f'{name[1]}, {name[0]}'

def task2():
    return person[1]

def task3():
    return ', '.join(person[2])

def task4():
    return len(person[2])

def task5():
    return 'Звезда Смерти' in person[2]

def task6():
    return person[3].get('световой меч')

def task7():
    person[1] = 42
    return task2()

def task8():
    if not 'Эндор' in person[2]:
        person[2].append('Эндор')
    return task3()

def task9():
    if person[3].get('ранг') == 'лорд ситхов':
        return 'Энакин - лорд ситхов'
    else:
        return 'Энакин - джедай'

def task10():
    if len(person[2]) > 4:
        return 'Энакин побывал во многих местах'
    else:
        return 'Энакин не так много путешествовал'


while True:
    task_number = input("Введите номер задания (выход - 'выход'): ")
    if task_number == 'выход':
        break
    elif task_number in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        if task_number == '1':
            print(task1())
        elif task_number == '2':
            print(task2())
        elif task_number == '3':
            print(task3())
        elif task_number == '4':
            print(task4())
        elif task_number == '5':
            print(task5())
        elif task_number == '6':
            print(task6())
        elif task_number == '7':
            print(task7())
        elif task_number == '8':
            print(task8())
        elif task_number == '9':
            print(task9())
        elif task_number == '10':
            print(task10())
    else:
        print("Такого задания не существует.")
