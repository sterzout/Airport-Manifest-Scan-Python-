class Airport():
# Class airport is created
    def __init__(self, code, city, country):
# making the constructor
        self._code = code
        self._city = city
        self._country = country
# initialize variables
    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"
# this returns airport objects

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country
# creates methods for Airport Class
