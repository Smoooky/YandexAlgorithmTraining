reader = open('input.txt', 'r')
a = int(reader.readline())
b = int(reader.readline())
c = int(reader.readline())
reader.close()
if a == b == c == 0:
    res = 'MANY SOLUTIONS'
elif c < 0:
    res = 'NO SOLUTION'
elif a == 0:
    if b == (c*c):
        res = 'MANY SOLUTIONS'
    else:
        res = 'NO SOLUTION'
else:
    res = float((c*c - b)/a)
    if res.is_integer():
        res = int(res)
    else:
        res = 'NO SOLUTION'
writer = open('output.txt', 'w')
writer.write(str(res))
writer.close()
