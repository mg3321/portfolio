#This program will allow a user to view a list of avilable items (stored in a separate file
#in dictionary form), and add items to a basket (also dictionary form)
#Each inventory item has a key, a price and a stock level, the program will ensure
#stock levels are maintained and not exceeded.
import inventory

inv = inventory.Inventory #shortcut for accessing inventory
basket = {} #empty basket

def yesNo(prompt): #General function for yes/no questions
    while True:
        response = input(prompt)
        if response == 'y' or response == 'Y':
            return True
        elif response == 'n' or response == 'N':
            return False
        else:
            print('Sorry I did not understand, please try again.')
            continue

def quantityIn(prompt, stock):#function for getting quantity value from user
    while True:
        try:
            quant = int(input(prompt))
            if quant > stock or quant < 1:#will not accept value higher than current stock 
                print('Sorry we do not have that quantity in stock.\n',
                      'Please try different a amount')
                continue
            break
        except ValueError:
            print('Invalid entry, please try again.')
    return quant

def printInventory(): #prints inventory in better format
    print('Our current inventory is....')
    item = 1
    for key in inv:
        print(str(item) + '. ' + key + ' at £'+ str(inv[key][0]) + ' each.')
        item += 1

def printBasket():#prints basket and totals when user is done
    grandTotal = 0
    print('Your basket.....')
    for product in basket:
        subTotal = round((inv[product][0] * basket[product]), 2)
        print(str(basket[product]) + ' ' + str(product) + '(s)', 'totals:'
              + str(subTotal))
        grandTotal += subTotal
    print('The grand total is: £' + str(round(grandTotal, 2)))
    
def updateBasket(product): #updates basket with new item and quantity
    print('We have ' + str(inv[product][1]) + ' in stock.')#also updates stock value in inventory
    quantity = quantityIn('Please enter the desired quantity: ',
                       inv[product][1])
    inv[product][1] -= quantity #Update stock level
    if product in basket:
        basket[product] += quantity #Accumulates quantity if basket item is duplicated 
    else:
        basket[product] = quantity #Adds new item to basket
    print(str(quantity) + ' ' + str(product) + '(s) added to basket.')

def addToBasket(): #function for getting basket items from user
    if yesNo('\nWould you like to add a product to your basket? Y/N'):
        while True:
            product = input('Please type the product name: ')
            if product in inv:#Checks product exists
                updateBasket(product)
                if yesNo('\nWould you like to add another product to your basket? Y/N'):
                    continue
                else:
                    printBasket()#User is ready for checkout
                    break
            else:
                print('Product not found, please try again.')
                continue
    else:
        print('Goodbye')
    
def main():
    printInventory()
    addToBasket()

main()
