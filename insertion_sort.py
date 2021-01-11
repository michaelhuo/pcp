def insertion_sort(head):
  #TODO: Write - Your - Code
    if not head:
        return head
    node = head
    dummy = LinkedListNode(-1)
    while node:
        tmp = node.next
        data = node.data
        curr = dummy
        prev = None
        while curr and curr.data < data:
            prev = curr
            curr = curr.next
        prev.next = node
        node.next = curr
        node = tmp
    return dummy.next
