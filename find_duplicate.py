class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashnums = set()
        for n in nums:
            if n in hashnums:
                return True
            else:
                hashnums.add(n)
        return False
            
