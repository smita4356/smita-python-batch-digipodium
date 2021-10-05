'''
calculate the average word length of the following paragraph.
this is a paragraph which is written just for the purpose of providing content 
to let the average word length be calculated'''

para='''this is a paragraph which is written just for the purpose of providing content 
to let the average word length be calculated'''
words=para.split()
average=sum(len(word) for word in words)/ len (words)
print(average)