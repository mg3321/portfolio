##This is an exercise in object oriented programming that I found online
##I defined parent and child classes for different types of product.

class Product:#parent class for all product categories
    def __init__(self, product_ID, price, prime_eleigible, stock, date_added):
        self.__product_ID = product_ID
        self.__price = price
        self.__prime_eleigible = prime_eleigible
        self.__stock = stock
        self.__date_added = date_added

    #setters and getters for each attribute
    def set_product_ID(self, value):
        self.__product_ID = value

    def get_product_ID(self):
        return self.__product_ID

    def set_price(self, value):
        self.__price = value

    def get_price(self):
        return self.__price

    def set_prime_eligible(self, value):
        self.__prime_eleigible = value

    def get_prime_eligible(self):
        return self.__prime_eleigible

    def set_stock(self, value):
        self.__stock = value

    def get_stock(self):
        return self.__stock

    def set_date_added(self, value):
        self.__date_added = value

    def get_date_added(self):
        return self.__date_added

    def info(self):#prints product info
        if self.get_prime_eligible():
            PE = "is Prime eligible"
        else:
            PE = "is NOT Prime eligible"
        print("Product I.D.:", self.get_product_ID(), "\n",
              "Price: £" + str(self.get_price()), "\n",
              self.get_product_ID(), PE, "\n",
              "Current stock level:", self.get_stock(), "\n",
              "Date added:", self.get_date_added())


class Book(Product):#child of Product class
    def __init__(self, productID, price, prime_eleigible, stock, date_added,
                 title, author, num_pages, publisher, publication_date):
        super().__init__(productID, price, prime_eleigible, stock, date_added)
        self.__title = title
        self.__author = author
        self.__num_pages = num_pages
        self.__publisher = publisher
        self.__publication_date = publication_date

    #setters and getters for each attribute
    def set_title(self, value):
        self.__title = value

    def get_title(self):
        return self.__title

    def set_author(self, value):
        self.__author = value

    def get_author(self):
        return self.__author

    def set_num_pages(self, value):
        self.__num_pages = value

    def get_num_pages(self):
        return self.__num_pages

    def set_publisher(self, value):
        self.__publisher = value

    def get_publisher(self):
        return self.__publisher

    def set_publication_date(self, value):
        self.__publication_date = value

    def get_publication_date(self):
        return self.__publication_date
 
    def info(self):#overrides Product class's .info() method
        super().info()
        print("Title:", self.get_title(), "\n",
              "Author:", self.get_author(), "\n",
              "Number of pages:", self.get_num_pages(), "\n",
              "Publisher:", self.get_publisher(), "\n",
              "Publication Date:", self.get_publication_date(), "\n")


class Clothing(Product):#child of Product class 
    def __init__(self, productID, price, prime_eleigible, stock, date_added,
                 brand_name, category, size, colour):
        super().__init__(productID, price, prime_eleigible, stock, date_added)
        self.__brand_name = brand_name
        self.__category = category
        self.__size = size
        self.__colour = colour

    #setters and getters for each attribute
    def set_brand_name(self, value):
        self.__brand_name = value

    def get_brand_name(self):
        return self.__brand_name

    def set_category(self, value):
        self.__category = value

    def get_category(self):
        return self.__category

    def set_size(self, value):
        self.__size = value

    def get_size(self):
        return self.__size

    def set_colour(self, value):
        self.__colour = value

    def get_colour(self):
        return self.__colour

    def info(self):#overrides Product class's .info() method
        super().info()
        print("Brand name:", self.get_brand_name(), "\n",
              "Category:", self.get_category(), "\n",
              "Size:", self.get_size(), "\n",
              "Colour:", self.get_colour(), "\n")
              

class VideoGame(Product):#child of Product class
    def __init__(self, productID, price, prime_eleigible, stock, date_added,
                 title, platform, PEGI_rating, release_date):
        super().__init__(productID, price, prime_eleigible, stock, date_added)
        self.__title = title
        self.__platform = platform
        self.__PEGI_rating = PEGI_rating
        self.__release_date = release_date

    #setters and getters for each attribute
    def set_title(self, value):
        self.__title = value

    def get_title(self):
        return self.__title

    def set_platform(self, value):
        self.__platform = value

    def get_platform(self):
        return self.__platform

    def set_PEGI_rating(self, value):
        self.__PEGI_rating = value

    def get_PEGI_rating(self):
        return self.__PEGI_rating

    def set_release_date(self, value):
        self.__release_date = value

    def get_release_date(self):
        return self.__release_date

    def info(self):#overrides Product class's .info() method
        super().info()
        print("Title:", self.get_title(), "\n",
              "Platform:", self.get_platform(), "\n",
              "PEGI rating:", self.get_PEGI_rating(), "\n",
              "Release date:", self.get_release_date(), "\n")
              

#instances of book object and calling .info() method on each
book1 = Book(1, 12.99, True, 10, "49/18/4467",
            "Barry Trotter", "Tarry Brotter", 329, "Mongoose", "67/49/7412")
book1.info()

book2 = Book(2, 10.99, True, 10, "102/3/2097",
            "Gotta Get Theroux This", "Louis Theroux", 416, "Macmillan", "19/09/2019")
book2.info()
book2.set_price(14.99)#change price of book2
book2.info()

book3 = Book(3, 12.99, True, 10, "This very moment",
            "Bible stories in cockney rhyming slang", "Keith Park", 32, "Jessica Kingsley", "15/02/2009")
book3.info()

#instances of Clothing object and calling .info() method on each
clothing1 = Clothing(4, 3.99, False, 44, "39/14/9043",
                     "Fauxsaci", "Female", 123, "Greenishbrown")
clothing1.info()

clothing2 = Clothing(5, 54.99, True, 23, "19/19/1919",
                     "Primonk", "Male", 6, "Yellowypurple")
clothing2.info()
clothing2.set_brand_name("Habithat")#change brand name of clothing2
clothing2.info()

clothing3 = Clothing(6, 7.03, False, 0, "24/12/6315",
                     "H&R", "Female", 30, "Lightblack")
clothing3.info()

#instances of VideoGame object and calling .info() method on each
vg1 = VideoGame(7, 59.99, True, 4, "90/40/1642",
                "Grand Theft Bicycle", "Z-Case", "34", "Pending")
vg1.info()

vg2 = VideoGame(8, 59.99, False, 7, "32/14/2222",
                "Need For Swede", "BS-4", "11", "Whenever we say it is")
vg2.info()
vg2.set_PEGI_rating("72")#change brand name of vg2
vg2.info()

vg3 = VideoGame(9, 59.99, True, 9, "15/04/2020",
                "Call Of Booty", "Nintendo", "1", "Soon, we 'promise'")
vg3.info()
              
