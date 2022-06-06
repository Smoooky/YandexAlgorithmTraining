reader = open('input.txt', 'r')
tr, tc = [int(n) for n in reader.readline().split(" ")]
res = 0
mode = reader.readline()

if mode == "auto\n":
    res = tc
elif mode == "heat\n":
    if tr < tc:
        res = tc
    else:
        res = tr
elif mode == "freeze\n":
    if tr > tc:
        res = tc
    else:
        res = tr
else:
    res = tr

writer = open("output.txt", 'w')
writer.write(str(res))
writer.close()
