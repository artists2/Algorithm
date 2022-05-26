def sum_arr(n, arr1, arr2):
    r = []
    for i in range(n):
        s = ''
        for j in range(n):
            tmp = int(arr1[i][j]) | int(arr2[i][j])
            if tmp:
                s += '#'
            else:
                s += ' '
        r.append(s)
    return r


def decryption(arr, n):
    result = []
    for number in arr:
        f = str(format(number, 'b')).zfill(n)
        result.append(f)
    return result


def solution(n, arr1, arr2):
    arr1 = decryption(arr1, n)
    arr2 = decryption(arr2, n)
    return sum_arr(n, arr1, arr2)

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# "#####",
# "# # #", 
# "### #", 
# "# ##", 
# "#####"]