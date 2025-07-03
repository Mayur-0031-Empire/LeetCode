class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1 # minimum weidth
        L = area # maximum Length
        ans = [L, W]
        i = 1
        while i * i <= area:
            if area % i == 0:
                W = i
                L = area // i
            i += 1
        return [L, W]
