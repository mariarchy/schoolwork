# imports the country class over
from country import Country

## Uses 2 files to build data structures holding information about countries and continents
class CountryCatalogue:
    ## Contructs the data structures cDictionary and countryCat
    # @param continentFile the file containing the names of countries and continents
    # @param countryFile the file containing the country information
    def __init__(self, continentFile, countryFile):
        continentFile = checkFileName(continentFile)        # checks if the input file name contains ".txt" in it
        countryFile = checkFileName(countryFile)
        continentData = open(continentFile, "r")
        self._cDictionary = {}
        for line in continentData :
            line = line.rstrip()
            # So that the code doesn't process headers
            if line != "Country,Continent" :
                listOfCountryData = line.split(",")
                # Makes characters lowercase so there isn't a discrepancy between the case sensitivity in cDictionary and countryCat
                country = listOfCountryData[0].lower()
                self._continent = listOfCountryData[1].lower()
                self._cDictionary[country] = self._continent

        countryData = open(countryFile, "r")
        self._countryCat = {}
        for line in countryData :
            line = line.rstrip()                        # strips "\n"
            if line != "Country|Population|Area" :      # Avoids storing headings of the code
                listOfInfo = line.split("|")
                # so there isn't a discrepancy between the case sensitivity in cDictionary and countryCat
                self._countryName = listOfInfo[0].lower()
                # removes the "," and formats numbers into an integer or float
                self._population = formatNumbers(listOfInfo[1], "int")
                self._area = formatNumbers(listOfInfo[2], "float")
                # makes sure the country read for countryCat is also in cDictionary
                if self._countryName in self._cDictionary :
                    # so that we may match each key with the countryCat's keys
                    self._formattedCountryName = formatString(self._countryName)
                    # creates the country object then makes the country the key and the country object the value in the dictionary
                    self._countryCat[self._countryName] = Country(self._formattedCountryName, self._population, self._area, formatString(self._cDictionary[self._countryName]))

        countryData.close()
        continentData.close()

    ## Looks up a country name in the data structure
    # @param countryName the name of the country the user would like to look up
    # returns the country name, and if the country inputted doesn't exist, returns "None"
    def findCountry(self, countryName) :
        # makes all the characters lowercase to match the case sensitivity of the country names in the dictionary countryCat
        countryName = countryName.lower()
        return self._countryCat.get(countryName, None)

    ## Sets the population of a country to a new one
    # @param countryName the country the user would like to update the population of
    # @param newPop the new population the user would like to input
    # returns True if the input country exists and False if it does not
    def setPopulationOfCountry(self, countryName, newPop):
        countryName = countryName.lower()
        if countryName in self._countryCat :
            self._countryCat[countryName].setPopulation(newPop)
            return True
        else :
            return False

    ## Sets the area of a country to a new one
    # @param countryName the country the user would like to update the population of
    # @param newArea the new area the user would like to input
    # returns True if the input country exists and False if it does not
    def setAreaOfCountry(self, countryName, newArea):
        countryName = countryName.lower()
        if countryName in self._countryCat :
            self._countryCat[countryName].setArea(newArea)
            return True
        else :
            return False

    ## Adds a country to the data structures cDictionary and countryCat
    # @param countryName the name of the new country
    # @param population the population of the new country
    # @param area the area of the new country
    # @continent the continent of the new country
    # returns True if the new country doesn't exist in the data structure and False if it already does
    def addCountry(self, countryName, population, area, continent):
        countryName = countryName.lower()           # Keeps consistent case sensitivity
        if countryName in self._countryCat :
            return False                            # returns False since the country already exists
        else :
            self._countryCat[countryName] = Country(formatString(countryName), population, area, formatString(continent))   # creates new country object
            self._cDictionary[countryName] = continent      # adds new country to cDictionary
            return True

    ## Deletes a country from the data structures cDictionary and countryCat
    # @param countryName the country the user would like to remove
    #
    def deleteCountry(self, countryName):
        countryName = countryName.lower()           # consistent case sensitivity
        if countryName in self._countryCat :
            self._countryCat.pop(countryName)       # if the input country exists in the list, this removes it from cDictionary and countryCat
            self._cDictionary.pop(countryName)

    ## displays the whole catalogue using the default string representation for Country objects
    #
    def printCountryCatalogue(self):
        for key in self._countryCat :
            print(str(self._countryCat[key]))           # prints all the string representations of each country object

    ## Gets the list of countries on a specific continent
    # @param continent the continent the user would like to find the countries of
    # returns a list containing the objects of the countries within the specified continent, and an empty list if the input country doesn't exist
    def getCountriesByContinent(self, continent):
        continent = continent.lower()
        listOfCountries = []
        for key in self._countryCat :
            if self._cDictionary[key] == continent :
                listOfCountries.append(self._countryCat[key])
        return listOfCountries

    ## Sorts data(numbers) in descending order
    # @param unsortedList a list containing elements that are lists, with the first element as the country name and the second element as the data that needs to be sorted
    # returns a list of tuples, with the country name and the data, in sorted order
    def sortData(self, unsortedList):
        i = 0
        largest = -1
        sortedList = []
        listOfTuples = []

        while i < len(unsortedList) :
            if unsortedList[i][1] > largest :
                sortedList.insert(0, unsortedList[i])       # inserts the largest value and its indicator (country name) to the first position
                largest = unsortedList[i][1]                # updates the largest value
            elif len(sortedList) == 1 :                     # appends the item to the second position if there is only 1 other element in the list
                sortedList.append(unsortedList[i])
            elif len(sortedList) >= 2:                      # appends the element in its proper order if it isn't the largest in the list
                for j in range(1, len(sortedList)) :
                    if unsortedList[i][1] > sortedList[j][1] :      # while looping through each element, if the value is larger, it gets inserted in that position
                        sortedList.insert(j, unsortedList[i])
                        # breaks so that the loop stops and there's no repeats when the loop reaches the end
                        break
                    elif j == len(sortedList) - 1 :
                        sortedList.append(unsortedList[i])          # if it loops through the entire list and isn't greater than any element, it gets appended to the end
            i = i + 1
        # creates a tuple of the country name and its data
        for list in sortedList :
            name = self._countryCat[list[0]].getName()
            data = list[1]
            tupleOfData = (name, data)
            listOfTuples.append(tupleOfData)

        return listOfTuples

    ## Gets countries and the populations in the input continent
    # @param continent the continent the user would like to know the countries and populations of, default is ""
    # returns a list of tuples with the country name and population (if continent = "" it returns every country and its population) in descending order
    def getCountriesByPopulation(self, continent = ""):
        continent = continent.lower()
        listOfData = []

        for key in self._countryCat :
            # if the continent name is the default, this adds all the countries and their populations
            if continent == "" :
                listOfData.append([key, self._countryCat[key].getPopulation()])

            # if the continent inputted is an existing continent
            elif self._cDictionary[key] == continent :
                listOfData.append([key, self._countryCat[key].getPopulation()])
                # if the population of the country is greater than the populations currently in the list
        tuples = self.sortData(listOfData)
        return tuples

    ## Gets countries and the populations in the input continent
    # @param continent the continent the user would like to know the countries and populations of, default is ""
    # returns a list of tuples with the country name and population (if continent = "" it returns every country and its population) in descending order
    def getCountriesByArea(self, continent = ""):
        continent = continent.lower()
        listOfInfo = []
        for key in self._countryCat :
            if continent == "" :                                            # if the continent name is the default, this adds all the countries and their areas
                listOfInfo.append([key, self._countryCat[key].getArea()])
            elif self._cDictionary[key] == continent :                      # if the continent inputted is an existing continent,
                listOfInfo.append([key, self._countryCat[key].getArea()])   # it appends all the areas from countries in that continent to a list
        tupleData = self.sortData(listOfInfo)           # sorts the data (the areas) from greatest to least and returns as a list of tuples
        return tupleData

    ## Gets the continent with the highest population
    # returns a tuples with the continent name and population
    #
    def findMostPopulousContinent(self) :
        listOfContinents = []
        for key in self._cDictionary :
            if self._cDictionary[key] not in listOfContinents :
                listOfContinents.append((self._cDictionary[key]))       # creates a list of unique continents in the dictionary cDictionary
        populationList = []
        for el in listOfContinents :
            listOfCountries = self.getCountriesByContinent(el)          # gets the countries from each continent and calculates the total population
            continentPopulation = 0
            for country in listOfCountries :
                population = country.getPopulation()
                continentPopulation = continentPopulation + population
            populationList.append([formatString(el), continentPopulation])  # appends the total population of each continent to a list
        i = 0
        largest = -1
        # find the maximum population
        while i < len(populationList) :
            if populationList[i][1] > largest :
                largest = populationList[i][1]                  # updates the largest population value
                largestContinent = populationList[i][0]         # updates the continent with the largest population
            i = i + 1
        return largestContinent, largest

    ## Gets countries with population densities in between the lower and upper bound
    # @param lowerBound the lower bound of the accepted population density range
    # @param upperBound the upper bound of the accepted population density range
    # returns a list of tuples with the country name and the population density that are within the accepted range
    def filterCountriesByPopDensity(self, lowerBound, upperBound):
        listOfPopDen = []
        for key in self._countryCat :
            popDensity = float(self._countryCat[key].getPopDensity())
            if popDensity >= lowerBound and popDensity <= upperBound :
                listOfPopDen.append([key, popDensity])                  # appends to a list of population densities if the population density is in the given range
        finalListOfPopDen = self.sortData(listOfPopDen)
        return finalListOfPopDen

    ## writes all the country data to a new file
    # @param fileName the file the user wants to write the country data to
    # returns the count of the number of items written and returns -1 if there is an error in the writing process
    def saveCountryCatalogue(self, fileName):
        countryString = ""
        stringList = []
        count = 0
        for key in self._countryCat :
            # creates the string of each country's data to be added
            newPortion = self._countryCat[key].getName() + "|" + self._countryCat[key].getContinent() + "|" + str(self._countryCat[key].getPopulation()) + "|" + str(self._countryCat[key].getArea()) + "|" + self._countryCat[key].getPopDensity() + "\n"
            # creates a list of country names and their respective string
            stringList.append([key, newPortion])
            count = count + 1                       # keeps a count of how many items are to be written to the input file
        stringList = sorted(stringList)             # sorts the strings in alphabetical order
        for country in stringList :
            countryString = countryString + country[1]  # creates a master string of all the individual country strings
        try :
            fileName = checkFileName(fileName)
            newFile = open(fileName, "w")
            newFile.write(countryString)            # writes the string to the specified file
            newFile.close()
            if count > 1 or count == 0:             # if count is greater than one or equal to 0
                return "There were " + str(count) + " items written."
            else :                                  # if count is equal to 1
                return "There was " + str(count) + " item written."

        except :
            return -1           # returns -1 if there is an error

