class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        arr=[]
        for row in range(n):
            for col in range(n):
                arr.append(matrix[row][col])
        arr.sort()
        for i in range(len(arr)):
            return arr[k-1]

        