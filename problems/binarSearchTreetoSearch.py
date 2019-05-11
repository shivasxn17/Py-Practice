import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
	if root.value == None:
		return False
	else:
		if root.value == value: 
			return True
		elif root.value > value:
			if root.left != None:
				return contains(root.left,value)
			else:
				return False    		
		elif root.value < value:
			if root.right != None:    	
				return contains(root.right,value)
			else:
				return False
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))