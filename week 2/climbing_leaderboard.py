# def climbingLeaderboard(ranked, player):
#     minIndex = 0
#     last_rank = 1
#     last_rank_value = ranked[0]
#     prev_rank_array = []
#     current_rank_array = []
#     maxIndex = len(ranked)
    
#     for i in range(0, len(ranked)):
#         if(ranked[i] == last_rank_value):
#             prev_rank_array.append(last_rank)
#         else:
#             last_rank = last_rank + 1
#             last_rank_value = ranked[i]
#             prev_rank_array.append(last_rank)

#     for i in range(len(ranked)):
#         last_p = player[len(player) - 1]
#         last_r = ranked[len(ranked) - 1 - i]
#         if last_p < ranked[i]:
#             minIndex += 1
#         if last_r < player[0]:
#             maxIndex -= 1
#     for i in range(len(player)):
#         rank = 0
#         for j in range(minIndex, maxIndex):
#             if player[i] >= ranked[j]:
#                 rank = prev_rank_array[j]
#                 break
#             else:
#                 rank = prev_rank_array[maxIndex - 1] + 1
#         current_rank_array.append(rank)
#     return current_rank_array


def climbingLeaderboard(ranked, player):
    last_rank = 1
    last_rank_value = ranked[0]
    prev_rank_array = []
    current_rank_array = []
    for i in range(0, len(ranked)):
        if(ranked[i] == last_rank_value):
            prev_rank_array.append(last_rank)
        else:
            last_rank = last_rank + 1
            last_rank_value = ranked[i]
            prev_rank_array.append(last_rank)

    for i in range(len(player)):
        rank = 0
        for j in range(len(ranked)):
            if player[i] >= ranked[j]:
                rank = prev_rank_array[j]
                break
            else:
                rank = prev_rank_array[-1] + 1
        print(rank)
        current_rank_array.append(rank)
    return current_rank_array

ranked = [100, 90, 90, 80, 60, 50]
# ranked = [100, 100, 50, 40, 40, 20, 10]
player = [90, 80, 105]
# player = [5, 25, 50, 250]


print(climbingLeaderboard(ranked, player))
