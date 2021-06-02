'''This program use the norwthwest corner and stepping stone algorithms to
minimise cost of transporting units from a range of suppliers to a range
of destinations, it will handle balanced and unbalanced problems, and problems
with any number of suppliers or destinations, balanced or unbalanced.
The program imports supply demand and price data from .txt files. It requires
three seprate files, single line for supply and demand with data separetd
by spaces eg.6 5 8. Price data must be separated by spaces and can be multi
line, eg. 3 4 5
          4 3 2
          7 5 8'''
import sys

def main(): 
    '''Main function'''
    getData()
    generateTables()
    northWest()
    steppingStone()

def getData(): 
    '''Import and prepare data from text files'''
    global supply, demand, priceTable
    supply = getSupply()
    demand = getDemand()
    balance() # balance problem if neccessary
    priceTable = getPriceTable()

def balance():
    '''Check total values of supply and demand
        and balance if neccessary'''
    global column, row
    ts = sum(supply)
    td = sum(demand)
    if(ts > td):
        column += 1 #Add dummy column
        demand.append(ts - td) #Add difference to dummy demand

    elif(td > ts):
        row += 1 #Add dummy row
        supply.append(td - ts) #Add difference to dummy supply


def generateTables():

    global NWTable, improvTable
    NWTable = [[None] * column for i in range(row)] #NorthWest/allocation table
    improvTable = [[None] * column for i in range(row)]
    #Table of improvement indicies

def getTextFile():
    '''Generised function for importing text files. The function will check
that the file exisits before moving on to processing'''
    check = False
    while not check:
        inPut = input("Enter file name: ")
        inPut += ".txt"
        try:
            file = open(inPut, "r")
            check = True
            file.close()
        except FileNotFoundError:
            print("File not found, please try again.")
        
    return inPut


def getPriceTable():
    '''Import and process price data'''
        
    data = []
    data2 = []

    print("Please enter file name for price table,",
          "without extension.")
    priceFile = getTextFile()
    pFile = open(priceFile, "r")
    lines = pFile.readlines()

    for line in lines:
        data.append(line.strip())

    daty = " ".join(data) 
    element = ""

    for l in daty + " ":
       
        if(l != " "):
            element += l
        else:
            data2.append(element)
            element = ""

    

    priceTable = [[0] * column for i in range(row)]

    s = 0
    for y in range(row2):
        for x in range(column2):
            priceTable[y][x] = int(data2[s])
            s += 1

    pFile.close()

    return priceTable

 
def getSupply():
    '''Import and process supply data'''
    global mmcSupply
    supply = []
    mmcSupply = []

    print("Please enter file name for supply values,",
          "without extension.")

    supplyFile = getTextFile()
    sFile = open(supplyFile, "r")
    line = [sFile.readline()]
    liney = " ".join(line)
    element = ""

    for l in liney + " ":
       
        if(l != " "):
            element += l
        else:
            supply.append(int(element))
            mmcSupply.append(int(element))
            element = ""

    sFile.close()

    global row, row2
    row = len(supply)
    row2 = row #This variable is used to populate price table
               #In case problem is balanced later, and row value changes
    
    return supply


def getDemand():
    '''Import and process demand data'''
    global mmcDemand
    demand = []
    mmcDemand = []

    print("Please enter file name for demand values,",
          "without extension.")

    demandFile = getTextFile()
    dFile = open(demandFile, "r")
    line = [dFile.readline()]
    liney = " ".join(line)
    element = ""

    for l in liney + " ":
       
        if(l != " "):
            element += l
        else:
            demand.append(int(element))
            mmcDemand.append(int(element))
            element = ""

    global column, column2
    column = len(demand)
    column2 = column#This variable is used to populate price table
               #In case problem is balanced later, and column value changes
    
    dFile.close()

    return demand


def checkCells():
    '''This function counts and returns the number of occupied cells'''
    Cells = 0
    for y in range(row):
        for x in range(column):
            if(NWTable[y][x] != None):
                Cells += 1
            
    return Cells


def northWest():
    '''NorthWest corner function for initial allocation'''
    s = 0
    d = 0
    nx = 0
    ny = 0
    ts2 = sum(supply)

    while ts2 > 0:

        if supply[s] == demand[d]:
            NWTable[ny][nx] = supply[s]
            ts2 -= supply[s]
            s += 1
            d += 1
            nx += 1
            ny += 1

        elif(supply[s] < demand[d]):
            NWTable[ny][nx] = supply[s]
            demand[d] = (demand[d] - supply[s])
            ts2 -= supply[s]
            ny += 1
            s+= 1

        elif(supply[s] > demand[d]):
            NWTable[ny][nx] = demand[d]
            ts2 -= demand[d]
            supply[s] = (supply[s] - demand[d])
            nx += 1
            d += 1

