import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
    check_file = open(filename, 'r')
    string = check_file.read()
    stack = Stack()
    for c in string:
        if c == "(" or c == "[" or c == "{":
            stack.push(c)
        if c == ")" or c == "]" or c == "}":
            if len(stack) == 0:
                return False
            elif stack.peek() == "(" and c == ")" or stack.peek() == "[" and c == "]" or stack.peek() == "{" and c == "}":
                stack.pop()
            else:
                stack.push(c)
    if stack.peek() == ")" or stack.peek() == "]" or stack.peek() == "}":
        return False
    if stack.peek() == "(" or stack.peek() == "[" or stack.peek() == "{":
        return False
    else:
        return True



  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
