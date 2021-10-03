name= 'vijay deenanath chauhan'
print(len(name))
print(name[2],name[3]) #bad idea

print(name[2:5]) #nice one
print(name[6:-8])
print(name[:5])#first five char from starting
print(name[-7:])#last 7 char from -7 to end index

#syntax for slicing
#var[startIdx: endIdx :gap]
print(name[::2]) #start to end with gap of 2 index
print(name[1::2])       #1 index to end with gap of 2 index

# reverse string
print(name[::-1])
print(name[:])
