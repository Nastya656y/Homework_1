def steps():
    count = input("Какое число ходов сделает Пётр? ")
    try:
        count = int(count)
    except ValueError:
        print("Введено некорректное значение.")
        steps()
    return count


coordinates = [0, 0]

def make_descision():
    descision = input("Выберите направление (вверх, вниз, лево, право): ").lower()
    if not descision in ["вверх", "вниз", "влево", "вправо"]:
        print("Введено некорректное значение.")
        make_descision()
    return descision

for step in range(steps()):
    descision = make_descision()
    if descision == "вверх":
        coordinates[1] += 1
    elif descision == "вниз":
        coordinates[1] -= 1
    elif descision == "влево":
        coordinates[0] -= 1
    elif descision == "вправо":
        coordinates[0] += 1

print(f'Чтобы добраться в точку ({coordinates[0]}, {coordinates[1]}) кратчайшим путём, Петру достаточно было сделать шагов: {sum(abs(i) for i in coordinates)} .')
        