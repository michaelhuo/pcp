def reverse_even_nodes(head):
  #TODO: Write - Your - Code
  if not head or not head.next:
    return head
  odd_head = head
  even_head = head.next
  node = even_head.next
  is_even = False
  even_tail = even_head
  even_node = even_head
  odd_node = odd_head
  while node:
    if is_even:
      even_node.next = node
      even_node = even_node.next
    else:
      odd_node.next = node
      odd_node = odd_node.next
    is_even = not is_even
    node = node.next
  even_node.next = None
  odd_node.next = None
  node = even_head
  prev = None
  while node:
    tmp = node.next
    node.next = prev
    prev = node
    node = tmp
  even_head = prev

  is_even = True
  head = odd_head
  node = head
  even_node = even_head
  odd_node = odd_head.next

  while even_node or odd_node:
    if is_even and even_node:
      node.next = even_node
      even_node = even_node.next
      node = node.next
      is_even = not is_even
    elif not is_even and odd_node:
      node.next = odd_node
      odd_node = odd_node.next
      node = node.next
      is_even = not is_even

  if even_node:
    node.next = even_node
    even_node = even_node.next
    node = node.next
  if odd_node:
    node.next = odd_node.next
    odd_node = odd_node.next
    node = node.next
  if node:
    node.next = None

  return head
