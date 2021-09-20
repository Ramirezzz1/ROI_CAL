# class FourSquareMethod:
#     def __init__(self,income,expenses,cashflow,cashoncash ):
#         self.income = income
#         self.expenses = expenses
#         self.cashflow = cashflow
#         self.cashoncash = cashoncash



class FinalIncome:
    def __init__(self):
        self.digit = digit 
        self.total_income = []

    def add_income(self, dollars):
        while True:
            response = input(f"Please enter your soucres of income (RENTAL/MISC/OTHER) ")
            while response not in ["RENTAL", "MISC", "OTHER"]:
                response = input(f'Please enter valid respone (RENTAL/OTHER/NONE)')
            if response == "RENTAL":
                rent = input("Please enter your rental income")
                self.total_income.additem(rent)
            if response == "MISC":
                other = input("Please enter any other income, enter 0 if none")
                self.total_income.additem(other)
            if response == "NONE":
                print(f'Your total income from this property is {self.total_income}')
                break
    # def final_income(self):
    #     total= 0
    #     for income in self.total_income:
    #         value = rent + other
    #         self.total_income.additem(value)

FinalIncome()