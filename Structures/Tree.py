#Binary Search Tree is based off the list-based tree
#so for example a tree with a root of 5 and children of 4 and 6 would be represented as [5,4,6]

class BST(object):
  __slots__ = "val", "left", "right"
  
  def __init__(self, val=None, left=None, right=None):
    
    #if val is none then it is an empty tree
    if val is None:
      self.val = self.left = self.right = None
    
    #if either left or right is None an empty BST will be present
    else:
      self.val = val
      self.left = left if left is not None else BST()
      self.right = right if right is not None else BST()
  
  def search(self, query):
    if self.val is None:
      return False, self
    
    c = cmp(query, self.val)
    
    if c == 0:
      return True, self
    
    elif c < 0:
      return self.left.search(query)
    return self.right.search(query)
  
  def __contains__(self, query):
    found, _ = self.search(query)
    return found
  
  def delete(self, query):
    found, node = self.search(query)
    Lchild = node.left.val
    Rchild = node.right.val
    if Lchild is None and Rchild is None:
      print "none"
    
  def insert(self, query):
    found, node = self.search(query)
    if not found:
      node.__init__(query)

  def iteritems(self):
    if self.val is None:
      return
    for item in self.left.iteritems():
      yield item
    yield self.val
    for item in self.right.iteritems():
      yield item

  def list(self):
    if self.val is None:
      return []
    return self.left.list() + [self.val] + self.right.list()
  
  def __str__(self):
    return "(%s %s %s)" % (self.left, self.val, self.right)
