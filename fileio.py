f = open("C:\\Users\\whkel\\Desktop\\car.txt", "r")

for line in f:
    orientation, row, col, size = line.split(", ")
    orientation =str(orientation)
    row = int(row)
    col = int(col)
    size = int(size)
    print(orientation)
    print(row)
    print(col)
    print(size)


f.close()

