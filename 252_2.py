class TreeNode:
    def __init__(self, start: int = -1, end: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        
class Solution:
    def add_node(self, root: 'TreeNode', start: int, end: int) -> 'TreeNode':
        if not root:
            return TreeNode(start, end)
        node = root
        while node:
            if start <= node.start < end or start < node.end <= end:
                return None
            elif end <= node.start:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(start, end)
                    return node.left
            elif start >= node.end:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(start, end)
                    return node.right
            else:
                return None
                
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        root = TreeNode(intervals[0][0], intervals[0][1])
        for s, e in intervals[1:]:
            node = self.add_node(root, s, e)
            if not node:
                return False
        return True
            
