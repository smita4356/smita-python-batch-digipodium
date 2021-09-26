num=[1,2,3,4,5,19,12]
for i in num:
    print(i)

msg="we are now using loops"
print('characters in msg:',len(msg))
for char in msg:
    print(char)
#traversal
for char in msg:
    if char!=' ':
        print(char)

#numeric loop

for i in range(10):
    print(i,end=',')