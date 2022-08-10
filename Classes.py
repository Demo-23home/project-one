#python Classes
class Emp:
    def __init__(self,name,age,department,is_manager):
        self.name=name
        self.age=age
        self.department=department
        self.is_manager=is_manager
#emp1=Emp("ziad",19,"SWE",True)
#print(emp1.name)

class Doctor:
    def studied_years(self):
        print("i have studied 7 years ")
    def works_here(self):
        print("i work at the hospital")
    def paid_by_who(slef):
        print("i get paid by the government")

class Fam_doc(Doctor):
    def what_specilization(self):
        print("i work with families")
    def paid_by_who(slef):
        print("i get paid by the people")
