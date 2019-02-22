from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__size = 0
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__values = [None] * self.__capacity
    self.__front = 0
    self.__back = 0
    # TODO replace pass with any additional initializations you need.

  def __str__(self):
      if self.__size == 0:
          string = "[" + " " + "]"
          return string
      string = "[" + " " + str(self.__contents[self.__front])
      counter = self.__front
      while counter%len(self.__contents) is not self.__back:
          counter += 1
          string += "," + " " + str(self.__contents[counter%len(self.__contents)])
      string += " " + "]"
      return string
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.

  def __len__(self):
      length = self.__size
      return length
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.


  def __grow(self):
      self.__values = self.__contents
      self.__capacity = self.__capacity * 2
      self.__contents = [None] * self.__capacity
      if self.__front > self.__back:
          place_holder = 0
          for i in range(self.__front, (self.__back+int(self.__capacity/2))+1):
              self.__contents[place_holder] = self.__values[i%len(self.__values)]
              place_holder += 1
      if self.__front <= self.__back:
          for i in range(self.__front, self.__back+1):
              self.__contents[i] = self.__values[i]
      self.__front = 0
      self.__back = int((self.__capacity/2)-1)

  def push_front(self, val):
      if self.__size == 0:
          self.__contents[0] = val
          self.__size += 1
      elif self.__size == self.__capacity:
          self.__grow()
          self.__front = (self.__front - 1) % self.__capacity
          self.__contents[self.__front] = val
          self.__size += 1
      else:
          self.__front = (self.__front - 1) % self.__capacity
          self.__contents[self.__front] = val
          self.__size += 1

    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.


  def pop_front(self):
      if self.__size == 0:
          return None
      front_pop = self.__contents[self.__front]
      self.__contents[self.__front] = None
      self.__front = (self.__front + 1) % self.__capacity
      self.__size = self.__size - 1
      return front_pop
    # TODO replace pass with your implementation. Do not reduce the capacity.

  def peek_front(self):
      front_peek = self.__contents[self.__front]
      return front_peek
    # TODO replace pass with your implementation.

  def push_back(self, val):
      if self.__size == 0:
          self.__contents[0] = val
          self.__size += 1
      elif self.__size == self.__capacity:
          self.__grow()
          self.__contents[self.__size] = val
          self.__size += 1
          self.__back += 1
      else:
          self.__contents[self.__size] = val
          self.__size += 1
          self.__back += 1

    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.


  def pop_back(self):
      if self.__size == 0:
          return None
      back_pop = self.__contents[self.__back]
      self.__contents[self.__back] = None
      self.__back = (self.__back - 1) % self.__capacity
      self.__size = self.__size - 1
      return back_pop
    # TODO replace pass with your implementation. Do not reduce the capacity.

  def peek_back(self):
      back_peek = self.__contents[self.__back]
      return back_peek
    # TODO replace pass with your implementation.


# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
    AD = Array_Deque()
    AD.push_back(5)
    AD.push_back(6)
    AD.push_front(9)
    AD.push_front(10)
    print(AD.__str__())



#  pass
