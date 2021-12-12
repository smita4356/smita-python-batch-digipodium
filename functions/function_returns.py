def hypotaneous(p,b):
    hyp=(p**2+b**2)**.5
    return hyp
#answer can be stored
ans=hypotaneous(3,4)
print('answer',ans)
#answer can be used in expressions
out=hypotaneous(3,4)+hypotaneous(4,5)
print(out)
#can be directly printed if no variable is needed
print(hypotaneous(10,10))