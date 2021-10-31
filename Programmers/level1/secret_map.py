# 비밀지도

def solution(n, arr1, arr2):
    arr1 = [ format(bin(a)[2:]).zfill(n) for a in arr1 ]
    arr2 = [ format(bin(a)[2:]).zfill(n) for a in arr2 ]
    result = []

    for a, b in zip(arr1, arr2):
        string = ''
        for i in range(n):
            if a[i] == '1' or b[i] == '1':
                string += '#'
            else: string += ' '
        result.append(string)

    return result

# Test
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))