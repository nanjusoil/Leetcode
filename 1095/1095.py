class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        ans = 0
        middle = self.middleSearch(0, mountain_arr.length()-1, None, mountain_arr)
        front = self.binarySearchFront(0, middle , target, mountain_arr)
        end = self.binarySearchEnd(middle, mountain_arr.length()-1 , target, mountain_arr)
        if(front == -1):
            return end
        else:
            return front

    def middleSearch(self, left , right, target, mountain_arr):
        while(left < right):
            middle = (left + right) / 2
            if(mountain_arr.get(middle + 1) > mountain_arr.get(middle) ):
                left = middle + 1
            else:
                right = middle
        return left
    
    def binarySearchFront(self, left , right, target, mountain_arr):
        while(left <= right):
            middle = (left + right) / 2
            if(mountain_arr.get(middle) == target):
                return middle
            elif(mountain_arr.get(middle) > target ):
                right = middle - 1
            else:
                left = middle + 1
        return -1
    
    def binarySearchEnd(self, left , right, target, mountain_arr):
        while(left <= right):
            middle = (left + right) / 2
            if(mountain_arr.get(middle) == target):
                return middle
            elif(mountain_arr.get(middle) > target ):
                left = middle + 1
            else:
                right = middle - 1
        return -1