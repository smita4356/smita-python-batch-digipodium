from string import punctuation
def pro(read_file_path,save_file_path='result.txt'):
    file=open(read_file_path,encoding='utf-8')
    content=file.read()
    file.close()
    for punc in punctuation:
        content=content.replace(punc,'')  #remove every punctutation

#make everything in lowercase and split file in words
    words=content.casefold().split()
    print(f"total words==>{len(words)}")

#create a emptyfile
    file2=open(save_file_path,'w')  #create

#counting words
    for word in set(words):
       count=words.count(word)
       file2.write(f'{word}\t{count}\n')
    file2.close()

pro('franky.txt')