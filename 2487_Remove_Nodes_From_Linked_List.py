# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # max_val
        #lets try it by revers it 
        #tehn we can check revove what should be removed 
        # then we can revers ut back again 
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        temp = head
        max_val = head.val
        while temp and temp.next:
            if temp.next.val < max_val:
                temp.next = temp.next.next
            else:
                temp = temp.next
                max_val = temp.val
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev
