class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
		overlap_points = defaultdict(int)
		upper_ones, lower_ones, n = [], [], len(img1)
		ans = 0
		for i in range(n):
			for j in range(n):
				if img1[i][j] == 1:
					upper_ones.append((i, j))
				if img2[i][j] == 1:
					lower_ones.append((i,j))
		for x1, y1 in upper_ones:
			for x2, y2 in lower_ones:
				translate_point = (x1-x2, y1-y2)
				overlap_points[translate_point] += 1
				ans = max(ans, overlap_points[translate_point])
		return ans