reader = open('input.txt', 'r')
a = int(reader.readline())
b = int(reader.readline())
c = int(reader.readline())
if a + b > c > 0 and a + c > b > 0 and b + c > a > 0:
    res = 'YES'
else:
    res = 'NO'

writer = open("output.txt", 'w')
writer.write(str(res))
writer.close()
