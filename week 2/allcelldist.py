def allCellsDistOrder(R, C, r0, c0):
    result = []
    result_dict = {}
    for r in range(R):
        for c in range(C):
            rank = abs(r0 - r) + abs(c0 - c)
            if result_dict.get(rank):
                result_dict[rank] = result_dict[rank] + [[r, c]]
            else: 
                result_dict[rank] = [[r, c]]
    for k, v in  sorted(result_dict.items()):
        for i in v:
            result.append(i)
    return result

R = 1
C = 2
r0 = 0
c0 = 0

R = 2
C = 2
r0 = 0
c0 = 1

R = 2
C = 3
r0 = 1
c0 = 2
print(allCellsDistOrder(R, C, r0, c0))