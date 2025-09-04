class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        start=0
        current=[]
        total=0
        def back(start,current,total):
            if total==target:
                result.append(list(current))
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                back(i,current,total+candidates[i])
                current.pop()
        back(0, [], 0)
        return result

