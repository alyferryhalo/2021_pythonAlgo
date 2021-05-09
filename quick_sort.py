# quick sort

def quick_sort(num_array):
    # базовый случай
    if len(num_array) < 2:
        return num_array
    # рекурсивный случай
    else:
        pvt = num_array[0]  # опорный элемент
        less = [i for i in num_array[1:] if a <= pvt]  #  подмассив элементов, меньших опорного
        greater = [i for i in num_array[1:] if a > pvt]  #  подмассив элементов, больших опорного
        return quick_sort(less) + [pvt] + quick_sort(greater)
