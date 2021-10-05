content='''If you look around your home, you will find a number of
things used everyday that represent the heritage of Indian
crafts. These may include:
♦ an embroidered cushion or pillow case
♦ a bamboo basket or chair woven with cane
♦ a piece of jewellery
♦ a duree or carpet
♦ a stone bowl
♦ a clay pitcher or surahee, or a lamp or diya
♦ a mat or a broom'''
vowels='aeiou'
for vowel in vowels:
    c=content.casefold().count(vowel)
    print(f'{vowel}->{c} times')