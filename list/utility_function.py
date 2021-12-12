x=[1,3,4,45,57,5,3,4,3,2,3,4,6,7,7,6,6,4,4,4,5,5,6,7,7,7,8,98,7,6,5]
print(x)
print('occurence of 1=',x.count(1))
print('occurence of 2=',x.count(2))
print('occurence of 3=',x.count(3))


a=['newyork','chicago','athens']
b=[12,45,13]
c=['nevada',57,'mussorie',58]
print(a)
a.sort(reverse=True)
print(a)

print(b)
b.sort()
print(b)

y=[1,1,1,1,1,1223,3,3,3,3,3,3]
print(y)
y.reverse()
print(y)

idx=y.index(1223)
print('1223 found at',idx)

z=x.copy()
print(z)
