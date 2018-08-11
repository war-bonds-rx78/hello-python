def clac(num) :
    # 単価
    unit_price = 180
    try :
        num = float(num)
        result = num * unit_price
    except :
        # 例外スロー
        result = None
    return result

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