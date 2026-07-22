class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in hmap.keys():
                if not stack:
                    return False

                opening = stack.pop()
                if opening != hmap[c]:
                    return False
            else:
                stack.append(c)

        return False if stack else True

