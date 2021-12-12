


def hello():
    data=''
    while True:
        line =input('-->')
        if line:
            data+=line+'\n'
        else:
            break
    return data
def write_and_show(filename):
    print('enter some data')
    data=hello()
    file=open(filename,'w+')
    file.write(data)
    file.seek(0)  #go back to starting
    content=file.read()
    file.close()
    print(content)
write_and_show('kiroro.txt')
