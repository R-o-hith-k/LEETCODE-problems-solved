class Solution(object):
    def canPartition(self, nums):
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        curr_sum=0
        mem={}
        def back(i,curr_sum):
            if curr_sum==target:
                return True
            if i==len(nums) or curr_sum>target:
                return False
            if (i,curr_sum) in mem:
                return mem[(i,curr_sum)]
            if back(i+1,curr_sum+nums[i]):
                mem[(i,curr_sum)]=True

                return True
            if back(i+1,curr_sum):
                mem[(i,curr_sum)]=True
                return True
            mem[(i,curr_sum)]=False
            return False
        return back(0,0)