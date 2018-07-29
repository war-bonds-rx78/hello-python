from random import randint

# コメント追加
def dice() :
    num = randint(1, 6)
    return num

for i in range(5) : 
    result = dice()
    print(result)