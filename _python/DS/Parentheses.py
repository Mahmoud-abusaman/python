from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dic = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            else: 
                if not stack or stack[-1] != dic[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
