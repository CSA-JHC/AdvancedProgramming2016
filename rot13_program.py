import codecs
un=open('names_pws.txt','r')
en=open('rot13.txt','r+')
for y in un:
    i=y.split()
    print(i)
    e=[]
    e.append(codecs.encode(i[0],'rot13'))
    e.append(codecs.encode(i[1],'rot13'))
    j=' '.join(e)
    print(j)
    en.write(j)
    en.write('\n')
un.close()
en.close()
