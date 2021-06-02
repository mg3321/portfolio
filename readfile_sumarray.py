#This program will print the sum of the elements in an array given by the user
#The user will give the name of a plain text file with the data when prompted
#The data values can be separated by a comma, space or both.
#The data can be one or multi line.
#File name must have extension .txt

def main():
#Get file name from user and arrange into 1d list
    userData = arrangeData(getFileName())
    message = "The sum of all elements in the file is:"
#Prints message and result from sumList()
    print(message, sumList(userData))

#Checks file exists and returns name if it does
def getFileName():
    check = False #False until file is found
    while not check:
        inPut = input("Please enter a file name.\n"
                      "File must have extension .txt:\n")
        try:
            file = open(inPut, 'r')
            check = True
            file.close()
        except FileNotFoundError:
            print("File not found, please try again.")
    return inPut

#Arranges data into flat list
def arrangeData(data):
    newArray = []
    element = ''
    dataFile = open(data, 'r')
    joinedLines = ' '.join(dataFile.readlines())
    for char in joinedLines + ' ':
        if char != ' ' and char != ',':
            element += char
        else:
            try:
#int raises value error when data is separated by comma and space.
                newArray.append(int(element))
                element = ''
            except ValueError:
                element = ''
    dataFile.close()
    return newArray

def sumList(array):
    total = 0 #Empty counter to start
    for element in array:
        total += element #Add each element to counter
    return total

main()

