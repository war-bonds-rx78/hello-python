# Class
class Car :
    # クラス変数
    maker = "PEAGE"
    count = 0

    # クラスメソッド
    @classmethod
    def countup(cls) :
        cls.count += 1
        print(f"出荷台数：{cls.count}")
    
    def __init__ (self, color = "white") :
        self.color = color
        self.mileage = 0

    def drive(self, km) :
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです"
        print(msg)