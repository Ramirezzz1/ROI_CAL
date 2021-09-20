class ROI:
    def __init__(self):
        self.roi = {}
        self.income = {}
        self.expense = {}
        self.cashflow = {}
        self.cashoncash = {}
        
    def display(self):
        print(f'Here is your ROI {self.roi}')
        
    def additem (self, newinput):
        self.income.append(newinput)
        self.expense.append(newinput)
    
class NewBuyer:
    def __init__(self,income):
        self.income = income
        
    def income_cal(self):
        while True:
            ans = input (f' Please enter your income (Rental/Other/None)')
            while ans not in {'Rental', 'Other'}:
                ans = input(f'Please enter a form of income')
            if ans == 'Rental':
                rent = input( " Please enter your rental income")
                self.income.additem(rent)
            if ans == 'Other':
                other = input ("Please enter all other income")
                self.income.additem(other)
            if ans == 'None':
                print (f'Here is your total income {self.income}')
                break
    def expense_cal(self):
        while True:
            response = input(f'Please enter your expenses (TAX/Insurance/Utilites/Mortage/Property Management/Other)')
            while response not in {'TAX,Insurance,Utilites,Mortage,Other','None'}:
                response = input(f' Please enter an expense')
            if response == "TAX":
                tax = input(f'Please enter your Property taxes')
                self.expense.additem(tax)
            if response == "Insurance":
                insurance = input(f'Please enter your Insurance expense')
                self.expense.additem(insurance)
            if response == "Utilites":
                utilites = input(f'Please enter your total utility expense')
                self.expense.additem(utilites)
            if response == "Mortage":
                mortage == input(f'Please enter your Mortage')
                self.expense.additem(mortage)
            if response == "Other":
                other = input(f'Please enter any other expenses')
                self.expense.additem(other)
            if response == 'None':
                print(f'Here is your toatl expenses {self.expense}')
   
    def totalcashflow(self):
        cashflow = ({self.income} - {self.expense})
        self.cashflow = cashflow
        print(f"Your Cash Flow for this property is {self.cashflow}")
        
    def cashoncash(self):
        while True:
            cal = input(f"Please enter your (Down Payment/Closing Cost/Rehab budget/ Misc)")
            self.cashoncash.append(cal)
            

            #still need to incorporate math functions
            #to sum up values in dictionaries 