"""special variation of for loop
#where we can check if the for loop completed all iteration or not. 
else block will only execute when all iterattion are completed
"""
num=int(input('enter the number'))
for i in range(2,num):
    if num%i==0:
        print('non prime',num)
        break
else:
    print('prime value',num)