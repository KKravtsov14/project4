# Задача программы - редактировать текст

# Функция, заменяющая символ в строке на другой
# и обратную замену символов
def replacement(
        str_ex,
        str_1,
        str_2,
        str_3,
        num_step,
        num_step_reserve,
        ans_register,
        ans_reverse):

    """

    :param str_ex:
    :param str_1:
    :param str_2:
    :param str_3:
    :param num_step:
    :param num_step_reserve:
    :param ans_register:
    :param ans_reverse:
    :return:
    """

# В функцию вводятся: исходная строка
# символы, с которыми она будет работать
# шаги, через которые будет замена символов
# указания, будет ли работать обратная замена
# и замена разного регистра

    k = 0
    c = 0

    for i in range(0, len(str_1)):
        if str_1[i].lower() == str_2.lower():
            if ans_register.lower() == 'да':
                k += 1
                if k % num_step == 0:
                    str_ex += str_3
                    k = 0
                else:
                    str_ex += str_1[i]

            else:
                if str_1[i] == str_2:
                    k += 1
                    if k % num_step == 0:
                        str_ex += str_3
                        k = 0
                    else:
                        str_ex += str_1[i]
                else:
                    str_ex += str_1[i]

        elif ans_reverse.lower() == 'да':
            if str_1[i].lower() == str_3.lower():
                if ans_register.lower() == 'да':
                    c += 1
                    if c % num_step_reserve == 0:
                        str_ex += str_2
                        c = 0
                    else:
                        str_ex += str_1[i]

                else:
                    if str_1[i] == str_3:
                        c += 1
                        if c % num_step_reserve == 0:
                            str_ex += str_2
                            c = 0
                        else:
                            str_ex += str_1[i]

            else:
                str_ex += str_1[i]
        else:
            str_ex += str_1[i]

    print(str_ex)


# Функция, записывающая заданный символ
# перед определенным символом в строке
def before(
        str_ex,
        str_1,
        str_2,
        str_3,
        num_step):

    """

    :param str_ex:
    :param str_1:
    :param str_2:
    :param str_3:
    :param num_step:
    :return:
    """

# В функцию вводятся: исходная строка
# символы, с которыми она будет работать
# шаги, через которые будет замена символов

    k = 0
    for i in range(len(str_1) - 1):
        if str_1[i + 1] == str_2:
            k += 1
            if k == num_step:
                str_ex += str_1[i]
                str_ex += str_3
                k = 0
            else:
                str_ex += str_1[i]

        else:
            str_ex += str_1[i]

    str_ex += str_1[len(str_1) - 1]
    print(str_ex)


# Функция, записывающая заданный символ
# после определенного символа в строке
def after(
        str_ex,
        str_1,
        str_2,
        str_3,
        num_step):

    """

    :param str_ex:
    :param str_1:
    :param str_2:
    :param str_3:
    :param num_step:
    :return:
    """

# В функцию вводятся: исходная строка
# символы, с которыми она будет работать
# шаги, через которые будет замена символов

    k = 0
    for i in range(len(str_1)):
        if str_1[i] == str_2:
            k += 1
            if k == num_step:
                str_ex += str_1[i]
                str_ex += str_3
                k = 0
            else:
                str_ex += str_1[i]

        else:
            str_ex += str_1[i]

    print(str_ex)


# Функция, удаляющая заданный символ
def remove(
        str_ex,
        str_1,
        str_2,
        num_step):

    """

    :param str_ex:
    :param str_1:
    :param str_2:
    :param num_step:
    :return:
    """

# В функцию вводятся: исходная строка
# символы, с которыми она будет работать
# шаги, через которые будет замена символов

    k = 0
    for i in range(len(str_1)):
        if str_1[i] == str_2:
            k += 1
            if k != num_step:
                str_ex += str_1[i]
            else:
                k = 0
        else:
            str_ex += str_1[i]

    print(str_ex)


# Главная функция, объединяющая остальные
def main(str_1):

    """

    :param str_1:
    :return:
    """

    str_ex = ''

# В зависимости от задачи нужно выьрать разные функции

    print('Что нужно сделать?')
    print('1. Вписывать символ перед определенным символом')
    print('2. Вписывать символ после определенного символа ')
    print('3. Заменять один символ другим')
    print('4. Удалять символ из строки')
    ans = str(input())

    while not ans.isdigit():
        print('Ошибка: выберете вариант ответа')
        ans = str(input())

    ans_int = int(ans)

    if ans_int == 1:
        str_2 = str(input('Перед каким символом вписывать символ?'))

        while len(str_2) != 1:
            print('Ошибка: введите единственный символ')
            str_2 = str(input())

        str_3 = str(input('Какой символ вписать?'))
        num = str(input('Перед каким по счету символом?'))

        while not num.isdigit():
            print('Ошибка: введите верное число')
            num = str(input())

        num_step = int(num)

        before(str_ex, str_1, str_2, str_3, num_step)

    elif ans_int == 2:
        str_2 = str(input('После какого символа вписывать символ?'))

        while len(str_2) != 1:
            print('Ошибка: введите единственный символ')
            str_2 = str(input())

        str_3 = str(input('Какой символ вписать?'))
        num = str(input('Перед каким по счету символом?'))

        while not num.isdigit():
            print('Ошибка: введите верное число')
            num = str(input())

        num_step = int(num)

        after(str_ex, str_1, str_2, str_3, num_step)

    elif ans_int == 4:
        str_2 = str(input('Какой символ нужно удалять?'))

        while len(str_2) != 1:
            print('Ошибка: введите единственный символ')
            str_2 = str(input())

        num = str(input('Какой по счету символ удалять?'))

        while not num.isdigit():
            print('Ошибка: введите верное число')
            num = str(input())

        num_step = int(num)

        remove(str_ex, str_1, str_2, num_step)

    else:
        str_2 = str(input('Какой символ заменять?'))

        if len(str_2) == 1 and (64 < ord(str_2) < 122 or 1039 < ord(str_2) < 1104):
            ans_register = str(input('Заменять любой регистр?'))
        else:
            ans_register = 'нет'

        while len(str_2) != 1:
            print('Ошибка: введите единственный символ')
            str_2 = str(input())

        str_3 = str(input('Какой символ вписать?'))

        if len(str_3) == 1:
            ans_reverse = str(input('Делать обратную замену?'))
        else:
            ans_reverse = 'нет'

        if ans_reverse.lower() == 'да':
            num_reverse = str(input('С какой частотой делать обратную замену?'))
            while not num_reverse.isdigit():
                num_reverse = str(input('Ошибка: введите целое число'))
            num_step_reserve = int(num_reverse)
        else:
            num_step_reserve = 0

        num = str(input('Какой по счету символ заменять?'))

        while not num.isdigit():
            print('Ошибка: введите верное число')
            num = str(input())

        num_step = int(num)

        replacement(
            str_ex,
            str_1,
            str_2,
            str_3,
            num_step,
            num_step_reserve,
            ans_register,
            ans_reverse)


# Начало работы программы

str_1 = str(input('Введите строку, которую нужно изменить'))
main(str_1)