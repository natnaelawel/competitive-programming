#%%
def climbingLeaderboard(ranked, player):
    rank = 1
    playerScore = []
    leaderBoard = ranked
    for i in range(len(player)):
        # leaderBoard = ranked
        j = 0
        while(j < len(leaderBoard)):
            if player[i] > leaderBoard[j]:
                leaderBoard.insert(j, player[i])
                # break
            else:
                leaderBoard.append(player[i])
                # break
            j += 1
        print(leaderBoard)
        print(len(leaderBoard))
        for k in range(len(ranked)):
            pass


climbingLeaderboard([100, 90, 90, 80], [70, 90, 105])
# %%
