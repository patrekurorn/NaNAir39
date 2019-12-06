

class Employee:

    def __init__(self, ssn, name, position, rank, licence, address, mobile, landlineNr, email):
        self.my_list = []
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

    """ SSN """
    def get_ssn(self):
        return self.ssn

    def set_ssn(self, ssn):
        self.ssn = ssn

    """ Name """
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    """ Role """
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    """ Rank """
    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    """ Licence """
    def get_licence(self):
        return self.licence

    def set_licence(self, licence):
        self.licence = licence

    """ Address """
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    """ Postion """
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    """ Landline Nr """
    def get_landlineNr(self):
        return self.landlinenr

    def set_landlineNr(self, landlineNr):
        self.landlinenr = landlineNr

    """ Email """
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    """ Mobile """
    def get_mobile(self):
        return self.mobile

    def set_mobile(self, mobile):
        self.mobile = mobile
        
    
