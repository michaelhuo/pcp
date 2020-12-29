def find_low_index(arr, key):
 #TODO: Write - Your - Code
  size = len(arr)
  if size < 1:
    return -1
  low, high = 0, size - 1
  while low < high:
    mid = low + (high - low) // 2
    if arr[mid] < key:
      low = mid + 1
    else:
      high = mid
  if low < size and arr[low] == key:
    while low > 0 and arr[low - 1] == key:
      low -= 1
    return low
  return -1

def find_high_index(arr, key):
  #TODO: Write - Your - Code
  size = len(arr)
  if size < 1:
    return -1
  low, high = 0, size - 1
  while low < high:
    mid = low + (high - low) // 2
    if arr[mid] < key:
      low = mid + 1
    else:
      high = mid
  if low < size and arr[low] == key:
    while low < size - 1 and arr[low + 1] == key:
      low += 1
    return low
  return -1

