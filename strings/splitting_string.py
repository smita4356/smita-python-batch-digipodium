msg='we will be seeing the horizon'
words=msg.split()
print(words)

msg2='hi there, how are you? where have you been?'
sentence=msg2.split(',')
print(sentence)
sentence=msg2.split('?')
print(sentence)
sentence=msg2.split('a')
print(sentence)

print(f'we found {len(msg2.split())} words')
print(f'we found {len(words)} words')

msg3='''welcome to wakanda, you will have fun,just dont steal from us, or you will 
no have fun'''
print('normal-->',msg3.split(','))
print('reverse-->',msg3.rsplit(',',maxsplit=2)) #compulsure use of maxsplitwith this