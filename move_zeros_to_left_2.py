def move_zeros_to_left(A):
  #TODO: Write - Your - Code
  size = len(A)
  if size < 2:
    return
  read_index, write_index = size - 1, size - 1
  while read_index >= 0:
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1
    read_index -= 1
  while write_index >= 0:
    A[write_index] = 0
    write_index -= 1
