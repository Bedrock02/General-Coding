def quicksort(a):
  if a ==[]:
    return []
  pivot = a[0]
  left = [x for x in a if x < pivot]
  right = [x for x in a[1:] if x >=pivot]
  
  return quicksort(left) + [a[0]] + quicksort(right)
