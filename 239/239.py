class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue,ans = [], []
        for i in range(len(nums)):
            while(True):
                if(queue and ( i - queue[0]) >= k ):
                    queue.pop(0)
                else:
                    break;
            while(True):
                if(queue and nums[i] > nums[queue[-1]]):
                     queue.pop(-1)
                else:
                    break;
            queue.append(i)
            if(i>=k-1):
                ans.append(nums[queue[0]])
        return ans
