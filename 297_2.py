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
        if not root:
            return ""
        stack = []
        node = root
        ans = []
        while node or stack:
            if node:
                ans.append(str(node.val))
                stack.append(node)
                node = node.left
                if not node:
                    ans.append('null')
            else:
                node = stack.pop()
                node = node.right
                if not node:
                    ans.append('null')
        print(ans)
        return ",".join(ans)
    
            
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        dummy = TreeNode(0)
        nums = data.split(',')
        stack = []
        node = dummy
        is_left = True
        is_right = False
        for snum in nums:
            if snum != 'null':
                num = int(snum)
                if is_left:
                    node.left = TreeNode(num)
                    stack.append(node)
                    node = node.left
                else:
                    node.right = TreeNode(num)
                    node = node.right
                    is_left = True
            else:
                if is_left:
                    is_left = False
                else:
                    node = stack.pop()
        return dummy.left
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
