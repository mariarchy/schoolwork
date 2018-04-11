def main() :
    try:
        # prompts user for name of the file with the keywords
        nameOfKeyFile = input("Please enter the name of the file containing the keywords: ")
        # prompts user for name of file with the tweets
        nameOfTweetFile = input("Please enter the name of the file with tweets: ")
    # if the file the user inputs does not exist, the program raises an exception
    except IOError :
        print("Error: file not found")

    # keywords holds the entire text file
    keywords = checkFile(nameOfKeyFile)
    # dictionaryOfKeywords holds the data processed from the text file by formatting the data into a dictionary
    dictionaryOfKeywords = readKeywords(keywords)

    tweets = checkFile(nameOfTweetFile)       # adds ".txt" if the user entered a file without the ".txt" and opens the file
    listOfProcessedTweets = processTweets(dictionaryOfKeywords, tweets)     # processes tweets by calculating the happiness score and adding them to a list

    # store the lists for each region
    pacificList = listOfProcessedTweets[0]
    mountainList = listOfProcessedTweets[1]
    centralList = listOfProcessedTweets[2]
    easternList = listOfProcessedTweets[3]

    # calculates the happiness of each timezone
    pacificHappiness = timeZoneHappiness(pacificList)
    mountainHappiness = timeZoneHappiness(mountainList)
    centralHappiness = timeZoneHappiness(centralList)
    easternHappiness = timeZoneHappiness(easternList)

    # prints the happiness scores and the number of tweets found
    print("The happiness score for the Pacific timezone is", pacificHappiness, "with", len(pacificList), "tweets found.")
    print("The happiness score for the Mountain timezone is", mountainHappiness, "with", len(mountainList), "tweets found.")
    print("The happiness score for the Central timezone is", centralHappiness, "with", len(centralList), "tweets found.")
    print("The happiness score for the Eastern timezone is", easternHappiness, "with", len(easternList), "tweets found.")

    # creates a histogram
    import happy_histogram
    happy_histogram.drawSimpleHistogram(pacificHappiness, mountainHappiness, centralHappiness, easternHappiness)


## makes sure file name has ".txt" in it
# @param fileName is the name of the file
# @return returns the data inside the text file
def checkFile(fileName):
    # if ".txt" not included in the file name, adds ".txt"
    if ".txt" not in fileName :
        fileName = fileName + ".txt"
    inputData = open(fileName, "r", encoding="utf-8")      # opens the file
    return inputData            # returns the data from the file

## reads keyword file and returns the keyword as a key and the sentiment value as a value
# @param file is the data from a file
# @return returns the dictionary created
def readKeywords(file) :
    dictionaryOfData = {}
    for line in file :      # reads each line
        if line != "" :
            line = line.rstrip()        # strips the "/n" at the end of each line
            parts = line.split(",", 1)  #splits the line into the keyword and the sentiment value
            keyword = parts[0]          # stores the keyword into "keyword" variable
            happinessValue = int(parts[1])      # stores the sentiment value in "happinessValue"
            dictionaryOfData[keyword] = happinessValue      # creates dictionary with the keyword as the key and the happiness value as the value
    return dictionaryOfData

## processes the tweet data by calculating the happiness score of the tweet and appends it to a list from its given time zone
# @param keywordDictionary is the dictionary of the keyword and its values
# file is the file data that contains the tweets
# @return returns the list of happiness scores from each tweet in a list of its given region
def processTweets(keywordDictionary, file) :
    listOfPacific = []
    listOfMountain = []
    listOfCentral = []
    listOfEastern = []

    for line in file :          #reads each line from the file
        # makes sure the line being read has data
        if line != "" :
            line = line.rstrip()        # removes "\n" from each line
            line = line.lstrip("[")     # removes the first "[" of each line

            dataList1 = line.split("] ")    # splits the coordinate data

            # takes the coordinates and processes it to figure out what timezone the tweet came from
            unformattedCoord = dataList1[0].split(", ")         # splits the first portion of the coordinate and the second portion
            coordinateData = formatCoordinate(unformattedCoord[0], unformattedCoord[1])    # formats the coordinate into a list
            dataList2 = dataList1[1].split(" ", 3)      # splits the remaining data into 4 sections
            timeZone = convertTimeZone(coordinateData)      # converts the coordinate into the time zone it belongs to

            text = dataList2[3]         # stores the text from the tweet into "text"
            happinessScore = calculateHappiness(keywordDictionary, text)        #calculates the happiness score of that tweet
            if happinessScore != 0 :            # makes sure there were actual keywords in the tweet
                # adding the happiness score to the list of happiness scores in each time zone
                if timeZone == "Pacific" :
                    listOfPacific.append(happinessScore)
                elif timeZone == "Mountain" :
                    listOfMountain.append(happinessScore)
                elif timeZone == "Central" :
                    listOfCentral.append(happinessScore)
                elif timeZone == "Eastern" :
                    listOfEastern.append(happinessScore)

    return [listOfPacific, listOfMountain, listOfCentral, listOfEastern] # returns a multi-dimensional list with the lists of happiness scores from each time zone

