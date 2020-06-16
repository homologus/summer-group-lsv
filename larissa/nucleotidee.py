f=open('../../small-genome', 'r')
line0=f.readline()
line1=f.readline()
line2=f.readline()
line3=f.readline()

count0=len(line1.rstrip('/n'))
count1=len(line2.rstrip('/n'))
count2=len(line3.rstrip('/n'))

result=count0+count1+count2-3
print(result)


