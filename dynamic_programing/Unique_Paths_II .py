# https://leetcode.com/problems/unique-paths-ii/?envType=problem-list-v2&envId=dynamic-programming
from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ans = 0
        mem = {}
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        def calc(x, y):
            # Bài toán yêu cầu đếm số đường đi --> kiểu trả về là kiểu int
            nonlocal ans
            if x >= row or y >= col or obstacleGrid[x][y] == 1:
                return 0
            if x == row - 1 and y == col - 1:
                return 1
            if (x, y) in mem:
                return mem[(x, y)]
            move_right = calc(x + 1, y)
            move_down = calc(x, y + 1)
            mem[(x, y)] = move_right + move_down
            return mem[(x, y)]

        return calc(0, 0)


if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.uniquePathsWithObstacles(grid))