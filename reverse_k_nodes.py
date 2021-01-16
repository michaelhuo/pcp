def reverse_k_nodes(head, k):
   #TODO: Write - Your - Code
   def helper(head, k = 0):
      if not head:
         return head, None, None
      prev = None
      node = head
      tail = head
      count = 0
      while node:
         tmp = node.next
         node.next = prev
         prev = node
         node = tmp
         count += 1
         if count == k:
            break
      return prev, tail, node  
      
   if not head or k <= 1:
      return head
   size = 0
   node = head
   while node:
      node =  node.next
      size += 1
   if k >= size:
      head, tail, node = helper(head, k)
      return head
   node = head
   dummy = LinkedListNode(-1)
   prev = dummy
   while node:
      tmp, tail, node = helper(node, k)
      prev.next = tmp
      prev = tail
   head = dummy.next
   return head 
