
class Employee:

        def __init__(self, ssn, name, position, rank, licence, address, mobile, landlineNr, email):
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
            return ("SSN: {}\nName: {}\nPosition: {}\nRank: {}\nLicence: {}\nAddress: {}\nMobile: {}\nLandline number: {}\nEmail: {}".format(self.ssn,self.name,
                                                                                                                                             self.position,self.rank,
                                                                                                                                             self.licence,self.address,
                                                                                                                                             self.mobile,self.landlineNr,
                                                                                                                                             self.email))

        """ SSN """
        def get_ssn(self):
            return self.ssn
        def set_ssn(self, other):
            self.ssn = other

        """ Name """
        def get_name(self):
            return self.name
        def set_name(self, other):
            self.name = other

        """ Position """
        def get_position(self):
            return self.position
        def set_position(self, other):
            self.position = other

        """ Rank """
        def get_rank(self):
            return self.rank
        def set_rank(self, other):
            self.rank = other

        """ Licence """
        def get_licence(self):
            return self.licence
        def set_licence(self, other):
            self.licence = other

        """ Address """
        def get_address(self):
            return self.address
        def set_address(self, other):
            self.address = other


        """ Landline Nr """
        def get_landlineNr(self):
            return self.landlineNr
        def set_landlineNr(self, other):
            self.landlineNr = other

        """ Email """
        def get_email(self):
            return self.email
        def set_email(self, other):
            self.email = other

        """ Mobile """
        def get_mobile(self):
            return self.mobile
        def set_mobile(self, other):
            self.mobile = other
