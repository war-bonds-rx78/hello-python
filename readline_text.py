file = "./data/data2.txt"
with open (file, "r", encoding="utf_8") as fileobj :
    while True : 
        line = fileobj.readline()
        asline = line.rstrip()
        if asline :
            print(asline)
        else :
            break