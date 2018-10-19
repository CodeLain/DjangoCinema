import math


def interpolation_search(array, searched_number, start, end):
    pos = math.ceil(start + ((end - start) / (array[end] - array[start]) * (searched_number - array[start])))

    if searched_number < array[start] or searched_number > array[end]:
        return False

    elif array[pos] == searched_number:
        return True

    elif searched_number > array[pos]:
        return interpolation_search(array, searched_number, pos, end)

    else:
        return interpolation_search(array, searched_number, start, pos)



if __name__ == '__main__':
    some_list = [2, 6, 99, 100, 242, 654]

    print(interpolation_search(some_list, 2, 0, len(some_list)-1))
