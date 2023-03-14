import collections


class Solution:
    def totalFruit(self, tree: List[int]):
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res


trees = [[1, 2, 1], [0, 1, 2, 2], [1, 2, 3, 2, 2]]

for i in trees:
    print(Solution().totalFruit(i))
