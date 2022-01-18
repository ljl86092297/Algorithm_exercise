class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		else:
			direction = False

			dp = [[""] * len(s)for i in range(numRows)]
			print(dp)
			ind, col = 0, 0
			for i, cont in enumerate(s):
				print(ind, col)
				dp[ind][col] = cont
				if i % (numRows -1) == 0:
					direction = not direction
				# elif i % ((numRows -1 )*2) == 0:
				# 	direction = not direction
				if direction:
					ind += 1
				else:
					ind -= 1
					col += 1
			a = ""
			for i in range(len(dp)):
				for j in range(len(dp[i])):
					a += dp[i][j]
			return a


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
