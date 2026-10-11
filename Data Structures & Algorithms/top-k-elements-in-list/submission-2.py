class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = {}
        freq = [[] for _ in range(n+1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(n,0,-1):
            for fnum in freq[i]:
                res.append(fnum)
                if len(res) == k:
                    return res