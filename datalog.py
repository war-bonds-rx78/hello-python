from datetime import datetime

class Datalog :

    # コンテキスト
    def __init__ (self) :
        self.loglist = []
    
    # インスタンスメソッド
    def log(self, data) :
        now = datetime.now()
        item = (now, data)
        self.loglist.append(item)
