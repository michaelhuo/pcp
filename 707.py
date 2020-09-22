class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:
    
    def __init__(self, val = -1):
        """
        Initialize your data structure here.
        """
        if val == -1:
            self.head = self.tail = None
        else:
            self.head = Node(val)
            self.tail = self.head
        # self.print()
        
    def print(self):
        
        pass
    
        cur = self.head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        print ("---")
        print(l)            
        if l:
            print("head: {}, tail: {}".format(self.head.val, self.tail.val))

        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or not self.head:
            return -1
        i = index
        cur = self.head
        while i > 0 and cur.next:
            cur = cur.next
            i -= 1
        if i > 0:
            return -1
        return cur.val
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if val < 0:
            return
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = Node(val, self.head)
            self.head.prev = node
            self.head = node
            
        # self.print()
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if val < 0:
            return
        if not self.tail:
            self.addAtHead(val)
            return
        
        node = Node(val, None, self.tail)
        self.tail.next = node
        self.tail = node
        
        # self.print()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or val < 0:
            return
        if not self.head and index != 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        i = index
        cur = self.head
        prev = cur
        while i > 0 and cur.next:
            prev = cur
            cur = cur.next
            i -= 1
        if i > 1:
            return
        if i == 1:
            self.addAtTail(val)
            return

        node = Node(val, cur, prev)
        prev.next = node
        cur.prev = node
        
        # self.print()
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or not self.head:
            return
        if index == 0:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = self.tail = None
            return
        
        i = index
        cur = self.head
        prev = cur
        while i > 0 and cur.next:
            prev = cur
            cur = cur.next
            i -= 1
        if i > 0:
            return
        
        if cur == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = cur.next
            cur.next.prev= prev
            
        # self.print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
