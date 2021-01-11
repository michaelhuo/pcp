# Node indices starts from 1.
def swap_nth_node(head, n):
  #TODO: Write - Your - Code
  if not head or n < 1:
    return head
  prev = head
  while n > 2 and prev.next:
    prev = prev.next
    n -= 1 
  if not prev.next:
    return head
  tmp = head.next
  curr = prev.next
  head.next = curr.next
  prev.next = head
  curr.next = tmp

  return curr
