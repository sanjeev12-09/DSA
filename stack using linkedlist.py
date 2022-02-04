class EmptyStackError(Exception):
  pass

class Node:
  def __init__(self,value):
    self.info = value
    self.link = None

class Stack:
  def __init__(self):
    self.top = None

  def is_empty(self):
    return self.top == None

  def size(self):
    if self.top == None:
      return 0
    count =0
    p = self.top
    while p:
      count +=1
      p = p.link
    return count

  def push(self,item):
    temp =Node(item)
    temp.link = self.top
    self.top = temp

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")

    popped_element = self.top.info
    self.top = self.top.link
    return popped_element

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    return self.top.info

  def display(self):
    if self.is_empty():
      print("stack is empty")
      return 

    print("stack is ")
    p = self.top
    while p:
      print(p.info, end ="---")
      p = p.link

s = Stack()
print(s.size())
for i in range(5):
  s.push(i)
print(s.size())
s.display()
print("\n")
print(s.is_empty())
s.pop()
s.display()
print("\n")
print(s.peek())
print(s.size())
s.pop()
s.display()
print(s.size())