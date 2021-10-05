#Ask user to input a string and print how many times e appeared in the string
content=input('enter a sentence or story::')

letter='e'

counter=content.count(letter)
print(f'{letter} found{counter} times')