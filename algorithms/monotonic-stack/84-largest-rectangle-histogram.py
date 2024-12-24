"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

"""
**********************************************************

A monotonic stack is a special data structure used in algorithmic problem-solving. 
Monotonic Stack maintaining elements in either increasing or decreasing order. 
It is commonly used to efficiently solve problems such as finding the next greater or smaller element in an array etc.

*********************************************************
"""

"""
ideal quite same as trap water  + trick jump from 0(n^2) => 0(n)

for (int i = 1; i < height.length; i++) {              
    int p = i - 1;
    while (p >= 0 && height[p] >= height[i]) {
        p--;
    }
    lessFromLeft[i] = p;              
}

===> 
while (p >= 0 && height[p] >= height[i]) {
      p = lessFromLeft[p];
}


===>
public static int largestRectangleArea(int[] height) {
    if (height == null || height.length == 0) {
        return 0;
    }
    int[] lessFromLeft = new int[height.length]; // idx of the first bar the left that is lower than current
    int[] lessFromRight = new int[height.length]; // idx of the first bar the right that is lower than current
    lessFromRight[height.length - 1] = height.length;
    lessFromLeft[0] = -1;

    for (int i = 1; i < height.length; i++) {
        int p = i - 1;

        while (p >= 0 && height[p] >= height[i]) {
            p = lessFromLeft[p];
        }
        lessFromLeft[i] = p;
    }

    for (int i = height.length - 2; i >= 0; i--) {
        int p = i + 1;

        while (p < height.length && height[p] >= height[i]) {
            p = lessFromRight[p];
        }
        lessFromRight[i] = p;
    }

    int maxArea = 0;
    for (int i = 0; i < height.length; i++) {
        maxArea = Math.max(maxArea, height[i] * (lessFromRight[i] - lessFromLeft[i] - 1));
    }

    return maxArea;
}
"""

# ******** monotonic
"""
https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

"""

"""
====> a litle bit hack for not using 2 for as above

def largestRectangleArea(self, bars: List[int]) -> int:
	st, res = [], 0
	for bar in bars + [-1]: # add -1 to have an additional iteration
		step = 0
		while st and st[-1][1] >= bar:
			w, h = st.pop()
			step += w
			res = max(res, step * h)

		st.append((step + 1, bar))

	return res
"""
