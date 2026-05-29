class Solution:
    def topKFrequent(self, nums,k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # STEP 2: sort by frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # STEP 3: take top k
        return sorted_nums[:k]

        