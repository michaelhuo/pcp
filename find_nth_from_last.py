def find_nth_from_last(head, n):
  #TODO: Write - Your - Code
  node = head
  while n > 0 and node:
    node = node.next
    n -= 1
  if not node:
    return None
  node2 = head
  while node:
    node =  node.next
    node2 = node2.next
  return node2
