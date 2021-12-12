'''syntax.-->
newlist=[operation loop- for- existing list !condition!  ]

'''
x=[2,5,9,5,1,6,4,5,2,6,4,6,3]
#mapping
x2=[i**2 for i in x]
print(x)
print(x2)

#filter
x_odd=[i for i in x if i %2!=0]
print(x_odd)

x_odd_sqrs=[i**2 for i in x if i%2!=0]
print(x_odd_sqrs)