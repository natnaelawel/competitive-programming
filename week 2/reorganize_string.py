# def reOrganizeString(S):
#     if len(S) <= 1:
#         return S
#     rearranged_list = []
#     rearranged_str = ""
#     last_item = None
#     i = 1
#     is_organized = True
#     result = []
#     result_dict = dict()
#     for i in S: 
#         if result_dict.get(i):
#             result_dict[i] += 1
#         else: 
#             result_dict[i] = 1
#     result_dict = dict(sorted(result_dict.items(), key=lambda x:x[0]))
#     S = sorted(S)
#     print(result_dict)
#     print(S)
#     for k, v in result_dict.items():
#         nextIndex = result_dict[k]  #2
#         nextItem = S[nextIndex] #1
#         while v > 0:
#             if k != last_item: 
#                 # rearranged_list.append(k)
#                 rearranged_str += k
#                 last_item = k 
#                 # nextItem = S[nextIndex]
#                 v -= 1

#             elif result_dict[nextItem] > 0:
#                 # rearranged_list.append(nextItem)
#                 rearranged_str += nextItem
#                 last_item = nextItem
#                 result_dict[nextItem] -= 1
#             else: 
#                 v -= 1
#     for i in rearranged_str:
#         if i == last_item:
#             is_organized = False
#             break 
#         else:
#             last_item = i
#     if is_organized: 
#         return rearranged_list
#     else: 
#         last_item = ""

#     # return rearranged_list
#     return rearranged_str
# print(reOrganizeString("aaab"))

from collections import Counter
import heapq
def reOrganizeString(s):
    pq = [(-cnt, ch) for ch, cnt in Counter(s).items()]
    heapq.heapify(pq)
    
    # to check for if a count greater than the half of the list 
    # if any(-nc > (len(s) + 1)/ 2 for nc, _ in pq):
    if  -pq[0][0] > (len(s) + 1) / 2: return "no"
    print(pq)
    ans = []
    while len(pq) >= 2:
        nct1, ch1 = heapq.heappop(pq)
        nct2, ch2 = heapq.heappop(pq)
        ans.extend([ch1, ch2])
        if nct1 != -1:
            heapq.heappush(pq, (nct1 + 1, ch1))
        if nct2 != -1:
            heapq.heappush(pq, (nct2 + 1, ch2))
    return "".join(ans) + (pq[0][1] if pq else "")
# reOrganizeString("aaab")
# reOrganizeString("aabbb")
print(reOrganizeString("aabbb"))


    
    
    
    
    