import file_function as ff
def sum_digits(number):
    total=0

    

    for digit in str(number):
        total+=int(digit)
    ff.writer('sum_digits.txt',str(total))
sum_digits(44)

