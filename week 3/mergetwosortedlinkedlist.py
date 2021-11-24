# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        smaller, larger = (l1, l2) if self.count(
            l1) <= self.count(l2) else (l2, l1)
        firstValue, l1LessthanL2 = (
            smaller.val, True) if smaller.val <= larger.val else (larger.val, False)

        smallerSize = self.count(smaller)
        sortedNodeHead = ListNode(firstValue)
        currentSorted = sortedNodeHead
        currentSmaller = smaller
        currentLarger = larger
        if l1LessthanL2 == True:
            currentSmaller = smaller.next
        else:
            currentLarger = larger.next
        i = 0
        while i <= smallerSize:
            if i == 0:
                sortedNodeHead = ListNode(firstValue)
                currentSorted = sortedNodeHead
            elif currentSmaller.val <= currentLarger.val:
                sortedNewNode = ListNode(currentSmaller.val)
                currentSorted.next = sortedNewNode
                currentSorted = currentSorted.next
                currentSmaller = currentSmaller.next
            else:
                sortedNewNode = ListNode(currentLarger.val)
                currentSorted.next = sortedNewNode
                currentSorted = currentSorted.next
                currentLarger = currentLarger.next
                i -= 1
            i += 1
        while currentLarger != None:
            sortedNewNode = ListNode(currentLarger.val)
            currentSorted.next = sortedNewNode
            currentSorted = currentSorted.next
            currentLarger = currentLarger.next

        self.printNodes(currentLarger)
        
        return sortedNodeHead

    def printNodes(self, head):
        while head:
            print(head.val, end=", ")
            head = head.next
        print("")

    def count(self, head: ListNode) -> int:
        i = 0
        c = head
        while c:
            c = c.next
            i += 1
        return i


newNode5 = ListNode(5)
newNode4 = ListNode(4, newNode5)
newNode3 = ListNode(3, newNode4)
newNode2 = ListNode(2, newNode3)
newNode1 = ListNode(1, newNode2)


newNode6 = ListNode(8)
newNode7 = ListNode(7, newNode6)
newNode8 = ListNode(4, newNode7)
newNode9 = ListNode(2, newNode8)
newNode10 = ListNode(1, newNode9)
newNode11 = ListNode(0, newNode10)

# newNode4 = ListNode(4)
# newNode2 = ListNode(2, newNode4)
# newNode1 = ListNode(1, newNode2)


# newNode6 = ListNode(4)
# newNode7 = ListNode(3, newNode6)
# newNode8 = ListNode(1, newNode7)


solution = Solution()
# solution.printNodes(solution.mergeTwoLists(newNode1, newNode8))
solution.printNodes(solution.mergeTwoLists(newNode1, newNode11))

























# print(currentLarger.val, currentSmaller.val, firstValue, l1LessthanL2)
# self.printNodes(currentLarger)
# self.printNodes(currentSmaller)
# print("current")
# self.printNodes(sortedNodeHead)
# print("smaller")
# self.printNodes(currentSmaller)
# print("larger")
# self.printNodes(currentLarger)
# print(currentSmaller.val, ' is current smaller val')
# print(currentLarger.val, ' is current large val')
