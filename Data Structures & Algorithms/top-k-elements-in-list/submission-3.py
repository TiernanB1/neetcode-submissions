class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            bucket[n] = 1 + bucket.get(n, 0)
        for n, c in bucket.items():
            freq[c].append(n)

        out = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                out.append(n)
            if len(out) == k:
                return out

           


        
        