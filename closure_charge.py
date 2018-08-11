# クロージャーの定義
def charge (price) :
    def calc(num) :
        return price * num
    return calc

# クロージャー（関数オブジェクト）を2種類作る
chid = charge(400)
adult = charge(10000)
# 料金
price1 = chid(3)
price2 = adult(2)
print(price1)
print(price2)