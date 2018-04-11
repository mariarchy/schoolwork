def main() :
    # Asks user for the shape they'd like to calculate the volume of
    shape = input("What shape would you like to calculate the volume of? ")
    # Set valid to False so that if you want to end the loop, set valid to True and close the loop
    valid = False
    # Create list for the cube volumes calculated
    listOfCube = []
    # Create list for the pyramid volumes calculated
    listOfPyramid = []
    # Create list for the ellipsoid volumes calculated
    listOfEllipsoid = []
    # Create a list of accepted entries
    validEntries = ["cube", "pyramid", "ellipsoid", "quit"]

    # If user enters "quit" the first time being asked to enter a shape, the loop will not begin.
    if shape == validEntries[3] :
        print("You have come to the end of the session. \nYou did not perform any volume calculations.")
        valid = True


    while valid == False :
        shape = shape.lower()                           # Set the string from input into lowercase letters to match the valid entries

        if shape not in validEntries :                  # if shape entered is invalid, it goes through the loop again
            shape = input("Please enter a valid shape: ")

        # if shape entered is "cube"
        if shape == validEntries[0] :
            cubeData = list(cube())                   # create a new list out of the data returned from cube()
            # adding the final element in cube() (the volume) to the list of cube volumes
            listOfCube.append(cubeData[len(cubeData) - 1])
            # prints the statement that tells the dimensions and the volume
            print("The volume of a", shape, "with a side length of", cubeData[0], "is", cubeData[len(cubeData) - 1])

        # if shape entered is "pyramid"
        elif shape == validEntries[1] :
            pyramidData = list(pyramid())            # create a new list out of the data returned from pyramid()
            # adding the final element in pyramid() (the volume) to the list of pyramid volumes
            listOfPyramid.append(pyramidData[len(pyramidData) - 1])
            # prints the statement that tells the dimensions and the volume
            print("The volume of a", shape, "with a base of", pyramidData[0], "and a height of", pyramidData[1], "is", pyramidData[len(pyramidData) - 1])

        # if shape entered is "ellipsoid"
        elif shape == validEntries[2] :
            ellipsoidData = list(ellipsoid())        # create a new list out of the data returned from ellipsoid()
            # adding the final element in ellipsoid() (the volume) to the list of ellipsoid volumes
            listOfEllipsoid.append(ellipsoidData[len(ellipsoidData) - 1])
            # prints the statement that tells the dimensions and the volume
            print("The volume of a", shape, "with radius lengths of %d, %d, and %d" % (ellipsoidData[0], ellipsoidData[1], ellipsoidData[2]), "is", ellipsoidData[len(ellipsoidData) - 1])

        # ask the user if they want to calculate another shape or quit
        userInput = input("To continue, press enter. To quit, enter 'quit'")

        # if the input is "", the program prompts for a new shape
        if userInput == "" :
            shape = input("Please enter another shape: ")

        # if the input is "quit" the loops ends and prints the final statement ending()
        elif userInput.lower() == "quit" :
            # ending() prints the entire final statement, with lists of all the volumes calculated
            ending(listOfCube, listOfPyramid, listOfEllipsoid)
            # Set valid to True so that the loops ends
            valid = True


## Computes the volume of a cube.
# @param no parameters
# @return the side length of the cube and the volume of the cube
def cube() :
    sideLength = int(input("Please enter the side length: "))          # The assumption is that the input is a positive integer value
    vol = float(round(sideLength**3, 1))                               # Formula for the volume of a cube, rounded to 1 decimal point
    data = [sideLength, vol]                                           # Creates a list with the side length of the cube and the calculated volume
    return data                                                        # Returns the list in "data"

## Computes the volume of a pyramid.
# @param no parameters
# @return the base, height, and the volume of the pyramid
def pyramid() :
    base = int(input("Please enter the base: "))                # The assumption is that the input is a positive integer value
    height = int(input("Please enter the height: "))            # The assumption is that the input is a positive integer value
    vol = float(round(0.5 * (base**2) * height, 1))             # Formula for the volume of a pyramid, rounded to 1 decimal place
    data = [base, height, vol]                                  # Creates a list with the base, height, and calculated volume of the pyramid
    return data                                                 # Returns the list in "data"

