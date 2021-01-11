def delete_node(head, key):
  #TODO: Write - Your - Code
  if not head:
    return head
  dummy = LinkedListNode(-1)
  dummy.next = head
  prev = dummy
  node = dummy.next
  while node:
    if node.data != key:
      prev.next = node
      prev = prev.next
    node = node.next
  prev.next = None
  return dummy.next
