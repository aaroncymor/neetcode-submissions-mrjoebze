class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if (
                    i + len(w) <= len(s) and
                    s[i:i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i + len(w)] = True
                        return memo[i + len(w)]

            memo[i] = False
            return memo[i]
        return dfs(0)