## checks if the inputted file name has ".txt" in it
# @param fileName the name of the file to be checked
# returns the revised file name
def checkFileName(fileName) :
    if ".txt" not in fileName :
        return fileName + ".txt"
    else :
        return fileName

## formats strings with digits as integers or floats
# @param unformattedNumber the string that is to be formatted into an integer or float
# @param type accepts "int" (integer) or "float" (float)
# returns the formatted number as an integer or float
def formatNumbers(unformattedNumber, type) :
    formattedNumber = ""
    unformattedNumber = unformattedNumber.split(",")            # removes the ","
    for number in unformattedNumber :
        formattedNumber = formattedNumber + number
    # returns the string as an integer or float
    if type == "int" :
        return int(formattedNumber)
    elif type == "float" :
        return float(formattedNumber)

## formats strings with the proper case sensitivity (uppercase)
# @param string the string that is to be reformatted
# returns the formatted string with the proper case sensitivity
def formatString(string) :
    newString = ""
    for i in range(len(string)) :
        if i == 0 :
            newString = newString + string[i].upper()           # capitalizes the first character
        elif string[i-1] == " " :
            newString = newString + string[i].upper()           # capitalizes any characters that proceed a " "
        else :
            newString = newString + string[i].lower()           # appends any other letters as lowercase letters
    return newString

