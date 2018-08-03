input_data = int(input("入力："))

if input_data % 4 == 0 :
    if input_data % 100 == 0:
        if input_data % 400 == 0:
            print("閏年")
        else :
            print("失敗")
    else :
        print("閏年")
else :
    print("失敗")