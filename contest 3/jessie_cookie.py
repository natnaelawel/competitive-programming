class Solution:

    def cookies(self, k, A):
        count = 1
        isSweet = False
        A = sorted(A)
        while not isSweet:
            if len(A) < 2:
                return -1
            sweetness = A[0] + 2 * A[1]
            print(sweetness, ' is sweetness')
            if sweetness < k:
                count += 1
                del A[0]
                A[0] = sweetness
                A = sorted(A)
            else:
                isSweet = True

        return count
