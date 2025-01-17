def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid
    return lo if nums[lo] == target else -1
