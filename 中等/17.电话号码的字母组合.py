class Solution:
	def letterCombinations(self, digits: str):
		if len(digits) == 0:
			return []
		phonemap = {'2':"abc", '3': "def", '4': "ghi", '5': "jkl", '6':"mno", '7': "pqrs", '8': "tuv", '9':"wxyz"}


		def backtrack(index):
			if index == len(digits):
				conmbinations.append("".join(conmbination))
			else:
				digit = digits[index]
				for letter in phonemap[digit]:
					# 这里的关键就是添加字符以后  当backtrack最后一层执行完毕以后往回退的时候， 再删除上一次添加的字符就能进入新的递归。
					conmbination.append(letter)
					backtrack(index+1)
					conmbination.pop()
		conmbination = []
		conmbinations = []
		backtrack(0)
		return conmbinations