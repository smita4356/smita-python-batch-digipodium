# string find function allws us to pass the starting index and stop index

data='''what are the codes for the safe? how safe is the safe?
is the safe really safe?'''
start_idx=0
for i in range(5):   #use str.count() for better output
    idx=data.find('safe',start_idx)
    print(f'safe word found at {idx}')
    start_idx=idx+1

#best method
print('using while loop')
start_idx=0
while True:
    idx=data.find('safe',start_idx)
    if idx==-1:
        break
    print(f'safe found at {idx}')
    start_idx=idx+1