class EmptyStackError(Exception):
  pass

class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  def push(self,item):
    return self.items.append(item)

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")

    return self.items.pop()

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    return self.items[-1]

  def display(self):
    print(self.items)
  
  def __str__(self):
    return str(self.items)

s = Stack() 
for i in range(5):
  s.push(i)
  print(s)
print(s.size())
s.display()