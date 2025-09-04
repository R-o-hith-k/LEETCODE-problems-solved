class Solution(object):
    def combinationSum2(self, candidates, target):
        result=[]
        candidates.sort()
        def back(start,current,total):
            if target==total:
                result.append(list(current))
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if start<i and candidates[i]==candidates[i-1]:
                    continue
                current.append(candidates[i])
                back(i+1,current,total+candidates[i])
                current.pop()
        back(0,[],0)
        return result