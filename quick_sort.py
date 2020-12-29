from random import randint

def quick_sort(a):
  
  def helper(a, left, right):
    pivot_index = partition(a, left, right)
    if pivot_index == -1:
      return -1
    helper(a, left, pivot_index - 1)
    helper(a, pivot_index + 1, right)
  def partition(a, left, right):
    if right - left < 1:
      return -1
    if right - left == 2:
      if a[left] > a[right]:
        a[left], a[right] = a[right], a[left]
      return -1
    pivot_index = randint(left, right)
    pivot = a[pivot_index]
    a[pivot_index], a[right] = a[right], a[pivot_index]
    i, j = left, left
    while j < right:
      if a[j] < pivot:
        j += 1
      else:
        break
    if j == right:
      return j
    i = j + 1
    while i < right:
      if a[i] < pivot:
        a[j], a[i] = a[i], a[j]
        j += 1
      i += 1
    a[j], a[right] = a[right], a[j]
    return j
  if not a:
    return None
  size = len(a)
  if size < 2:
    return None
  helper(a, 0, size - 1)




