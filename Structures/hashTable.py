#implementation of a hast table using just arrays
#The idea behind this is that there will be list of keys
#
class listHash(object):


	__slots__ = "key_list","value_list"
	
	def __init__(self):
		self.key_list = []
		self.value_list = []

	def get(self,key):
		if key not in self.key_list:
			return "The Key: %s does not exist in this hash" % key
		else:
			return self.value_list[self.key_list.index(key)]
	
	def set(self,key,value):
		if key in self.key_list:
			self.value_list[self.key_list.index(key)] = value
		else:
			self.key_list.append(key)
			self.value_list.append(value)
		return self
	
	def __contains__(self,key):
		return key in self.key_list

	def remove(self,key):
		value_list.pop[self.key_list.index(key)]
		key_list.remove(key)

implemHash = listHash()
implemHash.set("Loser","Miriam")
implemHash.set("Loser","Steven")

