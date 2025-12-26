class Sonchi:
    def __init__(self, son):
        self.son = son

    def ikki_barobar(self):
        return self.son * 2

    def yarmi(self):
        return self.son / 2

    def teskari(self):
        return -self.son


a = Sonchi(10)

print(a.ikki_barobar())  
print(a.yarmi())      
print(a.teskari())   
