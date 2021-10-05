text='hello this is my text'
print(text)
vowels=['a','e','i','o','u']
newtext=""
textlen=len(text)
for i in range(textlen):
    if text[i] not in vowels:
        newtext=newtext+text[i]
print('string after removing vowels-->')
text=newtext
print(text)

