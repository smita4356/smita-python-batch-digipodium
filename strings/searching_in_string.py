msg='once upon a time, there was a kingdom. the king was richard'
idx=msg.find('time')
print(f'time was found at index{idx}')
idx=msg.find('queen')
print(f'queen was found at index{idx}')
if idx==-1:
    print('not found')


#find function gives -1 if word is not available

#find and index are same in functionality except index gives fatal error

idxking=msg.index('king')
print(f'king found at index {idxking}')
'''
idxqueen=msg.index('queen')
print(f'queen not found at {idxqueen}')
this gives error bcoz queen is not available
'''