#20.Ask user to input string, print found if any of the character is upper case
text=input('enter a string::')
ans=text.isupper()
print(ans)
if ans==True:
    print('found')
