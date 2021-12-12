#22.In the following string, add aye in the end of every word and print the results.
#text = 'this is some text'
text = 'this is some text'
print(text)
text='this is some text'
for word in text.split():
    print(word,'aye',sep='', end=' ')
