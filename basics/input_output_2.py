a=10
b="balls"
c=100
d="rupees"
# printing with comma saperated values
print("raju purchased",a,b,"for",c,d)


#concatenation using +
print('raju purchased ' + str(a) + ' ' +b+ "for" + str(c)+' '+d)


#printing format specifiers
print("raju purchased  %d %s for %d %s" %(a,b,c,d)) 

#print using format() method
print("raju purchased {} {} for {} {}".format(a,b,c,d))




#print using f-string(from version 3.6)
print(f'raju purchased {a} {b} for {c} {d}')


#properties of print
#end-- handles what will be displayed after printing content
#sep-- seperator symbol

#ex--
print('hi',end=' ')
print('there')

#ex sep
print(a,b,c,d)
print(a,b,c,d,sep="xx")