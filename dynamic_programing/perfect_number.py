# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?page=1&difficulty=Medium&sortBy=submissions
from typing import *

class Solution:
    def perfectSum(self, arr, target):
        mem = {}
        def calc(pos, remain):
            if pos < 0:
                return 1 if remain == 0 else 0 # số cách chọn
            if (pos, remain) in mem:
                return mem[(pos, remain)]
            skip = calc(pos-1, remain)
            choose = 0
            if remain >= arr[pos-1]:
                choose = calc(pos-1, remain - arr[pos-1])
            mem[(pos, remain)] = skip + choose
            return mem[(pos, remain)]

        return calc(len(arr) - 1, target)

if __name__ == "__main__":
    sol = Solution()
    arr = [int(i) for i in input().split()]
    target = int(input())
    print(sol.perfectSum(arr,target))