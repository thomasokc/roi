class Roi:

    
    #How much the tenant pays
    def payment(self):
        self.pay = {}
        self.keys = []

        while True:
            key = input("""\nEnter one thing your tenant will pay for.
             Examples: Rent, laundry, storage, etc.
             Type 'Done' when finished. """)
            if key.lower() == 'done':
                break
            else:
                self.keys.append(key)

        for k in self.keys:
            v = input(f"\nHow much will your tenant pay for {k}? ")
            self.pay[k] = int(v)

        self.total_pay = sum(self.pay.values())

    # How much the owner pays
    def expenses(self):
        self.expense = {}
        self.keys = []

        while True:
            key = input("""\nEnter what you need to save/pay each month.
             Examples: Tax, insurance, repairs, mortgage etc.
             Type 'Done' when finished. """)

            if key.lower() == 'done':
                break
            else:
                self.keys.append(key)

        for k in self.keys:
            v = input(f"\nHow much will you put into {k}? ")
            self.expense[k] = int(v)

        self.total_exp = sum(self.expense.values())


    def cash(self):
        self.payment()
        self.expenses()
        payed = self.total_pay
        exp = self.total_exp

        down_pay = int(input("\nHow much was your down payment? "))
        closing = int(input("\nHow much did it cost to close? (Payments for appraisal, attourney, documents, etc) "))
        rehab = int(input("\nHow much did you spend to renovate the property? "))
        
        total = down_pay + closing + rehab

        cash_roi = total / (12 * (payed - exp))

        return f"\nYour cash on cash return on investment(ROI) is {round(cash_roi, 2)}%"

test = Roi()
go = test.cash()
print(go)
    