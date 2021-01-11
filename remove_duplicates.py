def remove_duplicates(head):
  #TODO: Write - Your - Code
  if not head:
    return head
  keys = set()
  result = head
  keys.add(result.data)
  curr = result
  node = result.next
  while node:
    data = node.data
    print(keys)
    if data not in keys:
      keys.add(data)
      curr.next = node
      curr = curr.next
    node = node.next
  curr.next = None
  return result
  
