def size (item) :
    sizeList = ["XS", "S", "M", "L"]
    pos = sizeList.index(item)
    return pos

data = ["S", "M", "XS", "L", "M", "M"]
data.sort(key = size)
print(data)