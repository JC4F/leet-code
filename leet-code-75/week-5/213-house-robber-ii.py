"""
Improve House Robber => circel => first and end can't be robbed

=>public int rob(int[] nums) {
    if (nums.length == 1) return nums[0];
    return Math.max(rob(nums, 0, nums.length - 2), rob(nums, 1, nums.length - 1));
}
"""
