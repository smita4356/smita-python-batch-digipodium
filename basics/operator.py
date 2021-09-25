#python operator

#1. mathematical
#2.logical
#3.assignment
#4. condition
#5.membership
#6.instance


#mathematical
a=10*3
print(a)
a=10*3
print(a)
a=10/3
print(a)
a=10//3   # integer 
print(a)
a=10%3
print(a)
a=10**3
print(a)
a=10+3
print(a)
a=10-3
print(a)


#comparision
a=10
b=3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


#assignment operator
c=15
print(c)
c+=10 # add 10 to existing value of c
print(c)
c-=10
print(c)
c*=10
print(c)
c/=10
print(c)
c//=10
print(c)
c%=10
print(c)
c**=10
print(c)


#logical operator used for multiple operations
#ex
a=5
b=15
c=10
print(a > b and a > c)
print(b >a or b > 100)

print(not a > b)
print(a > b and a < c or a > 10)
print(not(a > b and a < c or a > 10))


# membership operator (in operator)-- it can search a value in a iterable
colors=['red','blue','green','purple','yellow']
print('red' in colors)
print('brown' in colors)
print('orange'in colors)
print(45 in colors)

