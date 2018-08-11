def calc(size = "M", num = 6) :
    unit_price = {"S": 150, "M":150, "L":180}
    price = unit_price[size] * num
    return (size, num, price)

a = calc()
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

a = calc("L")
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

local_num = 10
a = calc(num = local_num)
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")