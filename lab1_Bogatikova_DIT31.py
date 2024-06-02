import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None


def task1():
    df = pd.read_csv('../Data_Analysis_Tasks/datasets/Titanic.csv')
    print(df.head(10))
    print()

    columns = list(df.columns)
    print('Столбцы в приведённом датасете: ', end='')
    for i in columns:
        if i != columns[-1]:
            print(i, end=', ')
        else:
            print(i, end='.')
    print()

    print()
    print('Типы данных столбцов датасета: ')
    print(df.dtypes)

    shape = list(df.shape)
    print()
    print(f'Количество строк: {shape[0]}')
    print(f'Количество столбцов: {shape[1]}')
    print()

    women = df.loc[df['Sex'] == 'female']
    print('-' * 200)
    print(f'Женщины: \n{women}')

    women_life = women.loc[:, 'Survived']
    quantity_women = women_life.loc[women_life == 1].count()
    print(f'Общее количество мужчин: {len(women_life)}')
    print(f'Количество выживших женщин равно {quantity_women}')
    quantity_women_percentage = quantity_women / len(women_life) * 100
    print(f'Процент выживших женщин: {round(quantity_women_percentage, 1)}%')
    print('-' * 200)

    men = df.loc[df['Sex'] == 'male']
    print(f'Мужчины: \n{men}')

    men_life = men.loc[:, 'Survived']
    quantity_men = men_life.loc[men_life == 1].count()
    print(f'Общее количество мужчин: {len(men_life)}')
    print(f'Количество выживших мужчин равно {quantity_men}')
    quantity_men_percentage = quantity_men / len(men_life) * 100
    print(f'Процент выживших мужчин: {round(quantity_men_percentage, 1)}%')


def task2():
    df = pd.read_csv('../Data_Analysis_Tasks/datasets/student-mat.csv')
    print(df.head(10))
    print()

    shape_table = list(df.shape)
    print(f'Размеры таблицы: {shape_table[0]} x {shape_table[1]}')

    observations_table = shape_table[0]
    print()
    print(f'Количество наблюдений: {observations_table}')

    print()
    print(df.info())

    observations_info_table = 395
    print()
    if shape_table[0] == observations_info_table:
        print('Решение верно, количество наблюдений равно.')
        print()
    else:
        print('Решение неверно, проверьте ещё раз!')
        print()

    print('Таблица, состоящая из столбцов Medu и Fedu')
    parents = df.loc[:, 'Medu': 'Fedu']
    print(parents.head(10))
    print()

    m_edu = list(df.loc[:, 'Medu'].head(10))
    mother_hight = 0
    for i in m_edu:
        if i == 4:
            mother_hight += 1
        else:
            continue
    print(f'Число матерей с высшим образованием равно {mother_hight}')

    f_edu = list(df.loc[:, 'Fedu'].head(10))
    father_hight = 0
    for j in f_edu:
        if j == 4:
            father_hight += 1
        else:
            continue
    print(f'Число отцов с высшим образованием равно {father_hight}')

    if mother_hight > father_hight:
        print('Победители: матери')
        print()
    else:
        print('Победители: отцы')
        print()


num = "none"
while True:
    task = input("Введите номер задания для проверки (либо введите none для завершения работа программы): ")
    if task == num:
        print("Сеанс будет завершён.")
        break
    else:
        if task == "1":
            task1()
        elif task == "2":
            task2()
        else:
            print("Выбранного задания не существует. Повторите попытку ввода снова.")
            print()
            continue

