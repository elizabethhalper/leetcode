# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        paren_map = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in paren_map:
                top = paren_stack.pop() if paren_stack else '#'
                if paren_map[ch] != top:
                    return False
            else:
                paren_stack.append(ch)
        return not paren_stack