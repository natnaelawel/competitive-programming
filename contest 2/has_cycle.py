def has_cycle(head):
    # first method 
    
    # node_list = []
    # current = head
    # if not head:
    #     return 0
    # if head.next is None:
    #     return 0
    # while current:
    #     if current.data in node_list:
    #         indexof = node_list.index(current.data)
    #         if indexof == len(node_list)-1:
    #             return 1
    #     else:
    #         node_list.append(current.data)
    #     current = current.next 
    # return 0
    
    # second method
    
    slow = head
    fast = head
    # hashset = set()
    isFirst = True
    while slow != fast or isFirst:
        isFirst = False
        if fast is None or fast.next is None:
            return 0
        slow = slow.next 
        fast = fast.next.next
            # hashset.add(current)
        # current = current.next
    return 1
        
        