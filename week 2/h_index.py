def hIndex(citations):
    if len(citations) == 1: 
        if citations[0] == 0:
            return 0
        return 1
    
#    
    citations = sorted(citations, reverse=True)    
    for i in range(0, len(citations)):
        # print(citations[i])
        if citations[i] == len(citations) - i:
            return citations[i] 
    # if len(citations) == 1:
    #     if citations[0] == 0:
    #         return 0
    #     return 1
    # for i in range(0, len(citations)):
    #     if len(citations) > 1:
    #         if citations[i] == 0:
    #             citations.remove(0)
    #         if citations[len(citations) - i - 1] == 0:
    #             citations.pop()
    #         else:
    #             break
    # else: 
    #     return 0
    # citations = sorted(citations, reverse=True)
    # print(citations)
    # n = len(citations)

    # h_index = 0
    # # if current == 0:
    # #     h_index = 0
    # #     n -= 1
    # # print(n, citations)
    # for i in range(0, n):
    #     current = citations[i]
    #     # if current == 0:
    #     #     h_index = 0
    #     #     n -= 1
    #     if current == n - i:
    #         print(current)
    #         h_index = current
    # else:
    #     return h_index
    # return h_index


citations = [3, 0, 6, 1, 5]
citations = []
citations = [0]
citations = [1]
citations = [1, 2]
# citations = [2, 1]
citations = [0, 1]
# citations = [1, 0]
# citations = [0, 0]

print(hIndex(citations))
