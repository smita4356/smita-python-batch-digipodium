x=[]  #empty list
print('enter 3 value')
for i in range(3):
    val=input('>>')
    x.append(val)
x.append(10)
x.append('helium')
x.append('true')
print(x)

#x.append(1,2,3) gives error
x.append(['a','b','c'])  #append list to end of list
print(x)

#insert function
y=[5,4,5]
y.insert(0,5) #index value should be given, here 0 is index value
print(y)

#extend list
a=[1,2,3,4]
b=[3,4,3]
a.extend(b)
print(a)