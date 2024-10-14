input_data = open('input.txt','r') 
n = input_data.read() 
if n[0]=='A' or n[0]=='C' or n[0]=='E' or n[0]=='G' :
    if int(n[1])%2==0:
        output_data = open('output.txt','w')
        output_data.write('WHITE')
    else:
        output_data = open('output.txt','w')
        output_data.write('BLACK')
else:
    if int(n[1])%2==0:
        output_data = open('output.txt','w')
        output_data.write('BLACK')
    else:
        output_data = open('output.txt','w')
        output_data.write('WHITE')
input_data.close()
output_data.close()