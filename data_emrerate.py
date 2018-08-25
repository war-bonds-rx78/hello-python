file = "./data/data3.txt"

with open(file, "r", encoding="utf_8") as fileobj: 
    for i, line in enumerate(fileobj) :
        if line == "\n" :
            continue
#        asline = line.rstrip()
        asline = line.split(" ")
        print("-"*20)
        print(f"{i}:{asline}")
        for value in asline :
            asValue = value.rstrip()
            print(asValue)