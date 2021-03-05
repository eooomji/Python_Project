class Seller:

    def __init__(self, price, numOfMasks, myMoney):
        self.price = price
        self.numOfMasks = numOfMasks
        self.myMoney = myMoney

    def sellMask(self, money):
        number = money//(self.price)
        self.numOfMasks -= number
        self.myMoney += money
        return number

    def showSellResult(self):
        print("남은 마스크: %d" % (self.numOfMasks))
        print("판매 수익: %d" % (self.myMoney))

class Buyer:

    def __init__(self, myMoney):
        self.numOfMasks = 0
        self.myMoney = myMoney

    def buyMask(self, money):
        self.numOfMasks = Seller.sellMask(seller, money)
        self.myMoney -= money

    def showSellResult(self):
        print("마스크 개수: %d" % (self.numOfMasks))
        print("잔액: %d" % (self.myMoney))

seller = Seller(1000, 100, 0)
buyer = Buyer(40000)
buyer.buyMask(5000)

print("마스크 판매자")
seller.showSellResult()
print()
print("마스크 구매자")
buyer.showSellResult()
