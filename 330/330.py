class Solution(object):
    def minPatches(self, nums, n):
        cur_max , ans = 0 , 0
        nums.reverse()
        while(cur_max < n):
            if(len(nums) != 0):
                num = nums.pop()
            else:
                num = n + 1
            while(cur_max < num - 1 and cur_max < n):
                cur_max = 2*cur_max + 1
                ans +=1
            cur_max += num
        #print(ans)
        return ans