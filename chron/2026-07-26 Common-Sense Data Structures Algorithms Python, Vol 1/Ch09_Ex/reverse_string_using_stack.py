# use deque for stack

from collections import deque

def reverse_string_using_stack(str: string):
    stack = deque()
    for ch in str:
        stack.append(ch)
    
    reverse_str = ""
    while stack:
        reverse_str = reverse_str + stack.pop()
    
    return reverse_str



print(reverse_string_using_stack("abcde"))


