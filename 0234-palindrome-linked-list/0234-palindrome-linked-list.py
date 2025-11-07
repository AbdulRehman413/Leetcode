# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
    
        # Step 2: Reverse the list
        reversed_values = values[::-1]
    
        # Step 3: Compare both lists
        return values == reversed_values
        # #  midldle of linked list
        # slow = head
        # fast = head 
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # Reverse LL

        # prev = None 
        # while slow:
        #     nxt = slow.next
        #     slow.next = prev
        #     prev = slow 
        #     slow = nxt

        # # Comparison

        # left = head
        # right = prev 
        # while right:
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next

        # return True

        



        