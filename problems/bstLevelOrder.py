import sys

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

    def levelOrder(self,root):
        root = self.root if root is None else root
        to_visit = [root]
        visited = []
        while to_visit:
            current = to_visit.pop(0)
            visited.append(current.data)
            print(current.data,end=" ")
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)
        return visited

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
