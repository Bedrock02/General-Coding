#This Represents the structure to a Binary Search Tree
#The Binary Search Tree functions similar to a Dictionary
#For example to add an item: tree["node1"] = 3

class BST(object): #non-recursive methods
	
	__slots__ = "missing", "root", "length","searchNode"
	
	def __init__(self, dict=None, missing = None):
		self.missing = missing
		self.root = BSTNode()
		self.length = 0
		self.searchNode = self.root
		
		if dict is not None:
			for k, v in dict.iteritems():
				self[k] = v

	def __getitem__(self, key):
		node = self.root.search(key)
		if node.kv is None:
			#change it up for syntactic sugar
			self[key]=self.missing()
		return node.kv[1]
	
	def __setitem__(self, key, value):
		node = self.root.search(key)
		if node.kv is not None:
			node.kv = (key,value)
		else:
			node.__init__((key,value))
		self.length+=1

	def __delitem__(self,key):
		node = self.root.search(key)
		#print "Before Deletion Length: ",len(self)
		if node.kv is None:
			raise KeyError(str(key))
		#Case 1: No children
		elif node.left.kv is None and node.right.kv is None:
			node.kv = None
			self.length -=1
		#Case 2: 2 Children
		elif node.left.kv is not None and node.right.kv is not None:
			maxNode = node.left.max()
			newTup = maxNode.kv
			del self[maxNode.kv[0]]
			node.kv = newTup
			return
		#Case 3: 1 child
		else:
			if node.left.kv is None and node.right.kv is not None:
				node.kv = node.right.kv #copy the key
				node.left = node.right.left #copy the children 
				node.right = node.right.right
			else:	
				node.kv = node.left.kv
				node.right = node.left.right
				node.left = node.left.left
			self.length -=1
		
	#Returns a generator of the keys	
	def __iter__(self):
		return self.root.iterkeys()
		
	def __contains__(self, key):
		return self.root.search(key).kv is not None
	
	def __len__(self):
		return self.length
	
	def pop(self):
		if self.length is 0:
			raise KeyError("Your Tree is empty")
		else:
			minNode = self.root.min().kv
			del self[minNode[0]]
			print minNode
			self.length -=1

	#returns a list of the keys
	def keys(self):
		return [x for x in self]
	#returns a list of the values
	def values(self):
		return [x[1] for x in self.root.iteritems()]

	def items(self):
		return [x	for x in self.root.iteritems()]

	def iteritems(self):
		return self.root.iteritems()

	__str__ = lambda x: str(x.root)
	__repr__ = lambda x: repr(x.root)
	
class BSTNode(object): #recursive methods
	
	__slots__ = "kv", "left", "right" # kv is (key, value)
	
	def __init__(self, kv=None, left=None, right=None):
		self.kv = kv
		if kv is not None:
			self.left = left if left is not None else BSTNode()
			self.right = right if right is not None else BSTNode()
	
	def search(self, key):
	
		if self.kv is None:
			return self
		cmpValue = cmp(self.kv[0],key)
		if cmpValue is 0:
			return self
		if cmpValue is -1:
			return self.right.search(key)
		else:
			return self.left.search(key)
	
	#print out items
	def iteritems(self):
		if self.kv is None:
			return
		
		for items in self.left.iteritems():
			yield items
		
		yield self.kv

		for items in self.right.iteritems():
			yield items

	#print out keys
	def iterkeys(self):
	
		if self.kv is None:
			return
		
		for items in self.left.iteritems():
			yield items[0]
		
		yield self.kv[0]

		for items in self.right.iteritems():
			yield items[0]
	
	def max(self):

		if self.right.kv is None:
			return self
		return self.right.max()

	def min(self):
		if self.left.kv is None:
			return self
		return self.left.min()
	
	def __str__(self):
		if self.kv is None:
			return "_"
		else:
			return "(%s %s:%s %s)" % (self.left,self.kv[0],self.kv[1],self.right)			

	def __repr__(self, indent=0):

		if self.kv is None:
			return ""*indent
		
		for x in self.iteritems():
			return "\n"+"|"*indent+"%s:%s%s%s" % (self.kv[0],self.kv[1],self.left.__repr__(indent+1),self.right.__repr__(indent+1))
	