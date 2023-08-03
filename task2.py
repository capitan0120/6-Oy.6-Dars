class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        s, n = '', abs(num)
        while n:
            frac = n % 7
            n = n // 7
            s = str(frac) + s
        if num < 0:
            s = '-' + s
        return s