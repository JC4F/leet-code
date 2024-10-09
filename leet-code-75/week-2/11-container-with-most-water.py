'''
Solution: O(n)

I've seen some "proofs" for the common O(n) solution, but I found them very confusing and lacking. Some even didn't explain anything but just used lots of variables and equations and were like "Tada! See?". I think mine makes more sense:

Idea / Proof:

The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
Implementation: (Python)

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
'''