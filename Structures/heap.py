''' This Heap will be a min based heap
-Sorted List
-First value will be dummy to indicate the very top'''

class Heap(object):
	

	def __init__(self, heap=[0]):
		#internal heap will be acting as counter
    #this counter will help determine the number
    #of elements within the structure
		self.length = 0
		self.internalheap = [self.length]


	def __len__(self):
		return self.length

	def heapup(self,index):
		if index == 1:
			return
		parent = index/2 
		
		if self.internalheap[index] < self.internalheap[parent]:
			self.internalheap[index],self.internalheap[parent] = self.internalheap[parent],self.internalheap[index]
	  	return self.heapup(parent)
	 	
	 	return 

	def downheap(self,index):
		#There is no need to downheap if you are the last child
		if index == self.length:
			return

		#if we want to down heap we need to consider the following
		#1.The children (max two children)
		#2.We need to choose the smallest out of the two
		#3.We then swap values and continue to downheap

		#The parent
		parent = self.internalheap[index]
		
		#If True then Children exists
		if index*2 <= self.length:
			
			#Both children Exists
			if (index*2) + 1 <= self.length:
				#The left child
				child1 = self.internalheap[index*2]
				#The right child
				child2 = self.internalheap[(index*2)+1]
			
				#If the left child is less than the right
				#The left is the min child
				if child1 < child2:
					min = index*2

				#The right child is the min child
				else:
					min = (index*2) + 1
			
			#If only left child exists
			else:
				min = (index*2)
        
			
			#If the parent is less than the min
			#Then there is no need for downheaping
			
			if parent < self.internalheap[min]:
				return
			#switch values and then downheap
			else:
				self.internalheap[index], self.internalheap[min] = self.internalheap[min], self.internalheap[index] 
				return self.downheap(min)
		return
	
	#Appends the new value to the end of the heap
	#adds one to the counter
	#sends the new value to upheap
	def push(self,value):
		self.internalheap.append(value)
		self.length += 1
		self.heapup(self.length)
	
	#When we pop we are popping from the top
	#the new min will be the last value inputed
	#Then we downheap
	def pop(self):
		if self.length == 1:
			popped = self.internalheap[1]
			self.internalheap.pop()
			self.length = 0
			return popped

		popped = self.internalheap[1]
		newMin = self.length
		self.internalheap[1] = self.internalheap[newMin]
		#Note: List pop, removes the right most item
		self.internalheap.pop()
		self.length -= 1
		self.downheap(1)
		return popped

	def __str__(self):
		output = ""
		for x in self.internalheap[1:]:
			output += str(x)+ "|"
		return output