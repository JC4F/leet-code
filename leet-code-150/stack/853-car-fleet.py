"""
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
"""

"""
Vehicle 1 is the closest to the target, therefore, it will definitely lead a fleet since no one behind
it can pass it. The initial position of vehicle 2 is a little farther away than vehicle 1, 
but its speed is faster (steeper slope). Ideally, if vehicle 1 does not exist, vehicle 2 
will arrive at the target before t1. However, since in reality vehicle 1 is in front of it, 
it will join the fleet led by vehicle 1 at the black point. For vehicle 3, its ideal arrival 
time (dist/vel) is larger than the fleet in front of it, so itself will form a flee
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_t = None
        n = 0
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            t = dist / vel
            if not prev_t or t > prev_t:
                prev_t = t
                n += 1
        return n


"""
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


list(zip(position, speed))  # [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]

sorted(zip(position, speed))  # [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]

sorted(zip(position, speed))[::-1]  # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]

"""
