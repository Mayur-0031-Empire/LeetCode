class Solution:
    def minInsertions(self, s: str) -> int:
        """
        i ch ch_next count ans

        ch == ( ==> count++ i += 1 (no others condition matters)

        ch == ) && ch_next not exits && count == 0 ==> ans += 2 end
        ch == ) && ch_next not exits && count > 0 ==> ans = ans + 1 + (count - 1) * 2 end

        ch == ) && ch_next exits && ch_next == ) && count == 0 ==> ans++, i = i + 2
        ch == ) && ch_next exits && ch_next == ) && count > 0 ==> count-- i = i + 2

        ch == ) && ch_next exits && ch_next == ( && count == 0 ==> ans += 2, count++, i = i + 2
        ch == ) && ch_next exits && ch_next == ( && count > 0 ==> ans += 1, i = i + 2
        """

        i = 0
        n = len(s)
        if(n == 0):
            return 0
        count = 0
        ans = 0
        while i < n:
            ch = s[i]
            if ch == "(":
                count += 1
                i += 1
            else :
                i += 1
                if i >= n: # ch_next not exit
                    if count == 0:
                        ans += 2
                        return ans
                    elif count > 0:
                        ans = ans + 1 + (count - 1) * 2
                        return ans
                else : #ch_next exits
                    ch_next = s[i]
                    if ch_next == ")":
                        if count == 0:
                            ans += 1
                            i = i + 1
                        elif count > 0:
                            count -= 1
                            i = i + 1
                    else : # ch_next == (
                        if count == 0:
                            ans += 2
                            count += 1 
                            i = i + 1
                        elif count > 0:
                            ans += 1 
                            i = i + 1
        
        if count > 0:
            ans = ans + count * 2
        return ans


