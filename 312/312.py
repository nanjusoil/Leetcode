class Solution(object):
    def maxCoins(self, nums):
        k = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        Arr =  [[0 for i in range(k+2)] for j in range(k+2)]
        for i in range(2, k+2):
            for j in range(0, k - i  + 2):
                Max = -99999
                for m in range(j + 1, j + i):
                    cur = Arr[j][m] + Arr[m][j + i ] + nums[j] * nums[m] * nums[j + i ]
                    if cur> Max:
                        Max = cur
                        Arr[j][j + i] = Max
        return Arr[0][k+1]