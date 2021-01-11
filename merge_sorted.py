def merge_sorted(head1, head2):
  #TODO: Write - Your - Code
  if not head2:
    return head1
  elif not head1:
    return head2
  node1 = head1
  node2 = head2
  head = LinkedListNode(-1)
  node = head
  while node1 and node2:
    if node1.data < node2.data:
      node.next = node1
      node1 = node1.next
    else:
      node.next = node2
      node2 = node2.next
    node = node.next
  if node1:
    node.next = node1
  if node2:
    node.next = node2

  return head.next
