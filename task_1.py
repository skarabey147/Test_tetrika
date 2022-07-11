def task(array):
    lst = list(array)
    left = 0
    right = len(lst) - 1
    while (right - left) > 1:
        mid = (left + right) // 2
        if lst[mid] == '0':
            right = mid
        else:
            left = mid
    if lst[right] == '1':
        return 'В массиве нет нулей!'
    return right


if __name__ == '__main__':
    print(task("1111111000000000"))
