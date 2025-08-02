class Solution(object):
    def plusOne(self, digits):
        number = int(''.join(map(str, digits)))
        number = number + 1
        digits = [int(d) for d in str(number)]
        return digits