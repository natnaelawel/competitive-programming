def reOrganizeString(S):
    if len(S) <= 1:
        return S
    rearranged_list = []
    rearranged_str = ""
    last_item = None
    i = 1
    is_organized = True
    result = []
    result_dict = dict()
    for i in S: 
        if result_dict.get(i):
            result_dict[i] += 1
        else: 
            result_dict[i] = 1
    result_dict = dict(sorted(result_dict.items(), key=lambda x:x[0]))
    S = sorted(S)
    print(result_dict)
    print(S)
    for k, v in result_dict.items():
        nextIndex = result_dict[k]  #2
        nextItem = S[nextIndex] #1
        while v > 0:
            if k != last_item: 
                # rearranged_list.append(k)
                rearranged_str += k
                last_item = k 
                # nextItem = S[nextIndex]
                v -= 1

            elif result_dict[nextItem] > 0:
                # rearranged_list.append(nextItem)
                rearranged_str += nextItem
                last_item = nextItem
                result_dict[nextItem] -= 1
            else: 
                v -= 1
    for i in rearranged_str:
        if i == last_item:
            is_organized = False
            break 
        else:
            last_item = i
    if is_organized: 
        return rearranged_list
    else: 
        last_item = ""

    # return rearranged_list
    return rearranged_str
print(reOrganizeString("aaab"))