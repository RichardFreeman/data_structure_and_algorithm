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


# only for Python3, subgenerator
def permute1(arr, s, e):
    if(s == e):
        yield arr
    else:
        for i in range(s, (e+1)):
            swap(arr, s, i)
            yield from permute(arr, s+1, e)
            swap(arr, s, i)

# not accumulator
def permute2(arr):
    if len(arr) == 1:
        yield arr
    else:
        for i in range(len(arr)):
            for perm in permute2(arr[:i] + arr[i+1:]):
                yield [arr[i]] + perm

def permute3(arr, prefix):
    if len(arr) == 1:
        yield arr + prefix
    else:
        for i in range(len(arr)):
            yield from permute3(arr[:i] + arr[i+1:], prefix+[arr[i]])


[x for x in permute1([1,2,3], 0, 2)]
[y for y in permute2([1,2,3])]
[z for z in permute3([1,2,3])]
