#wap to take user input to create a list
#the user should decide the size of list
#the list should be numeric
#display list value amd sum,min , mean of the list
limit=int(input('enter the length of list>>'))
x=[]
for i in range(limit):
    val=int(input('>>'))
    x.append(val)
print('you entered the values')
print(x)
print('sum>>',sum(x))
print('max value>>',max(x))
print('min value',min(x))
print('mean value',sum(x)/len(x))


    

  