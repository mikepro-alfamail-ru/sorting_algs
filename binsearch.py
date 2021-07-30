def search(self, nums: list, target: int) -> int:
    def binsearch(start, end):
        if end == start:
            return end if nums[end] == target else -1
        else:
            center = start + (end - start) // 2
            return center if nums[center] == target \
                else binsearch(center + 1, end) if target > nums[center] \
                else binsearch(start, center)

    return binsearch(self, 0, len(nums) - 1), self.recurcivecount
