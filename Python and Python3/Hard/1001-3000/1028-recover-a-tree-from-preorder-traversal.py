# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        def recPreorderTraversal(nodeRec: Optional[TreeNode]):
            
            currentDepth = len(self.splittedPos[0]) - 1
            if len(self.splittedPos) > 2:
                if len(self.splittedPos[0]) == currentDepth + 1:
                    nodeLeft = TreeNode(int(self.splittedPos[1]), None, None)
                    nodeRec.left = nodeLeft
                    if len(self.splittedPos[0]) < len(self.splittedPos[2]):
                        self.splittedPos = self.splittedPos[2:]
                        recPreorderTraversal(nodeRec.left)
                    else: 
                        self.splittedPos = self.splittedPos[2:]
                
                if len(self.splittedPos) > 1:
                    if len(self.splittedPos[0]) == currentDepth + 1:
                        nodeRight = TreeNode(int(self.splittedPos[1]), None, None)
                        nodeRec.right = nodeRight

                        if len(self.splittedPos) > 2 and len(self.splittedPos[0]) + 1 == len(self.splittedPos[2]):
                            self.splittedPos = self.splittedPos[2:]
                            recPreorderTraversal(nodeRec.right)
                        else: 
                            self.splittedPos = self.splittedPos[2:]
                            
            if len(self.splittedPos) == 2 and currentDepth == len(self.splittedPos[0]) - 1:
                if nodeRec.left is None: 
                    nodeLast = TreeNode(int(self.splittedPos[1]), None, None)
                    nodeRec.left = nodeLast
                    self.splittedPos = self.splittedPos[2:]
                elif nodeRec.right is None: 
                    nodeLast = TreeNode(int(self.splittedPos[1]), None, None)
                    nodeRec.right = nodeLast
                    self.splittedPos = self.splittedPos[2:]




        self.splittedPos = list(re.split(r"([\d]*)|([\-]*)", traversal))[1:-1]
        self.splittedPos = [i for i in self.splittedPos if i is not None and i != '']

        self.node = TreeNode(int(self.splittedPos[0]), None, None)
        self.splittedPos = self.splittedPos[1:]
        
        if len(self.splittedPos) > 1:
            recPreorderTraversal(self.node) 
        

        return self.node