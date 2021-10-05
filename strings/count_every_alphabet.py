from string import ascii_lowercase
content='''If you look around your home, you will find a number of
things used everyday that represent the heritage of Indian
crafts. These may include:
♦ an embroidered cushion or pillow case
♦ a bamboo basket or chair woven with cane
♦ a piece of jewellery
♦ a duree or carpet
♦ a stone bowl
♦ a clay pitcher or surahee, or a lamp or diya
♦ a mat or a broom
♦ a handwoven sare'''
num_of_a=content.count('a')
print(f'a occurs{num_of_a} times')
 

#counting all alphabets
max_freq=0
most_frequent_letter=''

for letter in ascii_lowercase:
    counter=content.count(letter)
    print(f'{letter} found{counter} times')

if max_freq<counter:
    max_freq=counter
    most_freq_letter=letter
print(f'the{most_frequent_letter}has highest frequency:{max_freq}')