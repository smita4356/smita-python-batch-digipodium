colors=['yellow','green','blue','purple','pink','black','pink']
colors.remove('yellow')
print(colors)
#it is a fatal errror if item not present
#searching value-- always use if condition with remove
if 'jellow' in colors:
    colors.remove('jellow')
print(colors)
if 'pink' in colors:
    colors.remove('pink')
print(colors)

#remove value by idx value-- if idx value not given removes last element
#pop
#the removing value can be stored in a variable
colors.pop(1)
print(colors)

saperated_value=colors.pop(2)
print(colors)
print(saperated_value)

#clear
colors.clear()
print(colors)