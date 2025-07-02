class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9+7
        if len(word) == k:
            return 1
        freq = []
        prev = word[0]
        count = 0
        for ch in word:
            if ch == prev:
                count += 1
            else :
                prev = ch
                freq.append(count)
                count = 1
        freq.append(count)
        
        a = 1
        for fact in freq :
            a = (a * fact)  % mod
        if len(freq) >= k:
            return a
        # print(freq)
        
        dp = [0] * k
        dp[0] = 1

        for num in freq :
            new_dp = [0] * k
            Sum = 0
            for s in range(k):
                if s > 0:
                    Sum = (Sum + dp[s - 1]) % mod
                if s > num:
                    Sum = (Sum - dp[s - num - 1]) + mod
                new_dp[s] = Sum

            dp = new_dp
        invalid = sum(dp[len(freq) : k]) % mod
        return (a - invalid + mod) % mod
