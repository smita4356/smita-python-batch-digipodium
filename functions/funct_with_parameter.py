def prime_num(number):
    for i in range(2,number):
        if number % i==0:
            print('not prime')
            break
    else:
         print('prime')
       
prime_num(5)
prime_num(10)
