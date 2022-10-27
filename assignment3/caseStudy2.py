from pandas import *

class Bank:
    path = "C:/Users/naman/Desktop/Edureka Python/assignment3/bank-data.csv"
    df = read_csv(path)
    jobs = []
    def printFileData(self):
        print(self.df.to_string())
        
    def createUniqueSetOfProfessions(self):
        
        self.jobs = self.df['job'].to_list()
        print(set(self.jobs))
        
    def checkAvailabilityOfProfession(self,profession):
        print(profession in self.jobs)
        
    def eligibilityOfClient(self,minAge,profession,marital):
        data = DataFrame(self.df,columns=["age","job","marital","y"])        
        for ind in data.index:
            if data['age'][ind] > minAge and data['job'][ind] == profession and data['marital'][ind] == marital: 
                print(data['age'][ind]," - ", data['job'][ind]," - ", data['marital'][ind])
        
if __name__ == "__main__":
    
    obj = Bank()
    
    # 1
    # obj.printFileData()
    
    # 2

    obj.createUniqueSetOfProfessions()    
    
    # 3
    professions = input("Enter the job to be checked: ")
    obj.checkAvailabilityOfProfession(professions)
    
    # 4
    obj.eligibilityOfClient(20, "student", "single")
    
    
    
    
    
    
    

    