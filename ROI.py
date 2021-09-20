class Income:
    def __init__(self, rent, other):
        self.rent = rent 
        self.other = other
    
    def total_income(self):#add method
        final_income = self.rent + self.other
        return final_income

    def expenses(self):#add method
        return #expense = self.expense + self.other1

    def cashflow(self):#subtract
        cash_flow = final_income - final_expense
        return cash_flow

    def ROI(self):
        pass

# test = Income(2000,100)
# testrun= test.total_income()
# print(testrun)