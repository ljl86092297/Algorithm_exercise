

a = [2,1]
b = [2,3]
c = zip(a,b)
# print(list(c))
print(sorted(c, key=lambda x:x[0]))
