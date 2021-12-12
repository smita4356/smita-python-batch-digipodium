content='helo this mh hello  hello nyebjf hello'
words=content.split()
max_freq=0
mx_occ_word=''
for item in words:
    count=words.count(item)
    print(f'{item}-->{count}')
    if count>max_freq:
        max_freq=count
        mx_occ_word=item
print(f'{mx_occ_word}=>>{max_freq}')