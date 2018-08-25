from goods_property import Goods
from goods_property2 import Goods2

shoes = Goods("dream", 10000)
print(shoes.name)
shoes.name = "Dream8"
print(shoes.name)
print(shoes.price)

print("-" * 10)

shoes = Goods2("dream", 10000)
print(shoes.name)
shoes.name = "Dream8"
print(shoes.name)
print(shoes.price)