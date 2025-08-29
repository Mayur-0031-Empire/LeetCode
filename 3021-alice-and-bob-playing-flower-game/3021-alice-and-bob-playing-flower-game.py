class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n = n // 2
        odd_n = n - even_n

        even_m = m // 2
        odd_m = m - even_m

        return even_n * odd_m + even_m * odd_n
