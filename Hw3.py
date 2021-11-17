'''Real Estate Advisor Program:
We want to write a real estate consulting program that has the ability to add, search, rent and sell real estate.
The program consists of two parts, each of which includes several different parts:   '''
'''1)Enter property and owner information '''

'''A)supper class:'''

class Real_Estate:
    def __init__(self,search,add,rent,sale):
        self.search=search
        self.add=add
        self.rent=rent
        self.sale=sale

'''B)Address class(show address and Edit address specification'''

class Address:
    def __init__(self,City_name,Street_name,Number_plates,Postal_code):
        self.City_name=City_name
        self.Street_name=Street_name
        self.Number_plates=Number_plates
        self.Postal_code=Postal_code

    def __repr__(self):
        return  str(self.__dict__)

    @classmethod
    def add_address(cls):
        City_name = input('please enter  City_name:')
        Street_name = input('please enter Street_name:')
        Number_plates = int(input('please enter Number_plates:'))
        Postal_code = int(input('please enter  Postal_code:'))
        return cls(City_name=City_name, Street_name=Street_name, Number_plates=Number_plates, Postal_code=Postal_code)

    print('**********Get and edit the address class**********')
    def edit_address(self):
        while True:
            print("""\n 1)City_name \n 2)Street_name \n 3)Number_plates \n 4)postal_code \n 5) exit""")
            choice_number= int(input(' please enter choice : '))
            if choice_number == 1:
                self.City_name = input('please enter new city_name : ')
                return self.City_name
            if choice_number == 2:
                self.Street_name = input('please enter new Street_name : ')
                return self.Street_name
            if choice_number== 3:
                self.Number_plates = int(input('please enter new Number_plates : '))
                return self.Number_plates
            if choice_number == 4:
                self.Postal_code = int(input('please enter new Postal_code : '))
                return self.Postal_code
            if choice_number == 5:
                return 'exit'

'''c)person class(show address and Edit address specification'''

