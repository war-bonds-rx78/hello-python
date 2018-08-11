def clac(num) :
    # 単価
    unit_price = 180
    if not num.isdigit() :
        return None
    price = int(num) * unit_price
    return price

while True :
    num = input("個数を入力して下さい。(qで終了)")
    if "q" == num :
        break
    elif  num == "" :
        continue
    
    result = clac(num)

    if result is None :
        print("数字ではない")
    else :
        print(result)