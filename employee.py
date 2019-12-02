import csv
class Employee:

    def __init__(self, ssn ,name ,role ,rank ,licence, id,address,landlineNr,mobile,email):
        self.__ssn = ssn
        self.__name = name
        self.__role = role
        self.__rank = rank
        self.__licence = licence

        self.__id = id
        self.__address = address
        self.__landlineNr = landlineNr
        self.__mobile = mobile
        self.__email = email

    def __str__(self):
        return " Ssn: {}\n Name: {}\n Role {}:\n Rank {}:\n Licence:{}".format(self.__ssn,self.__name,self.__role,self.__rank,self.__licence)
    def get_ssn(self):
        return self.__ssn
    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def get_rank(self):
        return self.__rank
    def get_licence(self):
        return self.__licence

    def get_id(self):
        return self.__id
    def get_address(self):
        return self.__address
    def get_landlineNr(self):
        return self.__landlineNr
    def get_mobile(self):
        return self.__mobile
    def get__email(self):
        return self.__email



    def set_ssn(self,value):
        self.__ssn = value
    def set_name(self,value):
        self.__name = value
    def set_role(self,value):
        self.__role = value
    def set_rank(self,value):
        self.__rank = value
    def set_licence(self,value):
        self.__licence = value

    def set_id(self,value):
        self.__id = value
    def set_address(self,value):
        self.__address = value
    def set_landlineNr(self,value):
        self.__landlineNr = value
    def set_mobile(self,value):
        self.__mobile = value
    def set__email(self,value):
        self.__email = value

a = Employee( "ssn" ,"bla","role" ,"rank" ,"licence", "id","address","landlineNr","mobile","email")
print(a)
print()

a.set_name("Agúrka")
print(a)








