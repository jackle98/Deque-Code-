from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self._dq = get_deque(0)

  def __str__(self):
    string = self._dq.__str__()
    return string

  def __len__(self):
      length = self._dq.__len__()
      return length

  def push(self, val):
      self._dq.push_front(val)

  def pop(self):
      if len(self._dq) == 0:
          return None
      popped = self._dq.pop_front()
      return popped

  def peek(self):
      if len(self._dq) == 0:
          return None
      value = self._dq.peek_front()
      return value

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
