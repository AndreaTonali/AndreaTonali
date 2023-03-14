# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = l1 
        b = l2 
        arr1 = []
        arr2 = []
    
        while a.next is not None:
          arr1.append(a.val)
          a = a.next
        arr1.append(a.val)
    
        while b.next is not None:
          arr2.append(b.val)
          b = b.next
        arr2.append(b.val)
        
        invertedl1 = arr1[::-1]
        invertedl2 = arr2[::-1]
        
        invertedl1_to_str = [str(i) for i in invertedl1]
        invertedl2_to_str = [str(i) for i in invertedl2]

        inverted1 = int("".join(invertedl1_to_str))
        inverted2 = int("".join(invertedl2_to_str))

        total = list(str(inverted1 + inverted2))
        head = l3 = ListNode(total.pop())

        # total_inverted = [int(i) for i in str(total)][::-1]
        total_inverted = total[::-1]
        
        for i in total_inverted:
            l3.next = ListNode(i)
            l3 = l3.next

        return head 

