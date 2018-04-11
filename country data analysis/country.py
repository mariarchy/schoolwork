# A class that tracks the population, area, continent, and population density of a country
class Country :
    ## constructs the area, continent, population density, area, and population density
    # @param name is the name of the country
    # @param population is the population of the country
    # @param continent is the continent of the country
    #
    def __init__(self, name, population, area, continent) :
        self._name = name
        self._population = int(population)
        self._area = float(area)
        self._continent = continent
        self._unformattedPopulationDensity = self._population/self._area
        # sets the population density to 2 decimal places
        self._populationDensity = "%.2f" % self._unformattedPopulationDensity
        # this is repetitive and may be issue because it produces string

    ## gets the name of the country
    # @return the name of the country
    def getName(self) :
        return self._name

    ## gets the population of the country
    # @return the population of the country
    def getPopulation(self):
        return self._population

    #@ gets the area of the country
    # @return the area of the country
    def getArea(self):
        return self._area

    ## gets the continent of the country
    # @return the continent of the country
    def getContinent(self):
        return self._continent

    ## sets the new/updated population of the country
    # @param newPopulation the new population of the country
    #
    def setPopulation(self, newPopulation):
        self._population = int(newPopulation)

    ## sets the new/updated area of the country
    # @param newArea the new area of the country
    #
    def setArea(self, newArea):
        self._area = int(newArea)

    ## sets the new/updated continent of the country
    # @param newContinent the new continent of the country
    #
    def setContinent(self, newContinent):
        self._continent = newContinent

    ## gets the population density of the country
    # @return the population density of the country
    def getPopDensity(self):
        return self._populationDensity

    ## prints/represents the data as strings
    # @return the formatted string representation of the country data
    def __repr__(self):
        return self._name + " (pop: " + str(self._population) + ", size: " + str(self._area) + ")" " in " + self._continent


