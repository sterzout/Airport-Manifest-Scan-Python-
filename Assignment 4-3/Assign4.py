from Flight import*
from Airport import*
# Import both Flight and Aiport into the file as Classes

allFlights = {}
allAirports = {}
flightList = []
Flist = []
# initializing empty lists before the functions for use later in the code.
def loadData(airportFile, flightFile):
    try:
        fileAirports = open(airportFile, "r")
        fileFlights = open(flightFile, "r")
    except IOError:
        return False
# try and except, if try succeeds it goes and opens then reads each file, if fails it presents false for the IOError.

    airportList1 = []

    for lineA in fileAirports:
        lineA = lineA.strip().strip("\n").strip("\t")
        lineA = lineA.split(",")
        airportList1.append(lineA)
# cleans up fileAirports into List1 and strips unnecessary texts and spaces
    for lineA2 in airportList1:
        airportParts = []
# list to store parts of the airport list
        for lineinlineA in lineA2:
            lineinlineA=lineinlineA.strip("\t").strip(" ")
            airportParts.append(lineinlineA)
# cleans the List1 and strips unnecessary text and spaces, appends the seperated values into aiportParts list
        allAirports[airportParts[0]] = Airport(airportParts[0], airportParts[2], airportParts[1])
# creating a dictionary using the airport Code as the key
    for line in fileFlights:
        wordList = []
        line = line.split(',')
        for word in line:
            word = word.strip().strip('\n').strip('\t')
            wordList.append(word)
        flightList.append(Flight(wordList[0], allAirports[wordList[1]], allAirports[wordList[2]]))
# similar process but instead for the flight file then we create a flight object using the airport object parts.

    for key in allAirports:
        allFlights[key] = []
        for flight in flightList:
            if flight.getOrigin().getCode() == key:
                allFlights[key].append(flight)
    return True
# Returns true at the end of the function

def getAirportByCode(code):

    airports1 = allAirports[code]
    if airports1 == "None":
        return -1

    else:
        return airports1
# if none return value "-1" else we return the same airports1 value




def findAllCityFlights(city):

    cityFList = []
    for f in flightList:
        if f.getDestination().getCity() == city or f.getOrigin().getCity() == city:
            cityFList.append(f)
    return cityFList
# if the f destination and origin are the same we append this city

def findAllCountryFlights(country):

    countryFList = []
    for f in flightList:
        if f.getDestination().getCountry() == country or f.getOrigin().getCountry() == country:
            countryFList.append(f)
    return countryFList
# if the destination and origin country are the same we append this to a list

def findFlightBetween(origAirport, destAirport):
    for f1 in allFlights[origAirport.getCode()]:
        if f1.getDestination() == destAirport:
            return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
# return statement for flights directly from origAirport to destAirport
    cFlightsSet=set()
    for f in allFlights[origAirport.getCode()]:
        for cFlight in allFlights[f.getDestination().getCode()]:
            if cFlight.getDestination() == destAirport:
                cFlight1 = cFlight.getOrigin().getCode()
                cFlightsSet.add(cFlight1)
# if not a direct flight we add it as a connect flight to the cFlightsSet
    if len(cFlightsSet) > 0:
        return cFlightsSet
    else:
        return -1
# if length of the set is greater than 0 we return it meaning it is not empty otherwise we return "-1"
def findReturnFlight(firstFlight):
    for f in allFlights[firstFlight.getDestination().getCode()]:
        for rFlight in allFlights[f.getOrigin().getCode()]:
            if rFlight.getDestination().getCode() == firstFlight.getOrigin().getCode() and rFlight.getOrigin().getCode() == firstFlight.getDestination().getCode():
                return rFlight
    return -1
# finally when going through the for loop we use the return flight destination getcode, origin getcode and return
# flight origin getcode and first flight destination getcode to see if they go in opposite directions. If
# this is the case we give back the return "-1", otherwise we return the return flight.
