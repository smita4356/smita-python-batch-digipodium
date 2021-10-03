value=input('enter something>>')
ans=value.isupper()
print('is the value entrered is upper::',ans)

ans=value.islower()
print('is the value entrered is lower::',ans)


ans=value.isalpha()
print('is the value contains only alphabet::',ans)


ans=value.isnumeric()
print('is the value contains only numbers::',ans)


ans=value.isspace()
print('is the value contains only space::',ans)


ans=value.isprintable()
print('is the value printable on screen::',ans)


ans=value.isdigit()
print('is the value contains only digits::',ans)


ans=value.isdecimal()
print('is the value contains decimal numbers::',ans)

name='dr.ram verma'
if name.startswith('dr'):
    print('hello doctor')
    


if name.startswith('mr'):
    print('hello mister')


file=input('enter the filename:')
if file.endswith('.exe'):
    print(f"{file}is application file")
elif  file.endswith('.doc'):
    print(f"{file}is word  file")
elif  file.endswith('.pdf'):
    print(f"{file}is PDF file")
elif  file.endswith('.png'):
    print(f"{file}is image file")
else:
    print('invalid')