def steppingStone():
    '''This is the stepping stone function, it implements all the steps of the
    algorithm to minimse transport cost'''
    global sNo
    sNo = 1
    print("\nPrinting solution", sNo)
    printSolution()
    shadowCost()
    improvIndicies()
    while not optimal():#Loop breaks when all improvement indices are positive
        betterSolution()
        sNo += 1
        print("\nPrinting solution", sNo)
        printSolution()
        shadowCost()
        improvIndicies()
    print("Solution optimal as no negative improvment indicies.")

def printSolution():
    '''This function prints the current solution to the console, any dummy or
    zero cost routes are not printed, but still visible on the NWTable'''
    
    totalCost = 0
    print(NWTable)

    for i in range(row):
        for j in range(column):
            if(NWTable[i][j] != None and NWTable[i][j] != 0 and
               priceTable[i][j] != 0):
                unit = "unit"
                if NWTable[i][j] != 1:
                    unit += "s"
                print(NWTable[i][j],unit,"from supplier",i,"to destination",j,"at",
                      priceTable[i][j],"per unit =", NWTable[i][j] * priceTable[i][j])
                totalCost += (NWTable[i][j] * priceTable[i][j])

    print("Total cost of solution",sNo,"=", totalCost)

def shadowCost():
    '''Function to calculate shadow costs. This function is recursive to
    prevent degeneracy'''
    occupieds = checkCells()#Count occupied cells

    if occupieds < column + row -1:#If true, a zero is needed
        placeZero()

    else:
        global shadowY, shadowX
        shadowY = [0]
        shadowX = []
        for y in range(row -1):
            shadowY.append(None)
        for x in range(column):
            shadowX.append(None)

        for u in range(column + row):
            for y in range(row):
                for x in range(column):
                    if(NWTable[y][x] != None):
                        if shadowY[y] != None and shadowX[x] == None:
                            shadowX[x] = priceTable[y][x] - shadowY[y]
                        elif shadowX[x] != None and shadowY[y] == None:
                            shadowY[y] = priceTable[y][x] - shadowX[x]
                        
    empty = 0 #Check that shadow costs have been fully calculated
    for b in range(row):
        if shadowY[b] == None:
            empty += 1
    for r in range(column):
        if shadowX[r] == None:
            empty += 1

    return empty == 0

def placeZero():
    '''This function places a zero in the north west table if necessary'''
    for y in range(row):
        for x in range(column):
            if NWTable[y][x] == None:
                NWTable[y][x] = 0 #Place 0 in empty cell
                if not shadowCost(): #Test position of 0 by calculating shadow costs
                    NWTable[y][x] = None #If not possible, cell reset, loop continues
                else:
                    return True

def improvIndicies():
    '''This function calculates the improvement indicies of the unoccupied
    cells'''
    print("Calculating improvment indicies.")
    for y in range(row): #Populate improv table with None
        for x in range(column):
            improvTable[y][x] = None

    for y in range(row): #Populate table with improvement indicies
        for x in range(column):
            if(NWTable[y][x] == None):
                improvTable[y][x] = priceTable[y][x] - (shadowY[y] + shadowX[x])
        
    print(improvTable)

def optimal():
    '''This function checks the values of the improvement indicies to check if
    the solution is optimal'''
    negs = 0
    for y in range(row):
        for x in range(column):
            if(improvTable[y][x] != None):
                if(improvTable[y][x] < 0):
                    negs += 1
    if negs > 0:
        print("Solution not optimal")

    return(negs == 0)#If False, solution not optimal, if true, optimal.



def entryCell():
    '''Find coordinates of entry cell '''
    mini = 0
    for h in range(row):
        for g in range(column):
            if(improvTable[h][g] != None):
                if(improvTable[h][g] < mini):
                    mini = improvTable[h][g]

    for y in range(row):
         for x in range(column):
            if(improvTable[y][x] == mini):
                return [[y,x]]

def pathFinder():
    '''This function consturcts a theta path for solution adjustment.
    It was heavily inspired by a function from another program,
     a link to which is here:
     http://code.activestate.com/recipes/576575-stepping-stone-algorithum-for-solving-the-tranship/'''

