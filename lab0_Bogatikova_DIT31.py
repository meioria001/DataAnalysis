def task0():
    import pandas as pd

    music = [
        ['Three Days Grace', 'Never Too Late'],
        ['Breaking Benjamin', 'Anthem of the Angels'],
        ['Saint Asonia', 'Left Behind'],
        ['Nickelback', 'Song on Fire'],
        ['Ed Sheeran', 'Photograph']
    ]

    music_columns = ['artist', 'track']
    music_table = pd.DataFrame(data=music, columns=music_columns)

    print(music_table)
    print()


def task1():
    n = "0"
    while True:
        name = input("Введите своё имя или введите 0 для завершения работы: ")

        if name == n:
            print("Сеанс будет завершён")
            print()
            break
        else:
            print(f"Привет, {name}")
            print()


def task2():
    n = 0
    while True:
        age = int(input("Введите ваш возраст или введите 0 для завершения работы: "))

        if age == n:
            print("Сеанс будет завершён")
            print()
            break
        else:
            if age >= 18:
                print("Доступ разрешён")
                print()
            elif 14 <= age <= 17:
                print("Доступ ограничен")
                print()
            else:
                print("Доступ запрещён")
                print()


def task3():
    n = "0"
    while True:
        phrase = input("Введите текстовую фразу или введите 0 для завершения работы программы: ")
        if phrase == n:
            print("Сеанс будет завершён")
            break
        else:
            repeats = int(input("Введите количество повторений: "))

            for i in range(repeats):
                print(phrase)
            print()


def task4():
    n = "0"
    while True:
        phrase = input("Введите текстовую фразу или введите 0 для завершения работы программы: ")
        if phrase == n:
            print("Сеанс будет завершён")
            break
        else:
            repeats = int(input("Введите количество повторений: "))

            i = 0
            while i < repeats:
                print(phrase)
                i += 1
            print()


def task5():
    def print_fio(arg_surname, arg_name, arg_patronymic):
        print(arg_name[0], arg_surname[0], arg_patronymic[0], sep='')
        return

    n = "0"
    while True:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")

        if surname == n or name == n or patronymic == n:
            print("Сеанс будет завершён")
            print()
            break
        else:
            print_fio(name, surname, patronymic)
            print()


def task6():
    import pandas as pd

    data = {
        'col1': ['Я', 'Python', 'Буду'],
        'col2': ['люблю', 'мой', 'стараться'],
        'col3': ['анализ', 'лучший', 'хорошо'],
        'col4': ['данных', 'друг', 'учиться']
    }

    df = pd.DataFrame(data)
    print(df)
    print()


num = "none"
while True:
    task = input("Введите номер задания для проверки (либо введите none для завершения работа программы): ")
    if task == num:
        print("Сеанс будет завершён.")
        break
    else:
        if task == "0":
            task0()
        elif task == "1":
            task1()
        elif task == "2":
            task2()
        elif task == "3":
            task3()
        elif task == "4":
            task4()
        elif task == "5":
            task5()
        elif task == "6":
            task6()
        else:
            print("Выбранного задания не существует. Повторите попытку ввода снова.")
            print()
            continue
