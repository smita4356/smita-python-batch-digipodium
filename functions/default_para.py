def summer(a,b,c,d=0):   #if value of d is not given by user it automaticly be 0
    return a+b+c+d
print(summer(1,2,3,4))
print(summer(2,3,4))
print(summer(1,2,3,d=4))
#always put default parameters after required parameters