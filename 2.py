input_data = open('input.txt','r') 
data = input_data.readlines()  
a=data[0]
b=data[1]
c=data[2]
d=data[3]
a=a.split()
b=b.split()
c=c.split()
d=d.split()
a1=int(a[0])
b1=int(a[1])
a2=int(b[0])
b2=int(b[1])
a3=int(c[0])
b3=int(c[1])
a4=int(d[0])
b4=int(d[1])
s1=a1+a2+a3+a4
s2=b1+b2+b3+b4
if s1>s2:
    output_data = open('output.txt','w')
    output_data.write('1')
elif s1<s2:
    output_data = open('output.txt','w')
    output_data.write('2')
else:
    output_data = open('output.txt','w')
    output_data.write('DRAW')
input_data.close()
output_data.close()