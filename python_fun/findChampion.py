from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize indegree array
        indegree = [0] * n

        # Step 2: Update indegree array based on edges
        for edge in edges:
            indegree[edge[1]] += 1

        # Step 3: Find the node with no incoming edges (indegree 0)
        champion = -1
        for i in range(n):
            if indegree[i] == 0:
                if champion == -1:
                    champion = i  # Found a potential champion
                else:
                    return -1  # Found more than one node with indegree 0, return -1

        return champion


class SolutionTwo:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indexer = [0] * n
        [indexer.__setitem__(v, indexer[v] + 1) for _, v in edges]
        return -1 if indexer.count(0) != 1 else indexer.index(0)
