class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topFreq = {}
        result = []
        for num in nums:
            if num not in topFreq:
                topFreq[num] = 1
            else:
                topFreq[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, frequency in topFreq.items():
            freq[frequency].append(num)
        
        
        for i in range(len(freq)-1, 0, -1):
            for f in freq[i]:
                result.append(f)
                if len(result) == k:
                    return result
        return result