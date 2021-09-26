all_data='' #blank string
while True:
    line=input('~')
    if not line:                #if line is not entered
        break                   # stop loop
    all_data+=line               #add the line to all data
print('your data')
print(all_data)
print('you entered',len(all_data),'chars')