x11=input()
y11=""
l=[]
for t in x11:
	l.append(x11.count(t))
min1=min(l)
for t in x11:
	if x11.count(t)==min1 and t!=" ":
		y11=y11+t.lower()+" "
print(y11.strip())
