class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        # print(strs[0][0])
        min_length = len(strs[0])
        # print(min_length)
        for s in strs:
            min_length = min(min_length, len(s))
        for i in range(min_length):
            ch = strs[0][i]
            print(s[i])
            for s in strs:
                if ch != s[i]:
                    return ''.join(result)
            result.append(ch)
        
        return strs[0][:min_length]

        