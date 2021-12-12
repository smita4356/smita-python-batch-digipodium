def avg(number=[]):     #if not decided how many numbers will be passed..
    if number:
        return sum(number)/len(number)
#print(avg(12,32,55,2,52,4))


def stats(*val,action='max'):
    '''function for doing stats like min,max,sum,avg, count etc
    '''
    if val:
        if action=='max':
            return max(val)
        elif action=='min':
            return min(val)
        elif action=='sum':
            return sum(val)
        elif action=='avg':
            return avg(val)
        elif action=='all':
            return max(val),min(val),sum(val)
print('calling stats')
print(stats(1,56,5,3,5,6,1,6,4,6,2,8,6,6))
print(stats(8,5,9,action='sum'))

    
        