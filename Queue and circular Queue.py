class EmptyQueueError(Exception):
  pass

class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  def enqueue(self, item):
    return self.items.append(item)

  def dequeue(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")
    return self.items.pop(0)

  def peek(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")
    return self.items[0]

  def display(self):
    print(self.items)

if __name__ == "__main__":
  q = Queue()

for i in range(5):
  q.enqueue(i)

q.display()

# In this above code when we dequeue an element it takes n times to rearrange itself. so, it is not good .we can reduce the n time to constant time . 

class queue:
  def __init__(self):
    self.items = []
    self.front = 0 

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    return self.items.append(item)

  def dequeue(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")
    x = self.items[self.front]
    self.items[self.front] = None
    self.front = self.front +1
    return x

  def peek(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")

    return self.items[self.front]

  def display(self):
    print(self.items)

Q = queue()
for i in range(6,11):
  Q.enqueue(i)

Q.display()

Q.dequeue()
print(Q.peek())
Q.display()
Q.dequeue()
Q.display()

# In this algorithm time is reduced but alot of space is useless. so, it is not a efficient algorithm. we can undercome by using circular queue. 

class circularQueue:
  def __init__(self, default_size = 10):
    self.items = [None] * default_size
    self.front = 0
    self.count = 0

  def is_empty(self):
    return self.items == 0

  def size(self):
    return self.count

  def resize(self,newsize):
    old_list = self.items
    self.items = [None] * newsize
    i = self.front
    for j in range(self.count):
      self.items[j] = old_list[i]
      i = (1+i) % len(old_list)
    self.front =0

  def enqueue(self,item):
    if self.count == len(self.items):
      self.resize(2 * len(self.items))

    i = (self.front + self.count) % len(self.items)
    self.items[i] = item
    self.count +=1

  def dequeue(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")

    x = self.items[self.front]
    self.items[self.front] = None
    self.front = (1 + self.front) % len(self.items)
    self.count -= 1
    return x

  def peek(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")

    return self.items[self.front]

  def display(self):
    print(self.items)

c = circularQueue()
for i in range(12,18):
  c.enqueue(i)

print(c.size())
c.display()
print(c.peek())
c.dequeue()
print(c.peek())
c.display()
c.dequeue()
c.display()
c.enqueue(45)
c.display()
print(c.size())
