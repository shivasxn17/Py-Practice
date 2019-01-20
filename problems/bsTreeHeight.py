class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        height = 0
        if(root == None or (root.left == None and root.right == None)): 
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if (leftHeight >= rightHeight) :
            height = leftHeight
        else:
            height = rightHeight
        return 1 + height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       