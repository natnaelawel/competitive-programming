def rearrange_barcodes(barcodes):
    if len(barcodes) <= 1:
        return barcodes
    rearranged_list = []
    last_item = None
    i = 1
    is_organized = True
    for i in barcodes:
        if i == last_item:
            is_organized = False
            break 
        else:
            last_item = i
    if is_organized: 
        return barcodes
    else: 
        last_item = None

    
    result = []
    result_dict = dict()
    for i in barcodes: 
        if result_dict.get(i):
            result_dict[i] += 1
        else: 
            result_dict[i] = 1
    result_dict = dict(sorted(result_dict.items(), key=lambda x:x[0]))
    barcodes = sorted(barcodes)
    print(result_dict, last_item)
    for k, v in result_dict.items():
        nextIndex = result_dict[k]  #2
        nextItem = barcodes[nextIndex] #1
        while v > 0:
            if k != last_item: 
                rearranged_list.append(k)
                last_item = k 
                nextItem = barcodes[nextIndex]
                v -= 1

            elif result_dict[nextItem] > 0:
                rearranged_list.append(nextItem)
                last_item = nextItem
                result_dict[nextItem] -= 1
            else: 
                v -= 1
        
    return rearranged_list
barcodes = [1,1,1,2,2,2]
barcodes = [1,1,1,1,2,2,3,3]
# barcodes = [1,2,1]
# barcodes = [2,1,1]
# barcodes = [2,2,1,3]

# barcodes = [1]
print(rearrange_barcodes(barcodes))
