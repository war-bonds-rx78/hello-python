file = "./data/fox.txt"

with open(file) as fileobj:
    text = fileobj.read()
    nexttext = text.rstrip(".")
    worldlist = nexttext.split(" ")
    print(worldlist)