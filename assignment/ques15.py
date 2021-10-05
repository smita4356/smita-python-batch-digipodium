#Ask user to input a sentence and print each word on a different line
msg=input('enter a sentence::')
print(msg)
print('print each word on different line-->')
print(*msg.split(),sep='\n')