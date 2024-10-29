'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

=====>

Firstly, we need to finish prerequisites courses before taking a main course so this is a directed graph problem. In other words, this problem can be restated to Detect cycle in a directed graph or similarly Check if a graph is acyclic. (For undirected graphs, check out this article)

Secondly, while edges list together with adjacency list and adjacency matrix are three main ways to represent a graph, it's not commonly used to solve graph problems. One main reason is that to perform a common operation like getting all descendants of a given vertex it takes O(len(edgesList)). Hence, we can first build an adjacency list from the edges list which takes O(1) to perform such operation.

def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList
For a quick reference of graph representation this article might be helpful.

Complexity Analysis
Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.

Space Complexity: O(V + E) the adjacency list dominates our memory usage.

Solution 1: DFS with an array storing 3 different states of a vertex
This solution is from "Introduction to Algorithms" book where it uses 3 different colours instead of 3 states.

It's also similar to this article Python DFS + Memoization where we use an array for Memoization.

    class Solution:
    	def buildAdjacencyList(self, n, edgesList):
    		...
    		
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex is being processed. Either all of its descendants
            #             are not processed or it's still in the function call stack.
            # state 1   : vertex and all its descendants are processed.
            state = [0] * numCourses
    
            def hasCycle(v):
                if state[v] == 1:
                    # This vertex is processed so we pass.
                    return False
                if state[v] == -1:
                    # This vertex is being processed and it means we have a cycle.
                    return True
    
                # Set state to -1
                state[v] = -1
    
                for i in adjList[v]:
                    if hasCycle(i):
                        return True
    
                state[v] = 1
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v):
                    return False
    
            return True
    42/42 cases passed (96 ms)
    Your runtime beats 96.91 % of python3 submissions
    Your memory usage beats 65.31 % of python3 submissions (15.4 MB)
Solution 2: DFS with a stack storing all decendants being processed
Same idea as Solution 1, this time we use a stack to store all vertices being processed. While visiting a descendant of a vertex, if we found it in the stack it means a cycle appears.

This technique is also used to find a Topological order from the graph.

    class Solution:
        def buildAdjacencyList(self, n, edgesList):
            ...
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
            visited = set()
    
            def hasCycle(v, stack):
                if v in visited:
                    if v in stack:
                        # This vertex is being processed and it means we have a cycle.
                        return True
                    # This vertex is processed so we pass
                    return False
    
                # mark this vertex as visited
                visited.add(v)
                # add it to the current stack
                stack.append(v)
    
                for i in adjList[v]:
                    if hasCycle(i, stack):
                        return True
    
                # once processed, we pop it out of the stack
                stack.pop()
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v, []):
                    return False
    
            return True
    42/42 cases passed (100 ms)
    Your runtime beats 92.65 % of python3 submissions
    Your memory usage beats 51.02 % of python3 submissions (16 MB)
'''