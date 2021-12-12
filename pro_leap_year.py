def is_leap_year(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                return True
            return False
        else:
            return True
    else:   
        return False
for i in range(1900,2021)            
    
            