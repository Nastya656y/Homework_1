variable_name = input("Введите имя переменной: ")


def correct_variable_name(variable_name):
    variable_name = variable_name.replace("-", "_")
    
    variable_name = variable_name.replace(" ", "_")

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    variable_name_list = list(variable_name)
    for i in range(len(variable_name_list)):
        if variable_name_list[i] in upper:
            variable_name_list[i] = "_" + variable_name[i].lower()
    variable_name = "".join(variable_name_list)
            
    while "__" in variable_name:
        variable_name = variable_name.replace("__", "_")
    
    while variable_name[0] == " " or variable_name[0] == "_" or variable_name[0].isdigit():
        variable_name = variable_name[1:]
    
    while variable_name[-1] == " " or variable_name[-1] == "_":
        variable_name = variable_name[:-1]

    symbols = "abcdefghijklmnopqrstuvwxyz0123456789_"
    for symbol in variable_name:
        if symbol not in symbols:
            return "Введено некорректное имя переменной"

    return variable_name


print(correct_variable_name(variable_name))
