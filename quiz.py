from Deque_Generator import get_deque

def rec_palindrome(dq):
    if dq.pop_front()==dq.pop_back() and len(dq)>1:
        return rec_palindrome(dq)
    else:
        if len(dq)<=1:
            return True
        else:
            return False

def is_palindrome(character_string):
    dq = get_deque()
    for c in character_string:
        dq.push_back(c)
    return rec_palindrome(dq)
print(is_palindrome(input("Enter a phrase of lowercase characters only: ")))
