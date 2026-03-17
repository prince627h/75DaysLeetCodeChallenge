class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        
        # Step 1: Count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Bucket list
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        # Step 3: Collect top k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        