class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for i in nums for digit in str(i)]
