class Stack(object):

	def __init__(self,stack=[]):
		self.stack = stack
		self.length = 0

	def push(self,value):
		self.stack.append(value)
		self.length += 1

	def pop(self):
		popped = self.stack[-1]
		self.stack = self.stack[:-1]
		self.length -= 1
		return popped

	def __str__(self):
		return '[%s]' % '\n '.join(map(str,self.stack))


