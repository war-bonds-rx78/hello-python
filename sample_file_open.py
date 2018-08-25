file = "./data/fox.txt"
fileObj = open(file)
text = fileObj.read()
fileObj.close()
print(text)