def swap(arr, x, y)
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp
end

def permute(arr, s, e)
  if s == e
    p arr
  else
    for i in s..e
      swap(arr, s, i)
      permute(arr, s+1, e)
      swap(arr, s, i)
    end
  end
end

permuate([1, 2, 3], 0, 2)
