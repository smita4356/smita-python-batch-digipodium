'''
trivia
2types of function--
-function that will give output
-function that will change the original variable
'''

name='we are going to have FUN'
print(name)
uname=name.upper()
print('upper-->',uname)

lname=name.lower()
print('lower-->',lname)

n1=name.capitalize()
print('capital-->',n1)

n2=name.title()
print('title-->',n2)

n3=name.swapcase()
print('swap-->',n3)

n4=name.casefold()
print(n4)

word= input('what animal you like::')
spacing=int(input('select a number for spacing'))
print(f'printing{word}with spacing{spacing}')
char=input('enter a char')

lword=word.ljust(spacing,char)
print(lword)
rword=word.rjust(spacing,char)
print(rword)
cword=word.center(spacing,char)
print(cword)

