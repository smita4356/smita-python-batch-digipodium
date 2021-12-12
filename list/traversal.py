num=list(range(5,15))
for element in num:
    print(element)
words=['this','that','wish','which']
for item in words:
    print(f'{item} is {len(item)} chars')

cords=[[1,2],[2,3],[3,5]]
for i in cords:
    print(i)

for i in cords:
    print(i[0],i[1])

for idx,value in enumerate(words):
    print(f'{idx} has {value}')

for i in num:
    if i %3==0:
        print(i)