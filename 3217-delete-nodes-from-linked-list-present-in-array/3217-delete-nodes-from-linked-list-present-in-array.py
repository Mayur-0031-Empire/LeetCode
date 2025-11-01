# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        for num in nums :
            d[num] = 1
        
        prev = None
        curr = head
        while curr:
            if curr.val in d:
                if prev :
                    prev.next = curr.next
                    curr = curr.next
                else :
                    curr = curr.next
                    head = curr
                    
            else :
                prev = curr
                curr = curr.next
        return head


        