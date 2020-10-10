# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def _serialize(root: 'TreeNode') -> List[str]:
            if not root:
                return None
            ans = [str(root.val)]
            if root.left:
                left = _serialize(root.left)
            else:
                left = ['#']
            if root.right:
                right = _serialize(root.right)
            else:
                right = ['#']
            ans = ans + left + right
            
            return ans
        if not root:
            return '#'
        ans = _serialize(root)
        #print(ans)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _deserialize(data: List[str]) -> 'TreeNode': 
            if not data:
                return None
            val_str = data.pop()
            # print(val_str)
            if val_str == "#":
                return None
            val = int(val_str)
            node = TreeNode(val)
            node.left = _deserialize(data)
            node.right = _deserialize(data)
            return node
        
        #print(data)
        input_list = str(data).split(',')
        input_list.reverse()
        #print(input_list)
        root = _deserialize(input_list[:])
        return root
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
