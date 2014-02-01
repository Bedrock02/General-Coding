
class hheap(dict):
	@staticmethod
	def _parent(i): # please use bit operation (same below)!
	 return (i-1)>>1
	@staticmethod
	def _left(i):
		return (i<<1) + 1
	@staticmethod
	def _right(i):
		return (i<<1) + 2


	'''
	Structure is the following
	inside the heap we have a list
	[position,value]

	which means the dictionary holds a list
	[position,value,key]

	'''
	def __init__(self):
		self.heap = []
		self.hLength = -1
		dict.__init__(self)

	def __setitem__(self,key,value):
		if dict.__contains__(self,key):
			item = dict.__getitem__(self,key)
			item[1] = value
			if item[1] < self.heap[self._parent(item[0])][1]:
				self.heapup(item[0])			
			else:
				self.heapdown(item[0])
		else:
			self.hLength += 1
			self.heap.append([self.hLength,value,key])
			dict.__setitem__(self,key,self.heap[-1])
			self.heapup(self.hLength)

	def __getitem__(self,key):
		'''Get item retrieves the value of the given key	'''

		if dict.__contains__(self,key):
			return dict.__getitem__(self,key)[1]
		raise KeyError("Key does not exist")

	def heapup(self,index):
		''' Maintains the property of a heap by checking its parent, mostly used after insertion'''
		parent = self._parent(index)
		if parent is -1:
			return
		if self.heap[index][1] < self.heap[parent][1]:
			self._swap(index,parent) 
			return self.heapup(parent)
			
		if self.heap[index][1] == self.heap[parent][1]:
			if self.heap[index][2] < self.heap[parent][2]:
				self._swap(index,parent)
				return self.heapup(parent)
		return

	def heapdown(self,index=0):
		''' Maintains the property of a heap by checking its children '''
		leftChild = self._left(index)
		rightChild = self._right(index)
		last = len(self.heap)-1
		
		if leftChild > last:
			return
		elif rightChild > last:
				if self.heap[leftChild][1] < self.heap[index][1]:
					self._swap(index,leftChild)
				return self.heapdown(leftChild)
		else:
			if self.heap[rightChild][1] < self.heap[leftChild][1]:
				min = rightChild
			else:
				min = leftChild
			if self.heap[index][1] > self.heap[min][1]:
				self._swap(index,min)
			if self.heap[index][1] == self.heap[min][1]:
				if self.heap[index][2] > self.heap[min][2]:
					self._swap(index,min)
			return self.heapdown(min)

	def _swap(self, i, j):
		"""swap the contents b/w indices i and j; update hash accordingly"""
		#swap within the heap
		self.heap[i][0],self.heap[j][0] = j,i
		self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
		
	def pop(self): 
		# pop root (best)
		#display the soon to be popped item
		popped = self.heap[0]
		
		#remove from dict and heap
		dict.__delitem__(self,popped[2])
		self._swap(0,self.hLength)
		self.heap.pop()
		self.heapdown()
		self.hLength-=1
		return popped
	
	def update_if_better(self, key, newvalue,viakey=None):
		"""update if newvalue is better than the current value for key
		or insert if key is not here yet."""
		if dict.__contains__(self,key):
			self[key] = min(self[key],newvalue)
			info = dict.__getitem__(self,key)
			if self[key] == newvalue:
				if len(info) is 3:
					info.append(viakey)
				else:
					info[3] = viakey
		else:
			self[key] = newvalue
			
	def Display(self,arry):
		#print arry
		if len(arry) is 4:
			print arry[2]+" "+str(arry[1])+ " (via "+arry[3]+")"
		else:
			if arry[1] == float("+inf"):
				print str(arry[2])+" "+"unreachable"
			
			else:
			 print str(arry[2])+" "+str(arry[1])

#	def GenerateItems(self):
#		for x in self.heap:
#			yield x
	def __str__(self):
		string = "{"
		string += ', '.join(["'" + item[0]+ "'" + ": "+str(item[1][1]) for item in sorted(self.items(),key = lambda x: x[1][1])])
		string +="}"
		return string
	
	__repr__ = __str__
