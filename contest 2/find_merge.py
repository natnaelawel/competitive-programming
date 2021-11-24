def findMergeNode(head1, head2):
    stack1 = []
    stack2 = []
    current1 = head1 
    current2 = head2
    
    while current1: 
        stack1.append(current1)
        current1 = current1.next
    while current2: 
        stack2.append(current2)
        current2 = current2.next
    larger = len(stack1) if len(stack1) >= len(stack2) else len(stack2)
    
    last = None
    for i in range(larger):
        if len(stack1) <= 0:
            last = stack2.pop()
            return last
        if len(stack2) <= 0:
            last = stack1.pop()
            return last
        
        node1 = stack1.pop()
        node2 = stack2.pop()
        if node1 is node2:
            last = node1
        else:
            return last.data
            
    