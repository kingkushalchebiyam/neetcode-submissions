class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []

        for num in nums: 
            hashmap[num] += 1
        
        
        sortedKeys = sorted(hashmap, key=hashmap.get, reverse=True)
        
        for i in range(k): 
            res.append(sortedKeys[i])

        return res


        