class Employee:

    def __init__(self, id, ssn, name, position, rank, licence, address, mobile, landlineNr, email):
        self.my_list = []
        self.id = id
        self.ssn = ssn
        self.name = name
        self.position = position
        self.rank = rank
        self.licence = licence
        self.address = address
        self.mobile = mobile
        self.landlinenr = landlineNr
        self.email = email


    def __str__(self):
        return ("{} {} {} {} {} {} {} {} {} {} ".format(self.id, self.name, self.ssn, self.address, self.landlinenr, self.mobile, self.email, self.position, self.rank, self.licence))

    """ ID """
    def get_id(self):
        return self.id
    def set_id(self):
        self.id = self
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

