## Computes the volume of a ellipsoid.
# @param no parameters
# @return the radii and the volume of the ellipsoid
def ellipsoid() :
    r1 = int(input("Please enter the first radius: "))        # The assumption is that the input is a positive integer value
    r2 = int(input("Please enter the second radius: "))       # The assumption is that the input is a positive integer value
    r3 = int(input("Please enter the third radius: "))        # The assumption is that the input is a positive integer value
    from math import pi
    vol = float(round((4/3) * pi * r1 * r2 * r3, 1))          # Formula for the volume of a ellipsoid, rounded to 1 decimal point
    data = [r1, r2, r3, vol]                                  # Creates a list with the three radii and the calculated volume of the ellipsoid
    return data                                               # Returns the list in "data"

## Computes the list of volumes for each shape and prints them
# @param listOfCube is the list of the cube volumes calculated
# @param listOfPyramid is the list of pyramid volumes calculated
# @param listOfEllipsoid is the list of ellipsoid volumes calculated
# @return returns and prints the complete, formatted list of volumes from each shape
def ending(listOfCube, listOfPyramid, listOfEllipsoid) :
    print("You have come to the end of the session")
    print("The volumes calculated for each shape are shown below")
    listOfCube.sort()                       # Sorts the list of cube volumes from least to greatest
    listOfPyramid.sort()                    # Sorts the list of pyramid volumes from least to greatest
    listOfEllipsoid.sort()                  # Sorts the list of ellipsoid volumes from least to greatest

    # Creates an empty string to be added to with each of the volumes from each shape
    finalCubeList = ""
    finalPyramidList = ""
    finalEllipsoidList = ""

    # If there are no volume calculations, print this:
    blankEntry = "No computations for this shape"

    # If there are volume calculations
    if len(listOfCube) > 0 :
        # For loop with the range of the length of the list, this goes through each element in the list of cube volumes
        # and adds it to the new string
        for i in range(len(listOfCube)) :
            # avoids repetition if len(listOfCube) - 1 = 0 aka if the len(listOfCube) = 1, meaning there's only 1 element
            if i < len(listOfCube) - 1 :
                listOfCube[i] = str(listOfCube[i])
                finalCubeList = finalCubeList + listOfCube[i] + ", "
            # final if statement for the final entry, so that the comma at the end gets removed
            if i == len(listOfCube) - 1 :
                listOfCube[i] = str(listOfCube[i])
                finalCubeList = finalCubeList + listOfCube[i]
        # Prints the final list, with all the cube volumes
        print("Cube:", finalCubeList)
    else :
        # Prints the blankEntry string if there are no elements
        print("Cube:", blankEntry)

    # If there are volume calculations
    if len(listOfPyramid) > 0 :
        # For loop with the range of the length of the list, this goes through each element in the list of pyramid volumes
        # and adds it to the new string
        for i in range(len(listOfPyramid)) :
            # avoids repetition if len(listOfPyramid) - 1 = 0 aka if the len(listOfPyramid) = 1, meaning there's only 1 element
            if i < len(listOfPyramid) - 1 :
                listOfPyramid[i] = str(listOfPyramid[i])
                finalPyramidList = finalPyramidList + listOfPyramid[i] + ", "
            # final if statement for the final entry, so that the comma at the end gets removed
            if i == len(listOfPyramid) - 1 :
                listOfPyramid[i] = str(listOfPyramid[i])
                finalPyramidList = finalPyramidList + listOfPyramid[i]
        # Prints the final list, with all the pyramid volumes
        print("Pyramid:", finalPyramidList)
    else :
        # Prints the blankEntry string if there are no elements
        print("Pyramid:", blankEntry)

    # If there are volume calculations
    if len(listOfEllipsoid) > 0 :
        # For loop with the range of the length of the list, this goes through each element in the list of ellipsoid volumes
        # and adds it to the new string
        for i in range(len(listOfEllipsoid)) :
            if i < len(listOfEllipsoid) - 1 :
                # avoids repetition if len(listOfEllipsoid) - 1 = 0 aka if the len(listOfEllipsoid) = 1, meaning there's only 1 element
                listOfEllipsoid[i] = str(listOfEllipsoid[i])
                finalEllipsoidList = finalEllipsoidList + listOfEllipsoid[i] + ", "
            # final if statement for the final entry, so that the comma at the end gets removed
            if i == len(listOfEllipsoid) - 1 :
                listOfEllipsoid[i] = str(listOfEllipsoid[i])
                finalEllipsoidList = finalEllipsoidList + listOfEllipsoid[i]
        # Prints the final list, with all the ellipsoid volumes
        print("Ellipsoid:", finalEllipsoidList)
    else :
        # Prints the blankEntry string if there are no elements
        print("Ellipsoid:", blankEntry)
    return()

main()


