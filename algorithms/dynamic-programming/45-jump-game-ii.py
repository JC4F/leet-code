"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

"""
# Solution - I (Brute Force) [Rejected]
Time Complexity : O(N!)
Space Complexity : O(N)
int jump(vector<int>& nums, int pos = 0) {
	if(pos >= size(nums) - 1) return 0;        
	int minJumps = 10001;  // initialising to max possible jumps + 1
	for(int j = 1; j <= nums[pos]; j++)  // explore all possible jump sizes from current position
		minJumps = min(minJumps, 1 + jump(nums, pos + j));        
	return minJumps;
}

# Solution - II (Recursive Dynamic Programming - Memoization) [Accepted]
Time Complexity : O(N^2)
Space Complexity : O(N)
int jump(vector<int>& nums) {
	vector<int> dp(size(nums), 10001); // initialise all to max possible jumps + 1 denoting dp[i] hasn't been computed yet
	return solve(nums, dp, 0);
}
// recursive solver to find min jumps to reach end
int solve(vector<int>& nums, vector<int>& dp, int pos) {
	if(pos >= size(nums) - 1) return 0;    // when we reach end, return 0 denoting no more jumps required
	if(dp[pos] != 10001) return dp[pos];    // number of jumps from pos to end is already calculated, so just return it
	// explore all possible jump sizes from current position. Store & return min jumps required
	for(int j = 1; j <= nums[pos]; j++)
		dp[pos] = min(dp[pos], 1 + solve(nums, dp, pos + j));        
	return dp[pos];
}

#  Solution - III (Iterative Dynamic Programming - Tabulation) [Accepted]
Time Complexity : O(N^2)
Space Complexity : O(N)
int jump(vector<int>& nums) {
	int n = size(nums);
	vector<int> dp(n, 10001);
	dp[n - 1] = 0;  // start from last index. No jumps required to reach end if we are already here
	// same as above. For each index, explore all jump sizes and use the one requiring minimum jumps to reach end
	for(int i = n - 2; i >= 0; i--) 
		for(int jumpLen = 1; jumpLen <= nums[i]; jumpLen++) 
			dp[i] = min(dp[i], 1 + dp[min(n - 1, i + jumpLen)]);  // min(n-1, i + jumpLen) for bounds handling
	return dp[0];
}


#  Solution IV (Greedy BFS)
Time Complexity : O(N)
Space Complexity : O(1)
int jump(vector<int>& nums) {
	int n = size(nums), i = 0, maxReachable = 0, lastJumpedPos = 0, jumps = 0;
	while(lastJumpedPos < n - 1) {  // loop till last jump hasn't taken us till the end
		maxReachable = max(maxReachable, i + nums[i]);  // furthest index reachable on the next level from current level
		if(i == lastJumpedPos) {			  // current level has been iterated & maxReachable position on next level has been finalised
			lastJumpedPos = maxReachable;     // so just move to that maxReachable position
			jumps++;                          // and increment the level
	// NOTE: jump^ only gets updated after we iterate all possible jumps from previous level
	//       This ensures jumps will only store minimum jump required to reach lastJumpedPos
		}            
		i++;
	}
	return jumps;
}
"""
