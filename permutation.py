def swap(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp

def permute(arr, s, e):
    if(s == e):
        print(arr)

    else:
        for i in range(s, e):
            swap(arr, s, i)
            permute(arr, s+1, e)
            swap(arr, s, i)

permute([1,2,3], 0, 3)
