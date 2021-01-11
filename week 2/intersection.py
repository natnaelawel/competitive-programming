def intersection(list1, list2):
    intersection_list = set()
    for i in list1:
        if i in list2: 
            intersection_list.add(i)
    return list(intersection_list)


nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
