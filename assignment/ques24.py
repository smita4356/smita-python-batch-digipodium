#24.Remove all the special characters and numbers from the following string
#text = '%p34@y!*-*!t68h#&on404'
text = '%p34@y!*-*!t68h#&on404'
print(text)
new="".join(c for c in text if c.isalpha())
print(new)

