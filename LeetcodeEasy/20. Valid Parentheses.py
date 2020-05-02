

class Solution:
    def isValid(self, s: str)->bool:
        if s is None or len(s) == 0: return True
        if len(s) % 2 != 0: return False

        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif stack:
                cur = stack.pop()
                if cur != c:
                    return False

        return False if stack else True


if __name__ == "__main__":
    strs = ["()","()[]{}","(]", "([)]", "{[]}"]

    for s in strs:
        print("input %s" % s, " is valid parentheses: ", Solution().isValid(s))


