"""
Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
"""

"""
1. Backtracking (Brute Force)
"""


class Solution:
    def combinationSum2(self, candidates, target):
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            generate_subsets(i + 1, cur, total + candidates[i])
            cur.pop()

            generate_subsets(i + 1, cur, total)

        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]


"""
2. Backtracking 
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


"""
3. Backtracking (Optimal)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res
