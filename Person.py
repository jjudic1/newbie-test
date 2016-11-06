class Person:

    def __init__(self, name, address, telephone, email, apikey, location):
        self.name = name

        self.address = address
        self.telephone = telephone
        self.email = email
        self.apikey = apikey
        self.location = location

    def location(self):
        return self.location

    def address(self):
        return self.address

    def apikey(self):
        return self.apikey

    def email(self):
        return self.email

    def telephone(self):
        return self.telephone

    def name(self):
        return self.name
