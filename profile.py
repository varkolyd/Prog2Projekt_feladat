class EmailAddressFormatException(Exception):
    pass

class MissingDataException(Exception):

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value + " is missing!"

class Profile:

    def __init__(self, name, email, egyenleg, id):
        self.name = name
        self.email = email
        self.egyenleg = egyenleg
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_egyenleg(self, egyenleg):
        self.egyenleg = egyenleg

    def set_id(self, id):
        self.id = id


    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_egyenleg(self):
        return self.egyenleg

    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.get_name()},{self.get_email()},{self.get_egyenleg()},{self.get_id()}"

    def __lt__(self, other):
        return self.get_id() < other.get_id()

    def __le__(self, other):
        return self.get_id() <= other.get_id()

    def __ge__(self, other):
        return self.get_id() >= other.get_id()

    def __gt__(self, other):
        return self.get_id() > other.get_id()

    def __eq__(self, other):
        return self.get_id() == other.get_id()

