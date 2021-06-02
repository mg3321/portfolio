##This program simulates a class based prinitng account system

class PrinterAccount:
    def __init__(self, name, student_ID, balance, pages_printed=0):
        self.name = name
        self.student_ID = student_ID
        self.balance = balance
        self.pages_printed = pages_printed

    def printAccount(self): #Prints details of account
        print('Name:', self.name, '\n',
              'Student ID:', self.student_ID, '\n',
              'Account Balance: £' + str(round(self.balance, 2)), '\n',
              'Total Pages Printed:', self.pages_printed)

    def printBalance(self): #Prints remaining balance of account
        print('Account balance for', self.name,
              'is £' + str(round(self.balance, 2)))

    def topUp(self, amount): #Tops up user's account balance
        amountInPounds = amount / 100
        print(self.name, 'topped up £' + str(amountInPounds) )
        self.balance += amountInPounds

    def cost(self, paperSize, colour): #Returns cost/page of requested job
        if colour:
            if paperSize == 'A4':
                charge = 0.1
            else:
                charge = 0.2
        else:
            charge = 0

        return charge

    def yesNo(self, prompt): #General function for yes/no questions
        while True:
            response = input(prompt)
            if response == 'y' or response == 'Y':
                return True
            elif response == 'n' or response == 'N':
                return False
            else:
                print('Sorry I did not understand, please try again.')
                continue

    def checkBalance(self, numPages, paperSize, colour): #Checks that the user has enough credit for requested job
        charge = self.cost(paperSize, colour)
        totalCost = charge * numPages
        if totalCost > self.balance:
            if self.yesNo('\nYour balance is not sufficient to print all pages.\n' +
                     'Would you like to continue anyway? Y/N'):
                return True
            else:
                print('Please top-up and try again')
                return False
        else:
            return True
            
        
    def printDocument(self, numPages, paperSize, colour):
        charge = self.cost(paperSize, colour)
        if self.checkBalance(numPages, paperSize, colour):
            for i in range(numPages):
                if self.balance >= 0.1:
                    self.balance -= charge
                    self.pages_printed += 1
                    print('Printing page', i + 1)      
                else:
                    print('Account balance too low to continue.\n',
                          'Please top-up, and try again.')
                    return False
        else:
            return False

       
bob = PrinterAccount('bob', 1527348363, 1, 0)
bob.printAccount()
bob.printBalance()
#bob requests a job which he cannot afford
bob.printDocument(12, 'A4', True)
bob.printAccount()

