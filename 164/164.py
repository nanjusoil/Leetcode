import math
class Solution(object):
    def maximumGap(self, nums):
        ans = 0

        if(len(nums) <2):
            return 0
        global_min = float(min(nums))
        global_max = float(max(nums))

        bucket_interval = round( (global_max - global_min)/len(nums), 1) + 0.1
        buckets = [[] for i in range((len(nums)))]
        pre_max = global_min
        
        for i in range(len(nums)):
            buckets[int((nums[i] - global_min) / bucket_interval)].append(nums[i])
        
        for i in range(len(nums)):
            if(len(buckets[i]) > 0):
                ans = max( min(buckets[i]) - pre_max , ans )
                pre_max = max(buckets[i])
                
        return int(ans)