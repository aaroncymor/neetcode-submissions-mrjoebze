class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }
        for i in range(len(s)-1, -1, -1):
            print("I", i)
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

                print("I + 1", i + 1)
                if i + 1 < len(s):
                    if s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456":
                        dp[i] += dp[i + 2]
        print("DP", dp)
        return dp[0]
