input_data = open('input.txt','r') # Открываем для чтения файл
n = input_data.read() # Читаем в другую переменную содержимое всего файла
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
    output_data = open('output.txt','w')
    output_data.write('YES')
else:
    output_data = open('output.txt','w')
    output_data.write('NO')
input_data.close()
output_data.close()
