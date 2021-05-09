# Задание 4.1
# напишите код для функции sum
def summa(num_list):
    if num_list == []:
        return 0
    return num_list[0] + summa(num_list[1:])


# Задание 4.2
# напишите рекурсивную функцию для подсчёта элементов в списке
def count(num_list):
    if num_list == []:
        return 0
    return 1 + count(num_list[1:])

# Задание 4.3
# найдите наибольшее число в списке
def find_max(num_list):
    if len(num_list) == 2:
        return num_list[0] if num_list[0] > num_list[1] else num_list[1]
    sub_max = find_max(num_list[1:])
    return num_list[0] if num_list[0] > sub_max else sub_max
