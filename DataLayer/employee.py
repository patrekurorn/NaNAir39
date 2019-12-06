class Employee:

    def __init__(self, ssn, name, position, rank, licence, address, mobile, landlineNr, email):
        self.my_list = []
        #self.id = id
        self.ssn = ssn
        self.name = name
        self.position = position
        self.rank = rank
        self.licence = licence
        self.address = address
        self.mobile = mobile
        self.landlineNr = landlineNr
        self.email = email


    def __str__(self):
        return ("{} {} {} {} {} {} {} {} {}".format(self.ssn,self.name,self.position,self.rank,self.licence,self.address,self.mobile,self.landlineNr,self.email))

    """ ID """
   # def get_id(self):
   #     return self.id
   # def set_id(self):
   #     self.id = self
    """ SSN """
    def get_ssn(self):
        return self.ssn
    def set_ssn(self):
        self.ssn = self
    """ Name """
    def get_name(self):
        return self.name
    def set_name(self):
        self.name = self
    """ Role """
    def get_position(self):
        return self.position
    def set_position(self):
        self.position = self
    """ Rank """
    def get_rank(self):
        return self.rank
    def set_rank(self):
        self.rank = self
    """ Licence """
    def get_licence(self):
        return self.licence
    def set_licence(self):
        self.licence = self
    """ Address """
    def get_address(self):
        return self.address
    def set_address(self):
        self.address = self
    """ Postion """
    def get_position(self):
        return self.position
    def set_position(self):
        self.position = self
    """ Landline Nr """
    def get_landlineNr(self):
        return self.landlinenr
    def set_landlineNr(self):
        self.landlinenr = self
    """ Email """
    def get_email(self):
        return self.email
    def set_email(self):
        self.email = self
    """ Mobile """
    def get_mobile(self):
        return self.mobile
    def set_mobile(self):
        self.mobile = self

    #TODO þurfum að klára þessa klassa hér fyrir neðan 

    def list_all_employees(self):   # á eftir að setja í stafrósröð
        self.empl_dict = {}

        key = self.name
        value = (self.ssn,self.position,self.rank,self.licence,self.address,self.mobile,self.landlineNr,self.email)
        
        self.empl_dict[key] = value
        print(self.empl_dict)
        
    def list_all_pilots(self):
        self.pilot_dict = {}
        key = self.name
        value = (self.ssn,self.position,self.rank,self.licence,self.address,self.mobile,self.landlineNr,self.email)
        
        if self.position == "Pilot":
            self.pilot_dict[key] = value
        print(self.pilot_dict)

    def list_all_flight_attendants(self):
        pass

    def find_employee(self):
        pass

    def edit_employee(self):
        pass

    def new_pilot(self):
        pass
    def new_flight_attendant(self):
        pass
    def list_all_available(self):
        pass
    def list_all_bust(self):
        pass
    def print_week_of_employees(self):
        pass

        
    
