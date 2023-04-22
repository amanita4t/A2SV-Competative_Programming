class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target = int(target)
        for i in range(len(nums) -1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        target_indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                target_indices.append(i)
        return target_indices
