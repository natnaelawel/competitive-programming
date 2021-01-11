def relativeSortArray(arr1, arr2):
    values = dict()
    sortedArray = []
    lastArray = []
    for i in range(len(arr1)): 
        if values.get(arr1[i]):
            values[arr1[i]] += 1
        else:
            values[arr1[i]] = 1
            # if i not in arr2:
                # lastArray.append(arr1[i])

    for num in arr2:
        times = values.get(num)
        for i in range(times):
            sortedArray.append(num) 
        values[num] = 0

    return sortedArray + sorted([x for x in arr1 if x not in arr2])

# arr1 = []
# arr2 = []
# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr1 = [28,6,22,8,44,17]
# arr2 = [2,1,4,3,9,6]
arr2 = [22,28,8,6]

print(relativeSortArray(arr1, arr2))