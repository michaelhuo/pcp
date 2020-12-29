def move_zeros_to_left(A):
  #TODO: Write - Your - Code
  if not A:
    return
  size = len(A)
  count = sum([1 for i in A if i == 0])
  if count == 0 or count == size:
    return
  read, write = size - 1, size - 1
  index = size - 1
  while index > 0 and A[index] != 0:
    index -= 1
  if index == 0:
    return
  write = index
  read = index - 1
  while count > 0 and read >= 0 and write >=0:
    if A[read] == 0:
      count -= 1
    else:
      A[write] = A[read]
      write -= 1
    read -= 1
  while write >= 0:
    A[write] = 0
    write -= 1
  
