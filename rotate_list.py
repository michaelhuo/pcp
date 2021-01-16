def rotate_list(head, n):
  #TODO: Write - Your - Code
  if not head or n == 0:
    return head
  size = 0
  node = head
  prev = None
  while node:
    size += 1
    prev = node
    node = node.next
  offside = size - n % size - 1
  tail = prev
  node = head
  while offside > 0:
    node = node.next
    offside -= 1
  tail.next = head
  head = node.next
  node.next = None  
  return head
