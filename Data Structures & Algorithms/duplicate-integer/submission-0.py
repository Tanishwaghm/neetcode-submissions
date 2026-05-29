class Solution(object):
    def hasDuplicate(self, nums):
        a=set()
        for num in nums:
            if num in a:
                return True
            a.add(num)
        return False

        