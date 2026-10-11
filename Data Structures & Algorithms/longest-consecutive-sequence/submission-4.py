from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        lookup = defaultdict(int)

        for num in nums:
            lookup[num] = 1

        res = 0

        for num in lookup:
            if lookup[num]:
                lt = num-1
                rt = num+1
                tres = 1
                while lt in lookup:
                    tres += 1
                    lookup[lt] = 0
                    lt -= 1
                while rt in lookup:
                    tres += 1
                    lookup[rt] = 0
                    rt += 1
                res = max(res, tres)

        return res            


            



        

        