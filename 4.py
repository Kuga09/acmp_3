input_data = open('input.txt','r') 
data = input_data.read()  
a=data.split()
S=int(a[0])
P=int(a[1])
print(S)
for i in range(1,1001):
    for j in range(1,1001):
        if i+j==S and i*j==P:
            break
    if i+j==S and i*j==P:
        break
if i>=j:
    output_data = open('output.txt','w')
    output_data.write(str(j)+' '+str(i))
else:
    output_data = open('output.txt','w')
    output_data.write(str(i)+' '+str(j))
input_data.close()
output_data.close()
