#wap to find the sum of all value in a list
total=0
x=[3,4,5,6,3,4]
for i in x:
    total+=i
print(x,'>>total=',total)

#short version
total=sum(x)
print(total)

x_max=max(x)
print(x_max)

x_min=min(x)
print(x_min)

x_mean=sum(x)/len(x)
print(x_mean)