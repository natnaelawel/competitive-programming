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

    result_dict_array = []
    for a,b in result_dict.items():
        result_dict_array.append([a,b])
    rearranged_list = [0]*len(barcodes)
    result_dict_array = sorted(result_dict_array,key=lambda v:v[1])
    i = 0
    while i <len(rearranged_list):
        rearranged_list[i] = result_dict_array[-1][0]
        result_dict_array[-1][1]-=1
        if result_dict_array[-1][1]==0:
            result_dict_array.pop()
        i+=2
    i=1
    while i < len(rearranged_list):
        rearranged_list[i] = result_dict_array[-1][0]
        result_dict_array[-1][1]-=1
        if result_dict_array[-1][1]==0:
            result_dict_array.pop()
        i+=2

   
    return rearranged_list
barcodes = [1,1,1,2,2,2]
barcodes = [1,1,1,1,2,2,3,3]
# barcodes = [1,2,1]
# barcodes = [2,1,1]
# barcodes = [2,2,1,3]

# barcodes = [1]
print(rearrange_barcodes(barcodes))
