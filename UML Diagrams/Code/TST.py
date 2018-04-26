
class TSTnode(object):
	def __init__(self, key, value=None):
		"""
		key: one of the word's characters
		"""
		self.key = key
		self.value = value
		self.leftNode = None
		self.middleNode = None
		self.rightNode = None
		
class TST(object):
	def __init__(self):
		self.rootNode = None

	def put(self, key, value):
		self.rootNode = self.putItem(self.rootNode, key, value, 0)

	def putItem(self, node, key, value, index):
		"""
			node 	the node where we want to add the (key, value) pair
			index 	index in the key string
		"""
		c = key[index]
		
		if node == None:
			node = TSTnode(c, value)
			
		if c < node.key:
			node.leftNode = self.putItem(node.leftNode, key, value, index)
		elif c > node.key:
			node.rightNode = self.putItem(node.rightNode, key, value, index)
		elif index < len(key) - 1:
			node.middleNode = self.putItem(node.middleNode, key, value, index+1)
		else:
			node.value = value
		return node;
		
	def get(self, key):
		node = self.getItem(self.rootNode, key, 0)
		if node == None or node.value == None:
			return None
		return node.value
	
	def getItem(self, node, key, index):
		if node == None:
			return None
		c = key[index]
		if c < node.key:
			return self.getItem(node.leftNode, key, index)
		elif c > node.key:
			return self.getItem(node.rightNode, key, index)
		elif index < len(key) - 1:
			return self.getItem(node.middleNode, key, index+1)
		else:
			return node

