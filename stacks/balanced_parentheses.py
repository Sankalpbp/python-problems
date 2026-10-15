class Solution(object):

    def __init__(self):
        self.mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        self.stack = []

    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for char in s:
            if char == '[' or char == '(' or char == '{':
                self.stack.append(char)
            else:
                if len(self.stack) == 0 or self.mapping.get(char) is not self.stack.pop():
                    return False

        return len(self.stack) == 0

solution = Solution()

print(Solution.is_valid(solution, "([])"))
print(Solution.is_valid(solution, "([]}"))
print(Solution.is_valid(solution, "({[]}))"))
