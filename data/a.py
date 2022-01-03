with open('train_expr.txt') as f:
	xs = f.readlines()
with open('train_res.txt') as f:
	ys = f.readlines()

mp = {}

for x,y in zip(xs,ys):
	mp[(x,y)]=0

for x,y in zip(xs,ys):
	mp[(x,y)]+=1

print(mp)
'''
lns = list(map(lambda x:x.split()[0]+'\n',lns))

with open('train_expr_1.txt','w') as f:
	f.writelines(lns)
'''