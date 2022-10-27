class Bank():
    defaultPassword = "12345678"
    def __init__(self,bankBalance):
        self.bankBalance = bankBalance
        
    def withdrawl(self, amountWithdrawal):
        if amountWithdrawal < self.bankBalance:
            self.bankBalance-=amountWithdrawal
            print(f"Your current balance is {self.bankBalance}")
        else:
            print("Insufficient bank balance")
            
    def creditBalance(self, amountCredit):
        self.bankBalance+=amountCredit
        print(f"Your current balance is {self.bankBalance}")

    def changePassword(self,newPassword):
        self.defaultPassword = newPassword
        print("Your password has been changed")
    
    def getNewPassword(self):
        return self.defaultPassword;


if __name__=="__main__":
    bank = Bank(1000)
    enterPassword = input("Enter your password: ")
    
    flag = True
    print(bank.defaultPassword)
    print(enterPassword)
    print(enterPassword == bank.defaultPassword)
    if(enterPassword == bank.defaultPassword):
        while(flag):     
        
            print("========Welcome to mini bank========")
            print("Please enter your choice")
            print("1: for withdrawal")
            print("2: for credit amount")
            print("3: for change password")
            print("4: for exit\n")

            noCh = int(input())
            
            match noCh:
                case 1:
                    withdrawalAmount = int(input("Enter the ampunt to be withdrawan: "))
                    bank.withdrawl(withdrawalAmount)
                    # break
                case 2:
                    creditAmount = int(input("Enter the amount to be credited: "))
                    bank.creditBalance(creditAmount)   
                case 3:
                    newPassword = input("Please enter new password: ")
                    bank.changePassword(newPassword)
                    print("Do you wish to see your changed password enter 1 for yes and 0 for no: ")
                    choice = int(input())
                    if choice == 1:
                        print(bank.getNewPassword())
                    else:
                        pass

                case 4:
                    print("========Thanks for visiting Mini bank========")
                    flag = False
                case _:
                    print("Please enter no between 1-4")
    else:
        print("Incorrect Password!")
            