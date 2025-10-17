class Solution(object):
    def isPalindrome(self, s):
        temp = []
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        clean = ''.join(temp)
        reverse = temp[::-1]
        if reverse == temp:
            return True
        return False

        # temp = []
        # for i in s:
        #     if i.isalnum():
        #         temp.append(i.lower())
        #     merge = ''.join(temp)
        #     reverse = temp[::-1]
        #     if reverse == temp:
        #         return True
        #     return False
       
       

        