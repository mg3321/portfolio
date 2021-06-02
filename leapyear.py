#This program will take a year value from the user and return
#True if it is a leap year and False if it is not
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def main():
    Year = int(input("Please Enter a Year:"))
    print(leap(Year))
        

main()
