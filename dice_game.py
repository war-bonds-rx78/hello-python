from random import randint

# コメント追加
def dice() :
    num = randint(1, 6)
    return num

for i in range(5) : 
    dice1 = dice()
    dice2 = dice()

    sum = dice1 + dice2
    print(f"{dice1}と{dice2}の合計は{sum}")