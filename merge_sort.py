def merge_sort(head):
  #TODO: Write - Your - Code
  def find_premid(head):
    if not head:
      return head
    slow = head
    prev = None
    if not slow.next:
      return None
    fast = slow.next
    while fast and fast.next and slow and slow.next:
      prev = slow
      fast = fast.next.next
      slow = slow.next
    return prev
  def merge(head1, head2):
    if not head2:
      return head1
    elif not head1:
      return head2
    display(head1)
    display(head2)
    dummy = LinkedListNode(-1)
    node = None
    if head1.data < head2.data:
      node = head1
      head1 = head1.next
    else:
      node = head2
      head2 = head2.next
    head = node
    while head1 and head2:
      if head1.data < head2.data:
        node.next = head1
        head1 = head1.next
      else:
        node.next = head2
        head2 = head2.next
      node = node.next
    if head1:
      node.next = head1
    if head2:
      node.next = head2
    return head
  def helper(head):
    if not head:
      return head
    premid = find_premid(head)
    if not premid:
      return head
    head2 = premid.next
    if not head2:
      return head
    premid.next = None
    return merge(helper(head), helper(head2))
  return helper(head)
