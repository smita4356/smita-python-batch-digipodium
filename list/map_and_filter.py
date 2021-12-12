x=[12,25,15,45,48,58]
words='python is the best language for coding'.split()
'''
map()-->modern way for mapping a sequence for a operation
filter()--> modern way for filtering a sequence using condition in 1 line

map() and reduce() use lazy objects, in which data is not consuming 
memory until it is casted to a particular datatype like
list, tuple, set 
'''
x2=list(map(lambda i: i**2,x))
print(x2)

y=[2,5,4,9,5,6,4]
xy=list(map(lambda i,j: i+j,x,y))
print(xy)

#another method
f=lambda i,j: i+j
xy=list(map(f,x,y))
print(xy)


#filter
words_with_n=list(filter(lambda i: 'n' in i,words))
print(words_with_n)
