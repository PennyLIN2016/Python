# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #Runtime: 64 ms, faster than 13.28% of Python online submissions for Delete Node in a BST.
        s#Memory Usage: 20 MB, less than 6.67% of Python online submissions for Delete Node in a BST.
        if not root: return None
        if root.val==key:
            if not root.right:
                left = root.left
                return left
            else:
                right=root.right
                while right.left:
                    right=right.left
                root.val,right.val=right.val,root.val
        root.left= self.deleteNode(root.left,key)
        root.right= self.deleteNode(root.right,key)
        return root

if __name__ == '__main__':
    object = Solution()
    n1=  TreeNode(5)
    n2=TreeNode(3)
    n3=TreeNode(6)
    n1.left=n2
    n1.right=n3
    n4=TreeNode(2)
    n5=TreeNode(4)
    n6=TreeNode(7)
    n2.left=n4
    n2.right=n5
    n3.right=n6


    k=3

    print(n1.right.val)
    print('---Start---')
    r = object.deleteNode(n1,k)
    print(r)
    print('---End---')