class person:
    def __init__(self,first_name,last_name,National_Code,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.National_Code=National_Code
        self.phone_number=phone_number
    def __repr__(self):
        return  str(self.__dict__)

    @classmethod
    def add_person(cls):
       first_name=input('please enter  first_name:')
       last_name=input('please enter  last_name:')
       National_Code=int(input('please enter  National_Code:'))
       phone_number=int(input('please enter  phone_number:'))
       return cls(first_name=first_name,last_name=last_name,National_Code=National_Code,phone_number=phone_number)


    def edit_person(self):
        print('**********Get and edit the person class**********')
        while True:
            print("""\n 1)first_name \n 2)last_name \n 3)National_Code \n 4)phone_number \n 5) exit""")
            choice_number= int(input(' please enter choice : '))
            if choice_number == 1:
                self.first_name = input('please enter new first_name : ')
                return self.first_name
            if choice_number == 2:
                self.last_name = input('please enter new last_name : ')
                return self.last_name
            if choice_number== 3:
                self.National_Code = int(input('please enter new National_Code : '))
                return self.National_Code
            if choice_number == 4:
                self.phone_number = int(input('please enter new phone_number : '))
                return self.phone_number
            if choice_number == 5:
                return 'exit '
    # @staticmethod
    # def validation_address_email():
    #     y=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{1,3})$/
    #     pass



'''D)Apartment class(show address and Edit address specification'''

class Apartment:
    def __init__(self,Owner,Tenant,Number_rooms,Area,Floor,Number_classes,Address,Phone
                 ,active,inactive,Mortgage_amount,Rent_price,selling_price,onsale,Rent):
        self.Owner=Owner
        self.Tenant=Tenant
        self.Number_rooms=Number_rooms
        self.Area=Area
        self.Floor=Floor
        self.Number_classes=Number_classes
        self.Address=Address
        self.Phone=Phone
        self.active=active
        self.inactive=inactive
        self.Mortgage_amount=Mortgage_amount
        self.Rent_price=Rent_price
        self.selling_price=selling_price
        self.onsale=onsale
        self.Rent=Rent
    def __repr__(self):
        return  str(self.__dict__)


    @classmethod
    def add_apartment(cls):
       Owner=input('please enter Owner:')
       Tenant=input('please enter Tenant:')
       Number_rooms=int(input('please enter Number_rooms:'))
       Area=int(input('please enter Area:'))
       Floor=int(input('please enter Floor:'))
       Number_classes=int(input('please enter Number_classes:'))
       Address=input('please enter Address:')
       Phone=int(input('please enter Phone:'))
       active=input('please enter Phone:')
       inactive=input('please enter Phone:')
       Mortgage_amount=int(input('please enter Phone:'))
       Rent_price=int(input('please enter Phone:'))
       selling_price=int(input('please enter Phone:'))
       onsale=input('please enter Phone:')
       Rent=int(input('please enter Phone:'))
       return cls(Owner=Owner,Tenant=Tenant,Number_rooms=Number_rooms,Area=Area,Floor=Floor,
                   Number_classes=Number_classes,Address=Address,Phone=Phone,active=active,inactive=inactive,
                   Mortgage_amount=Mortgage_amount,Rent_price=Rent_price,selling_price=selling_price,onsale=onsale,Rent=Rent)
    def edit_apartment(self):
        print('**********Get and edit the apartment  class**********')
        while True:
            print("""\n 1)Owner \n 2)Tenant \n 3)Number_rooms \n 4)Area \n 5) Floor \n 6) Number_classes \n 7)Address \n 8)Phone \n
             9)active \n 10)inactive \n 11)Mortgage_amount \n 12)Rent_price \n 13)selling_price \n 14)onsale \n 15)Rent \n 16)exit""")
            choice_number = int(input(' please enter choice : '))
            if choice_number == 1:
                self.Owner = input('please enter new Owner : ')
                return self.Owner
            if choice_number == 2:
                self.Tenant = input('please enter new Tenant : ')
                return self.Tenant
            if choice_number == 3:
                self.Number_rooms = int(input('please enter new Number_rooms : '))
                return self.Number_rooms
            if choice_number == 4:
                self.Area = int(input('please enter new Area : '))
                return self.Area
            if choice_number == 5:
                self.Floor = int(input('please enter new Floor : '))
                return self.Floor
            if choice_number == 6:
                self.Number_classes = int(input('please enter new Number_classes : '))
                return self.Number_classes
            if choice_number == 7:
                self.Address = input('please enter new Address: ')
                return self.Address
            if choice_number == 8:
                self.Phone = int(input('please enter new Phone : '))
                return self.Phone
            if choice_number == 9:
                self.active  = input('please enter new active  : ')
                return self.active
            if choice_number == 10:
                self.inactive = input('please enter new inactive : ')
                return self.inactive
            if choice_number == 11:
                self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                return self.Mortgage_amount
            if choice_number == 12:
                 self.Rent_price = int(input('please enter new Rent_price : '))
                 return self.Rent_price
            if choice_number == 13:
                self.selling_price = int(input('please enter new selling_price : '))
                return self.selling_price
            if choice_number == 14:
                self.onsale = input('please enter new onsale : ')
                return self.onsale
            if choice_number == 15:
                self.Rent = int(input('please enter new Rent : '))
                return self.Rent
            if choice_number == 16:
                return 'exit'

'''E)Home class(show address and Edit address specification'''

class Home(Apartment):
    def __init__(self,Owner,Tenant,Number_rooms,Area,Number_classes,Address,Phone,active,inactive,Mortgage_amount
                 ,Rent_price,selling_price,onsale,Rent,Yard_area):
        super().__init__(Owner,Tenant,Number_rooms,Area,Number_classes,Address,Phone,active,inactive,Mortgage_amount
                         ,Rent_price,selling_price,onsale,Rent)
        self.Yard_area=Yard_area

    def __repr__(self):
        return  str(self.__dict__)


    @classmethod
    def add_Home(cls):
        Owner = input('please enter Owner:')
        Tenant = input('please enter Tenant:')
        Number_rooms = int(input('please enter Number_rooms:'))
        Area = int(input('please enter Area:'))
        Number_classes = int(input('please enter Number_classes:'))
        Address = input('please enter Address:')
        Phone =int(input('please enter Phone:'))
        active = input('please enter active:')
        inactive = input('please enter inactive:')
        Mortgage_amount = int(input('please enter Mortgage_amount:'))
        Rent_price =  int(input('please enter Rent_price :'))
        selling_price =  int(input('please enter selling_price:'))
        onsale =  input('please enter onsale:')
        Rent = int(input('please enter Rent:'))
        Yard_area = int( input('please enter Yard_area:') )
        return cls(Owner=Owner,Tenant=Tenant, Number_rooms=Number_rooms, Area=Area,
                   Number_classes=Number_classes, Address=Address, Phone=Phone,active=active,
                   inactive=inactive,Mortgage_amount=Mortgage_amount,
                   Rent_price=Rent_price,selling_price=selling_price,onsale=onsale,Rent=Rent,
                   Yard_area=Yard_area)


    def edit_Home(self):
        print('**********Get and edit the Home  class**********')
        while True:
            print("""\n 1)Owner \n 2)Tenant \n 3)Number_rooms \n 4)Area \n 5) Number_classes \n 6)Address \n 7)Phone \n              
             8)active \n 9)inactive \n 10)Mortgage_amount \n 11)Rent_price \n 12)selling_price \n 13)onsale \n 14)Rent \n 15)exit""")
            choice_number = int(input(' please enter choice : '))
            if choice_number == 1:
                self.Owner = input('please enter new Owner : ')
                return self.Owner
            if choice_number == 2:
                self.Tenant = input('please enter new Tenant : ')
                return self.Tenant
            if choice_number == 3:
                self.Number_rooms = int(input('please enter new Number_rooms : '))
                return self.Number_rooms
            if choice_number == 4:
                self.Area = int(input('please enter new Area : '))
                return self.Area
            if choice_number == 5:
                self.Number_classes = int(input('please enter new Number_classes : '))
                return self.Number_classes
            if choice_number == 6:
                self.Address = input('please enter new Address: ')
                return self.Address
            if choice_number == 7:
                self.Phone = int(input('please enter new Phone : '))
                return self.Phone
            if choice_number == 8:
                self.active  = input('please enter new active  : ')
                return self.active
            if choice_number == 9 :
                self.inactive = input('please enter new inactive : ')
                return self.inactive
            if choice_number == 10:
                self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                return self.Mortgage_amount
            if choice_number == 11:
                 self.Rent_price = int(input('please enter new Rent_price : '))
                 return self.Rent_price                                                                                                          
            if choice_number == 12:
                self.selling_price = int(input('please enter new selling_price : '))
                return self.selling_price
            if choice_number == 13:
                self.onsale = input('please enter new onsale : ')
                return self.onsale
            if choice_number == 14:
                self.Rent = int(input('please enter new Rent : '))
                return self.Rent
            if choice_number == 15:
                return 'exit'

'''F)Shop class(show address and Edit address specification'''

class Shop(Apartment):
    def __init__(self,Owner,Tenant,Area,Address,Phone,active,inactive,Mortgage_amount
                     ,Rent_price,selling_price,onsale,Rent):
        super().__init__(Owner,Tenant,Area,Address,Phone,active,inactive,Mortgage_amount
                             ,Rent_price,selling_price,onsale,Rent)
    def __repr__(self):
        return  str(self.__dict__)
    @classmethod
    def add_Shop(cls):
        Owner = input('please enter Owner:')
        Tenant = input('please enter Tenant:')
        Area = int(input('please enter Area:'))
        Address = input('please enter Address:')
        Phone = int(input('please enter Phone:'))
        active = input('please enter active:')
        inactive = input('please enter inactive:')
        Mortgage_amount = int(input('please enter Mortgage_amount:'))
        Rent_price = int( input('please enter Rent_price :'))
        selling_price =  int(input('please enter selling_price:'))
        onsale =  input('please enter onsale:')
        Rent = int(input('please enter Rent:'))
        return cls(Owner=Owner,Tenant=Tenant, Area=Area,Address=Address, Phone=Phone,active=active,
                   inactive=inactive,Mortgage_amount=Mortgage_amount,Rent_price=Rent_price,selling_price=selling_price
                   ,onsale=onsale,Rent=Rent)




    def edit_Shop(self):
        print('**********Get and edit the Shop  class**********')
        while True:
            print("""\n 1)Owner \n 2)Tenant \n  3)Area \n 4)Address \n 5)Phone \n 6)active \n 7)inactive \n                      
              8)Mortgage_amount \n 9)Rent_price \n 10)selling_price \n 11)onsale \n 12)Rent \n 13)exit""")
            choice_number = int(input(' please enter choice : '))
            if choice_number == 1:
                self.Owner = input('please enter new Owner : ')
                return self.Owner
            if choice_number == 2:
                self.Tenant = input('please enter new Tenant : ')
                return self.Tenant
            if choice_number == 3:
                self.Area = int(input('please enter new Area : '))
                return self.Area
            if choice_number == 4:
                self.Address = input('please enter new Address: ')
                return self.Address
            if choice_number == 5:
                self.Phone = int(input('please enter new Phone : '))
                return self.Phone
            if choice_number == 6:
                self.active  = input('please enter new active  : ')
                return self.active
            if choice_number == 7 :
                self.inactive = input('please enter new inactive : ')
                return self.inactive
            if choice_number == 8:
                self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                return self.Mortgage_amount
            if choice_number == 9:
                 self.Rent_price = int(input('please enter new Rent_price : '))
                 return self.Rent_price
            if choice_number == 10:
                self.selling_price = int(input('please enter new selling_price : '))
                return self.selling_price
            if choice_number == 11:
                self.onsale = input('please enter new onsale : ')
                return self.onsale
            if choice_number == 12:
                self.Rent = int(input('please enter new Rent : '))
                return self.Rent
            if choice_number == 13:
                return 'exit'
''' 2) Sell / rent and search '''

'''A1)Property Consulting Class:'''
class Property_Consulting:
    pass


'''B1)Transaction class:'''

class Transaction:
    pass



























































































































