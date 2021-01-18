from __future__ import annotations
from typing import Optional
from linkedlist import *

class Solution:
    def printNodes(self, head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def merge_two_sorted_list(self, head1, head2):
        P = head1 
        Q = head2 
        S = None
        
        if not P:
            return Q 
        if not Q: 
            return P 
        if P and Q:
            if P.data <= Q.data: 
                S = P 
                P = S.next
            else: 
                S = Q 
                Q = S.next  
            newHead = S
            
        while P and Q: 
            if P.data <= Q.data: 
                S.next = P 
                S = P
                P = S.next 
            else: 
                S.next = Q 
                S = Q 
                Q = S.next

            if not Q: 
                S.next = P 
            if not P: 
                S.next = Q 
            
        return newHead
llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(1)
llist1.append(2)
llist1.append(3)

llist2.append(2)
llist2.append(4)
llist2.append(6)

sol = Solution()

sol.printNodes(sol.merge_two_sorted_list(llist1.head, llist2.head))
# sol.printNodes(llist1.head)