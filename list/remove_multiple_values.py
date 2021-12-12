x=[1,2,5,5,6,5,2,6,4,5,5,5,5,2,6,5,3,6,6,6,2,6,5,6,6,
5,5,2,7,5,9,6,3,4,2,5,5,2,5,65,2,6,54,6,2,4,6,2,5]
#remove all 3 in the list
print(x)
z=x.copy()
y=x.count(3)
for i in range (y):
    x.remove(3)
print(x)



#removing all 3s with pop n index
while 3 in z:
    idx=z.index(3)
    z.pop(idx)
print(z)