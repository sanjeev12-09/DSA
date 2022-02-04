class Node:
  def __init__(self, value):
    self.info = value
    self.link = None

class SingleLinkedList:
  def __init__(self):
    self.start = None

  def display_list(self):
    if self.start == None :
      print("List is empty")
    else:
      print("List is :")
      p = self.start
      while p is not None:
        print(p.info, end=' ')
        p = p.link
      print()

  def count_nodes(self):
    p = self.start
    n= 0
    while p is not None:
      n=n+1
      p= p.link

    print("Number of element in list is :",n)

  def search(self,x):
    p = self.start
    position =1
    while p :
      if p.info == x :
        print (" x is at position - ", position)
        return True
      position = position+1
      p = p.link
    else:
      print("x is not found")
      return False

  def insert_at_begining(self,data):
    temp = Node(data)
    temp.link = self.start
    self.start = temp

  def insert_at_end(self, data):
    temp = Node(data)
    if self.start is None:
      self.start = temp
      return
    p = self.start
    while p:
      p = p.link
    p.link = temp

  def create_list(self):
    n = int(input("Enter the number of node :" ))
    if n ==0 :
      return
    for i in range(n):
      data = int(input("Enter the element to be inserted: "))
      self.insert_at_end(data)

  def insert_after(self,data, x):
    p = self.start
    while p:
      if p.info == x:
        break
      p = p.link
    temp = Node(data)
    temp.link = p.link
    p.link = temp

  def insert_before(self,data,x):
    if self.start is None:
      print("List is empty ")
    # if x is first node new node have to insert itbefore first node
    if self.start == x:
      temp = Node(data)
      temp.link = self.start
      self.start = temp
    
    p = self.start
    while p:
      if p.link.info == x:
        break
      p = p.link
    if p.link is None:
      print(x,"not present in the list")
    else:
      temp = Node(data)
      temp.link = p.link
      p.link = temp
    
  def delete_node(self,x):
    if self.start is None:
      print("List is empty ")
    # delete the first node
    if self.start == x:
      self.start = self.start.link
    
    p = self.start
    while p:
      if p.link.info == x:
        break
      p = p.link
    if p.link is None:
      print(x,"not present in the list")
    else:
      p.link = p.link.link
  
  def reverse_list(self):
    prev = None
    p = self.start
    while p is not None:
      next = p.link
      p.link = prev 
      prev = p
      p = next
    self.start = prev 

list = SingleLinkedList()
list.create_list()