def intersect(head1, head2):
  #TODO: Write - Your - Code
  if not head1 or not head2:
    return None
  display(head1)
  display(head2)
  size1, size2 = 0, 0
  node = head1
  while node:
    node = node.next
    size1 += 1
  node = head2
  while node:
    node = node.next
    size2 += 1
  size = 0
  node2 = None
  if size1 < size2:
    node = head2
    node2 = head1
    size = size2 - size1
  else:
    node = head1
    node2 = head2
    size = size1 - size2
  result = None
  for _ in range(size):
    node = node.next
  while node and node2:
    if node == node2:
      if not result:
        result = node
    else:
      result = None
    node = node.next
    node2 = node2.next

  return result
