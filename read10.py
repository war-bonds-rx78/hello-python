file = "./data/fox.txt"

with open (file, "r", encoding="utf_8") as fileObj :
    while True :
        text = fileObj.read(10)
        if text :
            print(text)
        else :
            break;