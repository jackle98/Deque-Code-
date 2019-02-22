class Linked_List:

  class __Node:

    def __init__(self, val):
        self.next = None
        self.previous = None
        self.value = val
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation

  def __init__(self):
      self.__header = self.__Node(None)
      self.__trailer = self.__Node(None)
      self.__size = 0
      self.__header.next = self.__trailer
      self.__trailer.previous = self.__header
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class


  def __len__(self):
      return self.__size
    # return the number of value-containing nodes in
    # this list.



  def append_element(self, val):
      new_node = Linked_List.__Node(val)
      if self.__header.next == self.__trailer:
          self.__trailer.previous = new_node
          new_node.next = self.__trailer
          self.__header.next = new_node
          new_node.previous = self.__header
      else:
          curr = self.__trailer.previous
          self.__trailer.previous = new_node
          new_node.next = self.__trailer
          curr.next = new_node
          new_node.previous = curr
      self.__size += 1


    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation


  def insert_element_at(self, val, index):
      if index > (self.__size - 1):
          raise IndexError
      if index < 0:
          raise IndexError
      new_node = Linked_List.__Node(val)
      if index < self.__size//2:
          curr = self.__header.next
          for j in range(index):
              curr = curr.next
          new_node.next = curr
          new_node.previous = curr.previous
          curr.previous.next = new_node
          curr.previous = new_node
      else:
          curr = self.__trailer.previous
          for j in range(self.__size - index):
              curr = curr.previous
          new_node.previous = curr
          new_node.next = curr.next
          curr.next.previous = new_node
          curr.next = new_node
      self.__size += 1
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the
    # specified index. If the index is not a valid
    # position within the list, raise an IndexError
    # exception. This method cannot be used to add an
    # item at the tail position.
    # TODO replace pass with your implementation


  def remove_element_at(self, index):
      if index > (self.__size - 1):
          raise IndexError
      if index < 0:
          raise IndexError
      if index < self.__size//2:
          curr = self.__header.next
          for j in range(index):
              curr = curr.next
          curr.previous.next = curr.next
          curr.next.previous = curr.previous
      else:
          curr = self.__trailer
          for j in range (self.__size - index):
              curr = curr.previous
          curr.previous.next = curr.next
          curr.next.previous = curr.previous
      self.__size -= 1
      return curr.value

    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation


  def get_element_at(self, index):
      if index > (self.__size - 1):
          raise IndexError
      if index < 0:
          raise IndexError
      if index < self.__size//2:
          curr = self.__header.next
          for j in range(index):
              curr = curr.next
      else:
          curr = self.__trailer
          for j in range(self.__size - index):
              curr = curr.previous
      return curr.value
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation


  def rotate_left(self):
      if self.__size == 0:
          return None
      curr = self.__header.next
      self.__header.next = curr.next
      curr.next.previous = self.__header
      curr.previous = self.__trailer.previous
      self.__trailer.previous.next = curr
      curr.next = self.__trailer
      self.__trailer.previous = curr
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.


  def __str__(self):
      if self.__size == 0:
          return "[" + " " + "]"
      elif self.__size == 1:
          curr = self.__header.next
          string = "[" + " " + str(curr.value) + " " + "]"
          return string
      else:
          curr = self.__header.next
          string = "[" + " " + str(curr.value)
          while curr.next is not self.__trailer:
              curr = curr.next
              string += "," + " " + str(curr.value)
          string += " " + "]"
          return string




    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation


  def __iter__(self):
      self.__iter__index = self.__header.next
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
      return self

  def __next__(self):
      if self.__iter__index == self.__trailer:
          raise StopIteration
      curr = self.__iter__index.value
      self.__iter__index = self.__iter__index.next
      return curr
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation


