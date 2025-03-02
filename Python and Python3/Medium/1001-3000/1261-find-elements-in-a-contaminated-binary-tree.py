# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        def initializeTree(tree: Optional[TreeNode]):

            if tree is not None and tree.left is not None:
                tree.left.val =  2 * tree.val + 1
                if tree.left.val not in self.hashTable:
                    self.hashTable[tree.left.val] = True
                initializeTree(tree.left)
            if tree is not None and tree.right is not None:
                tree.right.val =  2 * tree.val + 2
                if tree.right.val not in self.hashTable :
                    self.hashTable[tree.right.val] = True
                initializeTree(tree.right)

            

        if(root == None):
            return False
        
        self.hashTable = {}
        self.head = root
        self.head.val = 0 
        self.hashTable[self.head.val] = True

        initializeTree(root)
    
        


    def find(self, target: int) -> bool:
        return True if target in self.hashTable else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)