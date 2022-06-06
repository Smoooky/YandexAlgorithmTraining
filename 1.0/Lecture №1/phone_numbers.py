reader = open('input.txt', 'r')
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
prefix = ['7', '4', '9', '5']
ph_list = [reader.readline(), reader.readline(), reader.readline(), reader.readline()]
reader.close()
cor_list = []
for j in ph_list:
    correct_number = []
    count = 0
    for i in j:
        if i in num_list:
            correct_number.append(i)
    if len(correct_number) == 7:
        correct_number = prefix + correct_number
    if correct_number[0] == '8':
        correct_number[0] = '7'
    cor_list.append(correct_number)
writer = open('output.txt', 'w')
if cor_list[0] == cor_list[1]:
    writer.write('YES\n')
else:
    writer.write('NO\n')
if cor_list[0] == cor_list[2]:
    writer.write('YES\n')
else:
    writer.write('NO\n')
if cor_list[0] == cor_list[3]:
    writer.write('YES\n')
else:
    writer.write('NO\n')
writer.close()