if __name__ == '__main__':
   #testing the append function as well as size being incrimented correctly
    test1 = Linked_List()
    print("Testing the string function with no nodes.")
    print(test1.__str__())
    print("Testing append and string function with one node.")
    test1.append_element(9)
    print(test1.__str__())
    print("Testing append and string function with multiple nodes.")
    test1.append_element(10)
    print(test1.__str__())
    test1.append_element(1)
    print(test1.__str__())
    test1.append_element(12)
    print(test1.__str__())
    print("Testing length function (should be 4).")
    print("The size is: " + str(test1.__len__()))

   #Testing insert_element_at function and if it is incremented correctly
    test2 = Linked_List()
    print("Testing trying to add an element to an empty list.")
    try:
        test2.insert_element_at(10, 0)
    except IndexError:
        print("Can't insert element into an empty list.")
    print("Testing inserting an element in a one value long list and size.")
    test2.append_element(1)
    test2.insert_element_at(10, 0)
    print(test2.__str__())
    print("The size is: " + str(test2.__len__()))
    print("Testing invalid index given by user (< 0), on non-empty list.")
    try:
        test2.append_element(2)
        test2.append_element(3)
        test2.insert_element_at(10, -1)
    except IndexError:
        print("Negative index is invalid.")
    print("Testing invalid index given by user (> (size of list-1)), on non-empty list.")
    try:
        test2.insert_element_at(10, 4)
    except IndexError:
        print("Index larger than (size of list-1) is invalid.")
    print("Testing inserting an element in a list with multiple values" \
     "(One with lower index and one with higher index) and size.")
    test2.insert_element_at(20, 1)
    print(test2.__str__())
    print("The size is: " + str(test2.__len__()))
    test2.insert_element_at(30, 4)
    print(test2.__str__())
    print("The size is: " + str(test2.__len__()))

   #Testing remove_element_at function and if size is done correctly
    test3 = Linked_List()
    print("Testing trying to remove an element from an empty list.")
    try:
        test3.remove_element_at(0)
    except IndexError:
        print("Cannot remove value from empty list.")
    print("Testing trying to remove an element from a one value list and size.")
    test3.append_element(1)
    print("Removed value: " + str(test3.remove_element_at(0)))
    print(test3.__str__())
    print("Size of list: " + str(test3.__len__()))
    print("Testing invalid index given by user (< 0), on non-empty list.")
    try:
        test3.append_element(1)
        test3.append_element(2)
        test3.append_element(3)
        test3.remove_element_at(-1)
    except IndexError:
        print("Negative index is invalid.")
    print("Testing invalid index given by user (> (size of list-1)), on non-empty list.")
    try:
        test3.remove_element_at(3)
    except IndexError:
        print("Index is out of bounds (> (size of list-1)).")
    print("Testing removing an element in a list with multiple values" \
     "(One with lower index and one with higher index) and size.")
    test3.append_element(4)
    test3.append_element(5)
    print(test3.__str__())
    print("Size of list: " + str(test3.__len__()))
    print("Removed value: " + str(test3.remove_element_at(1)))
    print(test3.__str__())
    print("Size of list: " + str(test3.__len__()))
    print("Removed value: " + str(test3.remove_element_at(3)))
    print(test3.__str__())
    print("Size of list: " + str(test3.__len__()))

   #Testing get_element_at function
    test4 = Linked_List()
    print("Testing trying to get an element in an empty list.")
    try:
        test4.get_element_at(0)
    except IndexError:
        print("Cannot get element in empty list.")
    print("Testing get element from a one value long list.")
    test4.append_element(1)
    print(test4.get_element_at(0))
    print("Testing invalid index given by user (< 0), on non-empty list.")
    try:
        test4.append_element(2)
        test4.append_element(3)
        test4.append_element(4)
        test4.get_element_at(-1)
    except IndexError:
        print("Negative index is invalid.")
    print("Testing invalid index given by user (> (size of list-1)), on non-empty list.")
    try:
        test4.get_element_at(6)
    except IndexError:
        print("Index is out of bounds (> (size of list-1)).")
    print("Testing getting an element in a list with multiple values" \
     "(One with lower index and one with higher index).")
    print(test4.__str__())
    print("Value at index 1: " + str(test4.get_element_at(1)))
    print("Value at index 3: " + str(test4.get_element_at(3)))

   #Testing rotate_left function
    test5 = Linked_List()
    print("Testing rotate left if list is empty (no effect).")
    print("Before rotate: " + test5.__str__())
    test5.rotate_left()
    print("After rotate: " + test5.__str__())
    print("Testing rotate left if list is one value long (no effect).")
    test5.append_element(1)
    print("Before rotate: " + test5.__str__())
    test5.rotate_left()
    print("After rotate: " + test5.__str__())
    print("Testing rotate left with multiple values.")
    test5.append_element(2)
    test5.append_element(3)
    test5.append_element(4)
    print("Before rotate: " + test5.__str__())
    test5.rotate_left()
    print("After rotate 1: " + test5.__str__())
    test5.rotate_left()
    print("After rotate 2: " + test5.__str__())
    test5.rotate_left()
    print("After rotate 3: " + test5.__str__())
    test5.rotate_left()
    print("After rotate 4: " + test5.__str__())

   #Testing the iterator and next functions
    test6 = Linked_List()
    print("Testing if list is empty (Nothing should appear).")
    for val in test6:
       print(val)
    print("Testing if list has one value.")
    test6.append_element(1)
    for val in test6:
        print(val)
    print("Testing if list has multiple values.")
    test6.append_element(2)
    test6.append_element(3)
    test6.append_element(4)
    for val in test6:
        print(val)

  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
