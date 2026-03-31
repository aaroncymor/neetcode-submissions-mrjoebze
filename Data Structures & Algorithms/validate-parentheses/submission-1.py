class Solution:
    def isValid(self, s: str) -> bool:
        
        def is_full_bracket(opening, closing):
            if opening == "(":
                return True if closing == ")" else False

            if opening == "[":
                return True if closing == "]" else False

            if opening == "{":
                return True if closing == "}" else False

        if not s:
            return False

        stack = []
        for i in range(len(s)):

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if not stack:
                    return False

                opening = stack.pop()

                if not is_full_bracket(opening, s[i]):
                    return False


        return True if not stack else False

