def middleOne(head):
    slow = head 
    fast = head 
    while fast.next != None: 
        slow = slow.next
         
        fast = fast.next.next 