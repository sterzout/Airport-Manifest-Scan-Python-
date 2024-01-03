from Airport import *
# Import Aiport Class


class Flight:
# Create Flight Class
    def __init__(self, flightNo, origin, destination):
# making the flight constructor
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
# for airport objects
        else:
            raise TypeError("The origin and destination must be Airport objects")
# when they are not airport objects
    def __repr__(self):
        if self.isDomesticFlight():
            flightType = "domestic"
# if the flight type is domestic it takes this type
        else:
            flightType = "international"
# if the flight type is international it takes this type

        return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + \
               self._destination.getCity() + " {" + flightType + "} "
# statement returning either domestic or international
    def __eq__(self, other):
        if type(other) == Flight:
            return self._origin == other.getOrigin() and self._destination == other.getDestination()
        else:
            return False
# returns true or false based on if the flights are the same and false if not flight object and different
    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination
# all these are the methods for Flight Class
