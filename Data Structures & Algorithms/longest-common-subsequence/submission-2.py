class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[0 for j in range(len(text2) + 1)] 
        #          for i in range(len(text1) + 1)]

        # for i in reversed(range(len(text1))):
        #     for j in reversed(range(len(text2))):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        cur = [0] * (len(text2) + 1)

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    cur[j] = 1 + prev[j+1]
                else:
                    cur[j] = max(cur[j+1], prev[j])
            prev, cur = cur, prev

        return prev[0]