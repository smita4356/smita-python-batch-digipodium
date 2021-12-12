'''
1..read a file - open()
2..write a file- open()
3..update a file - open()
open() function has a option to set mode of file
it returns  a file object
'''

file=open('dummy.txt') #existing file
print(file.read())
file.close()

f1=open('radients.txt','w')   #creating a file
f1.write("the radients are saviors of humanity \n")
f1.write("they have sharpable and sharable\n")
f1.write("to be continued\n")
f1.close() #save and close the file

f2=open('dummy.txt','a')   #update a file or append a file
f2.write('\n written by x')
f2.close()