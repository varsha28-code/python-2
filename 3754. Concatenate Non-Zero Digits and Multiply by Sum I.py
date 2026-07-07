class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        x = ""
        digit_sum = 0
        for ch in s:
            if ch != '0':
                x += ch
                digit_sum += int(ch)
        if x == "":
            return 0
        return int(x) * digit_sum
        
