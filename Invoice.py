class Invoice:
    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items["qnt"] = qnt
        self.items["unit_price"] = price
        self.items["discount"] = discount
        return self.items

    def totalImpurePrice(self, products):
        totalImpurePrice = 0
        for k, v in products.items():
            totalImpurePrice += float(v["unit_price"]) * int(v["qnt"])
        totalImpurePrice = round(totalImpurePrice, 2)
        return totalImpurePrice

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += float(v["unit_price"]) * int(v["qnt"]) * float(v["discount"]) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            user_input = input(input_value)
            if user_input in ['y', 'Y', 'n', 'N']:
                return user_input
            print("y or n! try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! try again.")
                continue
            else:
                return userInput