##    x = entryCellX()
##    y = entryCellY()
    

    thetaTable = entryCell()
    y = thetaTable[0][0]
    x = thetaTable[0][1]
    print("Entering at cell:",y,",",x,sep="")

    NWTable[y][x] = 0#Entry cell set to 0 to perform operations later

    

    if not lookHor(thetaTable, y, x, y, x):
        '''This code executes if a theta path cannot be found. I have not yet
        found a case where this happens, and not from lack of trying. A bag of salt
        and a bolt of silk will be awarded to the first person who can find a case that will
        make this code execute. In the unlikely event of this piece of code executing,
        the minimum cell cost method is implemented to provide a better initial allocation.'''

        print("Unable to establish theta path. Referring to minimum cell cost method.")
        minimumCellCost()
        sys.exit()#Terminate program
        
 
        
    return thetaTable


def lookHor(thetaTable, y, x, y1, x1):
    '''This function was heavily inspired by a function from another program,
    a link to which is here:
    http://code.activestate.com/recipes/576575-stepping-stone-algorithum-for-solving-the-tranship/'''

    for i in range(column):
        if(i != x and NWTable[y][i] != None):
            if(i == x1):
                thetaTable.append([y,i])
                return True
            if(lookVer(thetaTable, y, i, y1, x1)):
                thetaTable.append([y,i])
                return True
    return False#Not found


def lookVer(thetaTable, y, x, y1, x1):
    '''This function was heavily inspired by a function from another program,
     a link to which is here:
     http://code.activestate.com/recipes/576575-stepping-stone-algorithum-for-solving-the-tranship/'''

    for i in range(row):
        if(i != y and NWTable[i][x] != None):
            if lookHor(thetaTable, i, x, y1, x1):
                thetaTable.append([i, x])
                return True
    return False#Not found

def betterSolution():
    ''''This function finds the theta minimum and adjusts the northwest table
    accordingly. This function was also heavily inspired by a function from another program,
     a link to which is here:
     http://code.activestate.com/recipes/576575-stepping-stone-algorithum-for-solving-the-tranship/'''
 

    thetaMin = 999999999999 #Hopefully larger than any theta minimum

    thetaTable = pathFinder()#Calculate theta path
    
    
    for i in range(1, len(thetaTable), 2):#work out theta minimum

        if(NWTable[thetaTable[i][0]][thetaTable[i][1]] != None):
            t = NWTable[thetaTable[i][0]][thetaTable[i][1]]
            if (t < thetaMin):
                thetaMin = t
    for i in range(1, len(thetaTable), 2): #Perform operations on cells in theta path
        NWTable[thetaTable[i][0]][thetaTable[i][1]] -= thetaMin
        if NWTable[thetaTable[i][0]][thetaTable[i][1]] == 0:
            NWTable[thetaTable[i][0]][thetaTable[i][1]] = None
            print("Exiting at cell: ",thetaTable[i][0],",",thetaTable[i][1],sep="")
        NWTable[thetaTable[i-1][0]][thetaTable[i-1][1]] += thetaMin

def minimumCellCost():
    
    priceList = []
    mini = 999999999
    mmcTable = [[None]* column2 for i in range(row2)]

    for f in range(row2):#Flatten price table into a 1d array
        for j in range(column2):
            priceList.append(priceTable[f][j])

    while not sortd(priceList):#Sort list in ascending order
        for k in range(1,len(priceList),1):
            if priceList[k-1] > priceList[k]:
                temp = priceList[k]
                priceList[k] = priceList[k-1]
                priceList[k-1] = temp
            


    q = priceList[0]
    priceList2 = [q]
    for k in range(len(priceList)):#Remove duplicate values
        if priceList[k] != q:
            priceList2.append(priceList[k])
            q = priceList[k]
            

            
    for tt in priceList2:#Allocate amounts starting with lowest cost
        for b in range(row2):
            for bb in range(column2):
                if priceTable[b][bb] == tt:

                    if mmcSupply[b] == mmcDemand[bb] or mmcSupply[b] < mmcDemand[bb]:
                        mmcTable[b][bb] = mmcSupply[b]
                        mmcSupply[b] -= mmcTable[b][bb]
                        mmcDemand[bb] -= mmcTable[b][bb]
     

                    elif(mmcSupply[b] > mmcDemand[bb]):
                        mmcTable[b][bb] = mmcDemand[bb]
                        mmcSupply[b] -= mmcTable[b][bb]
                        mmcDemand[bb] -= mmcTable[b][bb]

    print(mmcTable)
    totalCost = 0
    for kk in range(row2):
        for uu in range(column2):
            if mmcTable[kk][uu] != 0:
                print(mmcTable[kk][uu], "units from supplier", kk, "to destination",
                      uu, "at", priceTable[kk][uu], "per unit.",  )
                totalCost += priceTable[kk][uu] * mmcTable[kk][uu]

    print("Total cost using minimum cell cost method =",totalCost)

def sortd(List):
    for k in range(1,len(List),1):
        if List[k-1] > List[k]:
            return False
    return True



main()

