class Solution(object):
    def jump(self, nums):
        cur_range_start = 0
        cur_range_end = 0
        count = 0
        while(cur_range_end < len(nums) -1):
            #print("cur_range_start: "+ str(cur_range_start) + " cur_range_end:" + str(cur_range_end))
            new_range_end = 0
            for i in range(cur_range_start, cur_range_end + 1):
                new_range_end = max (nums[i] + i , new_range_end)
            cur_range_start = cur_range_end + 1
            cur_range_end = new_range_end
            count +=1
        
        return count