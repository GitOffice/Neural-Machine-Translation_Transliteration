
class AVLnode(object):
	
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.height = 0
		self.leftChild = None
		self.rightChild = None
		
	def visit(self):
		print("(height:%s, key:%s, value:%s)" % (self.height, self.key, self.value))

class AVL(object):

	def __init__(self):
		self.rootNode = None

	def put(self, key, value):
		self.rootNode = self.insertNode(key, value, self.rootNode)

	def insertNode(self, key, value, node):
		if not node:
			return AVLnode(key, value)
		if key < node.key:
			node.leftChild = self.insertNode(key, value, node.leftChild)
		else:
			node.rightChild = self.insertNode(key, value, node.rightChild)
		node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1		
		return self.settleViolation(key, node)

	def remove(self, key):
		if self.rootNode:
			self.rootNode = self.removeNode(key, self.rootNode)

	def removeNode(self, key, node):
		if not node:
			return node

		if key < node.key:
			node.leftChild = self.removeNode(key, node.leftChild)
		elif key > node.key:
			node.rightChild = self.removeNode(key, node.rightChild)
		else:
			if not node.leftChild and not node.rightChild:
				# Removing a leaf node...
				del node
				return None

			if not node.leftChild:
				# Removing a node with a right child...
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:
				# Removing a node with a left child...
				tempNode = node.leftChild
				del node
				return tempNode
				
			# Removing node with two children...
			tempNode = self.getPredecessor(node.leftChild)
			node.key = tempNode.key
			node.leftChild = self.removeNode(tempNode.key, node.leftChild)

		if not node:
			return node # if the tree had just a single node
		
		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
		
		balance = self.calcBalance(node)
		
		# doubly left heavy situation
		if balance > 1 and self.calcBalance(node.leftChild) >= 0:
			return self.rotateRight(node)
			
		# left right case
		if balance > 1 and self.calcBalance(node.leftChild) < 0:
			node.leftChild = self.rotateLeft(node.leftChild)
			return self.rotateRight(node)
		
		# right right case
		if balance < -1 and self.calcBalance(node.rightChild) <= 0:
			return self.rotateLeft(node)
			
		# right left case
		if balance < -1 and self.calcBalance(node.rightChild) > 0:
			node.rightChild = self.rotateRight(node.rightChild)
			return self.rotateLeft(node)
			
		return node
		
	def getPredecessor(self, node):
		if node.rightChild:
			return self.getPredecessor(node.rightChild)
		return node
		
	def settleViolation(self, key, node):
		balance = self.calcBalance(node)

		# Case I left-left heavy situation
		if balance > 1 and key < node.leftChild.key:
			# Left left heavy tree...
			return self.rotateRight(node)
		
		# Case II right-right
		if balance < -1 and key > node.rightChild.key:
			# Right right heavy tree...
			return self.rotateLeft(node)
	
		# left-right situation
		if balance > 1 and key > node.leftChild.key:
			# Tree is leaft right heavy...
			node.leftChild = self.rotateLeft(node.leftChild)
			return self.rotateRight(node)
		
		# right-left situation
		if balance < -1 and key < node.rightChild.key:
			node.rightChild = self.rotateRight(node.rightChild)
			return self.rotateLeft(node)

		return node
		
	def calcHeight(self, node):
		if not node:
			return -1
		return node.height
		
	# returns value > 1  --> left heavy tree --> right rotation 
	#  ......       < -1 --> right heavy tree --> left rotation
	def calcBalance(self, node):
		if not node:
			return 0
		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
	
	def traverse(self):
		if self.rootNode:
			self.traverseInorder(self.rootNode)
	
	def traverseInorder(self, node):
		if node.leftChild:
			self.traverseInorder(node.leftChild)
		node.visit()		
		if node.rightChild:
			self.traverseInorder(node.rightChild)
	
	def get(self, key):
		if self.rootNode:
			return self.getHelper(key, self.rootNode)
		return None

	def getHelper(self, key, node):
		if node:
			if node.key == key:
				return node.value
			if key > node.key:
				# search in the right
				return self.getHelper(key, node.rightChild)
			else: # key < node.key
				# search in the left
				return self.getHelper(key, node.leftChild)
		return None
	
	def rotateRight(self, node):
		# Rotating to the right on node node.key
		tempLeftChild = node.leftChild
		t = tempLeftChild.rightChild
		
		tempLeftChild.rightChild = node
		node.leftChild = t
		
		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
		tempLeftChild.height = max( self.calcHeight(tempLeftChild.leftChild) , self.calcHeight(tempLeftChild.rightChild) ) + 1
		
		return tempLeftChild
		
	def rotateLeft(self, node):
		# Rotating to the left on node node.key
		
		tempRightChild = node.rightChild
		t = tempRightChild.leftChild
		
		tempRightChild.leftChild = node
		node.rightChild = t
		
		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
		tempRightChild.height = max( self.calcHeight(tempRightChild.leftChild) , self.calcHeight(tempRightChild.rightChild) ) + 1
		
		return tempRightChild
		

if __name__ == '__main__':
	import numpy as np
	
	avl = AVL()
	avl.put('a', np.random.rand(3))
	avl.put('b', np.random.rand(3))
	avl.put('c', np.random.rand(3))
	avl.put('d', np.random.rand(3))
	avl.put('e', np.random.rand(3))
	avl.put('f', np.random.rand(3))
	avl.put('g', np.random.rand(3))
	"""
	a     c    e     g
	 \   /      \   /
	   b          f
	    \        /
		    d
	"""
	
	avl.traverse()
	print('-'*50)
	
	print(avl.get('b'))
	
	avl.remove('b')
	#avl.remove('a')
	
	print(avl.get('b'))
	
	avl.traverse()
