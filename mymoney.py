import exchange
import importlib
# モジュールリロード
importlib.reload(exchange)

yen = 25000
rate = 114.22
charge = 1.0
dollar = exchange.yen2dollar(yen = yen, rate = rate, charge=charge)
print(f"{dollar :,.2f}ドル")