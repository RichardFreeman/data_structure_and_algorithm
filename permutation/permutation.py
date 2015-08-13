def swap(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp

def permute0(arr, s, e):
    if(s == e):
        print(arr)
    else:
        for i in range(s, (e+1)):
            swap(arr, s, i)
            permute(arr, s+1, e)
            swap(arr, s, i)


# only for Python3, subgenertor
def permute1(arr, s, e):
    if(s == e):
        yield arr
    else:
        for i in range(s, (e+1)):
            swap(arr, s, i)
            yield from permute(arr, s+1, e)
            swap(arr, s, i)
