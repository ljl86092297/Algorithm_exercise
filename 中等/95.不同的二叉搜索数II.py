# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def generateTrees(self, n: int):
		def generateTrees(start, end):
			if start > end:
				return [None, ]

			allTrees = []
			for i in range(start, end + 1):
				# 获取所有可行区域左子树集合
				leftTrees = generateTrees(start, i-1)
				# 获取所有可行区域右子树集合
				rightTrees = generateTrees(i + 1, end)

				for l in leftTrees:
					for r in rightTrees:
						currentTrees = TreeNode(i)
						currentTrees.left = l
						currentTrees.right = r
						allTrees.append(currentTrees)
			return allTrees

		return generateTrees(1, n) if n else []

S = Solution()
S.generateTrees(2)