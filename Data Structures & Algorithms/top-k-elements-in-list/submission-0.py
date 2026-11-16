class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for number in nums:
            count[number] = 1 + count.get(number,0)
        for number, c in count.items():
            frequency[c].append(number)

        result = []
        for i in range (len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result)==k:
                    return result