## formats the coordinate data into a list
# @param coord1 is the x coordinate
# @param coord 2 is the y coordinate
# @return returns the entire coordinate as a list
def formatCoordinate(coord1, coord2) :
    formattedCoordinate = []
    # add data into a lsit
    formattedCoordinate.append(float(coord1))
    formattedCoordinate.append(float(coord2))
    return formattedCoordinate

## takes the coordinate data and figures out with time zone the coordinate belonds to
# @param coordinate is a list with the longitude-latitude pint
# @return returns time zone it belongs to
def convertTimeZone(coordinate) :
    # stores the x and y coordinate
    xCoord = coordinate[0]
    yCoord = coordinate[1]
    yMinimum = -125.24226
    yMaximum = -67.444574
    xMinimum = 24.660845
    xMaximum = 49.189787

    # each region includes every point up the the given "y-max"es below
    easternYMax = -67.444574
    centralYMax = -87.518395
    mountainYMax = -101.998892
    pacificYMax = -115.236428

    # makes sure the given coordinates are within the maximum and minimum ranges
    if (xCoord > xMinimum and xCoord < xMaximum) and (yCoord > yMinimum and yCoord < yMaximum) :
        if yCoord < pacificYMax :
            return "Pacific"
        elif yCoord < mountainYMax :
            return "Mountain"
        elif yCoord < centralYMax :
            return "Central"
        elif yCoord < easternYMax :
            return "Eastern"

## calculates the happiness score of each tweet
# @param keyDictonary is the dictionary of keywords
# @param tweet is the text from the tweet
# @return returns the happiness score of the tweet
def calculateHappiness(keyDictionary, tweet) :
    sentimentValue = 0
    countOfKeywords = 0
    specialCase = False
    if tweet != "" :        # makes sure tweet is not empty
        wordList = tweet.split()        # splits the tweet into individual words
        for word in wordList :      # analyzes each word in the tweet
            newWord = word.strip(".,?!").lower()    # clears punctuation from the word and updates to lowercase letters
            i = 0
            while not specialCase :
                if newWord[i] in ".,!?" and i != 0 :
                    if "!,.?" in newWord[i:] :
                        i = i + 1
                        word1 = newWord[:i].rstrip
                    else:
                        specialCase = True
                        break
                else:
                    i = i + 1

            for keyword in keyDictionary :      # for loop to start comparing newWord with keywords
                if newWord == keyword :
                    keywordValue = keyDictionary[keyword]           # stores the keyword value
                    sentimentValue = sentimentValue + keywordValue  # adds keyword value to the total sentiment value of the tweet
                    countOfKeywords = countOfKeywords + 1           # running count of the amount of keywords in the tweet
                elif specialCase and newWord[]:
                    keywordValue = keyDictionary[keyword]           # stores the keyword value
                    sentimentValue = sentimentValue + keywordValue  # adds keyword value to the total sentiment value of the tweet
                    countOfKeywords = countOfKeywords + 1           # running count of the amount of keywords in the tweet
    if countOfKeywords > 0 :        # makes sure there were actual keywords in the tweet
        happinessScore = sentimentValue/countOfKeywords     # calculates the happiness score
        return happinessScore       # returns the happiness score
    else :
        return 0        # if there were no keywords found, the function returns 0

## calculates the happiness score of the entire time zone
# @param listOfHappinessScores is the list of happiness scores from each region
# @return returns the happiness score of the entire time zone
def timeZoneHappiness(listOfHappinessScores) :
    sum = 0
    for element in listOfHappinessScores :      # runs through each happiness score
        sum = sum + element         # calculates the sum of happiness scores
    happiness = sum /len(listOfHappinessScores)     # divides the sum by the amount of scores/tweets
    return happiness


main()

