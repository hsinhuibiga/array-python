#Squares of a Sorted Array

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        j = 0  # i, j，表示兩個指針，分別從正負界限，指向負數部分，和正數部分
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        res = []
        while 0 <= i and j < N:  # 歸併操作, 誰的平方小，誰先輸出
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1

        while i >= 0:  # 如果，負數部分沒有輸出完，則直接輸出
            res.append(A[i]**2)
            i -= 1
        while j < N:  # 如果，正數部分沒有輸出完，則直接輸出
            res.append(A[j]**2)
            j += 1

        return res


if __name__ == '__main__':
    solu = Solution()
    A = [4, 5, 0, -2, -3, 1]
    print(solu.sortedSquares(A))