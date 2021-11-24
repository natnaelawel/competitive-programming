def kClosest(points, K):
    result_dict = {}
    result_array = []
    if len(points) ==K: 
        return points
    for i in range(len(points)):
        x, y = points[i]
        result = x ** 2 + y ** 2
        if result_dict.get(result):
            result_dict[result] += [[x, y]]
        else:
            result_dict[result] = [[x, y]]
    result_dict = dict(sorted(result_dict.items(), key=lambda x: x[0]))
    values = list(result_dict.values())
    return [j for i in values for j in i][:K]

points = [[1, 3], [-2, 2]]
points = [[0,1],[1,0]]
points = [[1,3],[-2,2],[2,-2]]
K = 2
print(kClosest(points, K))
