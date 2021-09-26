#continue keyword
#used to skip loop step
#used in both for and while


i=int(input('enter a value of i'))
while i>0:
    if i%3==0:
       i-=1
       continue
    print(i)
    i-=1

#without continue

