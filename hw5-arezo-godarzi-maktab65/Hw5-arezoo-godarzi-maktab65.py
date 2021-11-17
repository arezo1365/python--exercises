import csv
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
        try:
            int(City_name)
            print('City_name can not be integer')
        except ValueError:
            print(City_name)
        Street_name = input('please enter Street_name:')
        try:
            int(Street_name)
            print('Street_name can not be integer')
        except ValueError:
            print(Street_name)
        try:
            Number_plates = int(input('please enter Number_plates2:'))
        except ValueError:
            print('Number can not be string')
        else:
            print(Number_plates)
        try:
            Postal_code = int(input('please enter  Postal_code2:'))
        except ValueError:
            print('Number can not be string')
        else:
            print(Postal_code)
            return cls(City_name=City_name, Street_name=Street_name, Number_plates=Number_plates, Postal_code=Postal_code)

    print('**********Get and edit the address class**********')
    def edit_address(self):
        while True:
            try:
                print("""\n 1)City_name \n 2)Street_name \n 3)Number_plates \n 4)postal_code \n 5) exit""")
                choice_number= int(input(' please enter choice : '))
                if choice_number == 1:

                    self.City_name = input('please enter new city_name : ')
                    try:
                        int(self.City_name)
                        print('self.City_name can not be integer')
                    except ValueError:
                        print(self.City_name)
                        return self.City_name
                if choice_number == 2:
                    self.Street_name = input('please enter new Street_name : ')
                    try:
                        int(self.Street_name)
                        print('self.Street_name can not be integer')
                    except ValueError:
                        print(self.Street_name)
                        return self.Street_name
                if choice_number== 3:
                    try:
                        self.Number_plates = int(input('please enter new Number_plates : '))
                    except ValueError:
                        print('self.Number_plates can not be string')
                    else:
                        print(self.Number_plates)
                        return self.Number_plates
                if choice_number == 4:
                    try:
                        self.Postal_code = int(input('please enter new Postal_code : '))
                    except ValueError:
                        print('self.Postal_code  can not be string')
                    else:
                        print(self.Postal_code )
                        return self.Postal_code
                if choice_number == 5:
                    return 'exit'
            except ValueError:
                print('please enter int')


    def edit_info(self, **kwargs):
            self.__dict__.update((k, v) for k, v in kwargs.items())
            return self


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
        try:
            int(first_name)
            print('first_name can not be integer')
        except ValueError:
            print(first_name)

        last_name=input('please enter  last_name:')
        try:
            int(last_name)
            print('first_name can not be integer')
        except ValueError:
            print(last_name)

        try:
            National_Code = int(input('please enter  National_Code:'))
        except ValueError:
            print('National_Code can not be string')
        else:
            print(National_Code)

        try:
            phone_number = int(input('please enter  phone_number:'))
        except ValueError:
            print('phone_number can not be string')
        else:
            print(phone_number)


            return cls(first_name=first_name,last_name=last_name,National_Code=National_Code,phone_number=phone_number)


    def edit_person(self):
        print('**********Get and edit the person class**********')
        while True:
            try:
                print("""\n 1)first_name \n 2)last_name \n 3)National_Code \n 4)phone_number \n 5) exit""")
                choice_number= int(input(' please enter choice : '))
                if choice_number == 1:
                    self.first_name = input('please enter new first_name : ')
                    try:
                        int(first_name)
                        print('first_name can not be integer')
                    except ValueError:
                        print(first_name)
                        return self.first_name
                if choice_number == 2:
                    self.last_name = input('please enter new last_name : ')
                    try:
                        int(last_name)
                        print('last_name can not be integer')
                    except ValueError:
                        print(last_name)
                        return self.last_name
                if choice_number== 3:
                    try:
                        self.National_Code = int(input('please enter new National_Code : '))
                    except ValueError:
                        print('National_Code can not be string')
                    else:
                        print(National_Code)
                        return self.National_Code
                if choice_number == 4:
                    try:
                        self.phone_number = int(input('please enter new phone_number : '))
                    except ValueError:
                        print('phone_number can not be string')
                    else:
                        print(phone_number)
                        return self.phone_number
                if choice_number == 5:
                    return 'exit '
            except ValueError:
                print('please enter int')
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
       try:
           int(Owner)
           print('Owner can not be integer')
       except ValueError:
           print(Owner)

       Tenant=input('please enter Tenant:')
       try:
           int(Tenant)
           print('Tenant can not be integer')
       except ValueError:
           print(Tenant)
       try:
            Number_rooms=int(input('please enter Number_rooms:'))
       except ValueError:
            print('Number_rooms can not be string')
       else:
            print(Number_rooms)
       try:
            Area=int(input('please enter Area:'))
       except ValueError:
            print('Area can not be string')
       else:
            print(Area)
       try:
            Floor=int(input('please enter Floor:'))
       except ValueError:
            print('Floor can not be string')
       else:
            print(Floor)
       try:
            Number_classes=int(input('please enter Number_classes:'))
       except ValueError:
            print('Number_classes can not be string')
       else:
            print(Number_classes)

       Address=input('please enter Address:')
       try:
           int(Address)
           print('Address can not be integer')
       except ValueError:
           print(Address)
       try:
            Phone=int(input('please enter Phone:'))
       except ValueError:
            print('Phone can not be string')
       else:
            print(Phone)
       active=input('please enter active:')
       try:
           int(active)
           print('active can not be integer')
       except ValueError:
           print(active)

       inactive=input('please enter inactive:')
       try:
           int(inactive)
           print('inactive can not be integer')
       except ValueError:
           print(inactive)
       try:
            Mortgage_amount=int(input('please enter Mortgage_amount:'))
       except ValueError:
            print('Mortgage_amount can not be string')
       else:
            print(Mortgage_amount)
       try:
            Rent_price=int(input('please enter Rent_price:'))
       except ValueError:
            print('Rent_price can not be string')
       else:
            print(Rent_price)
       try:
            selling_price=int(input('please enter selling_price:'))
       except ValueError:
            print('selling_price can not be string')
       else:
            print(selling_price)

       onsale=input('please enter onsale:')
       try:
           int(onsale)
           print('onsale can not be integer')
       except ValueError:
           print(onsale)
       try:
           Rent=int(input('please enter Rent:'))
       except ValueError:
            print('Rent can not be string')
       else:
            print(Rent)

            return cls(Owner=Owner,Tenant=Tenant,Number_rooms=Number_rooms,Area=Area,Floor=Floor,
                   Number_classes=Number_classes,Address=Address,Phone=Phone,active=active,inactive=inactive,
                   Mortgage_amount=Mortgage_amount,Rent_price=Rent_price,selling_price=selling_price,onsale=onsale,Rent=Rent)
    def edit_apartment(self):
        print('**********Get and edit the apartment  class**********')
        while True:
            try:
                print("""\n 1)Owner \n 2)Tenant \n 3)Number_rooms \n 4)Area \n 5) Floor \n 6) Number_classes \n 7)Address \n 8)Phone \n
                 9)active \n 10)inactive \n 11)Mortgage_amount \n 12)Rent_price \n 13)selling_price \n 14)onsale \n 15)Rent \n 16)exit""")
                choice_number = int(input(' please enter choice : '))
                if choice_number == 1:
                    self.Owner = input('please enter new Owner : ')
                    try:
                        int(self.Owner)
                        print('self.Owner can not be integer')
                    except ValueError:
                        print(self.Owner)
                        return self.Owner
                if choice_number == 2:
                    self.Tenant = input('please enter new Tenant : ')
                    try:
                        int(self.Tenant)
                        print('self.Tenant can not be integer')
                    except ValueError:
                        print(self.Tenant)
                        return self.Tenant
                if choice_number == 3:
                    try:
                        self.Number_rooms = int(input('please enter new Number_rooms : '))
                    except ValueError:
                        print('self.Number_rooms can not be string')
                    else:
                        print(self.Number_rooms)
                        return self.Number_rooms
                if choice_number == 4:
                    try:
                        self.Area = int(input('please enter new Area : '))
                    except ValueError:
                        print('self.Area  can not be string')
                    else:
                        print(self.Area )
                        return self.Area
                if choice_number == 5:
                    try:
                        self.Floor = int(input('please enter new Floor : '))
                    except ValueError:
                        print('self.Floor  can not be string')
                    else:
                        print(self.Floor )
                        return self.Floor
                if choice_number == 6:
                    try:
                        self.Number_classes = int(input('please enter new Number_classes : '))
                    except ValueError:
                        print('self.Number_classes  can not be string')
                    else:
                        print(self.Number_classes )
                        return self.Number_classes
                if choice_number == 7:
                        self.Address = input('please enter new Address: ')
                        try:
                            int(self.Address)
                            print('self.Address can not be integer')
                        except ValueError:
                            print(self.Address)
                            return self.Address
                if choice_number == 8:
                    try:
                        self.Phone = int(input('please enter new Phone : '))
                    except ValueError:
                        print('self.Phone  can not be string')
                    else:
                        print(self.Phone )
                        return self.Phone
                if choice_number == 9:
                    self.active  = input('please enter new active  : ')
                    try:
                        int(self.active)
                        print('self.active can not be integer')
                    except ValueError:
                        print(self.active)
                        return self.active
                if choice_number == 10:
                    self.inactive = input('please enter new inactive : ')
                    try:
                        int(self.inactive)
                        print('self.inactive can not be integer')
                    except ValueError:
                        print(self.inactive)
                        return self.inactive
                if choice_number == 11:
                    try:
                        self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                    except ValueError:
                        print('self.Mortgage_amount  can not be string')
                    else:
                        print(self.Mortgage_amount )
                        return self.Mortgage_amount
                if choice_number == 12:
                    try:
                        self.Rent_price = int(input('please enter new Rent_price : '))
                    except ValueError:
                        print('self.Rent_price  can not be string')
                    else:
                        print(self.Rent_price )
                        return self.Rent_price
                if choice_number == 13:
                    try:
                        self.selling_price = int(input('please enter new selling_price : '))
                    except ValueError:
                        print('self.selling_price  can not be string')
                    else:
                        print(self.selling_price )
                        return self.selling_price
                if choice_number == 14:
                    self.onsale = input('please enter new onsale : ')
                    try:
                        int(self.onsale)
                        print('self.onsale can not be integer')
                    except ValueError:
                        print(self.onsale)
                        return self.onsale
                if choice_number == 15:
                    try:
                        self.Rent = int(input('please enter new Rent : '))
                    except ValueError:
                        print('self.Rent  can not be string')
                    else:
                        print(self.Rent )
                    return self.Rent
                if choice_number == 16:
                    return 'exit'
            except ValueError:
            print('please enter int')

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
        try:
            int(Owner)
            print('Owner can not be integer')
        except ValueError:
            print(Owner)
        Tenant = input('please enter Tenant:')
        try:
            int(Tenant)
            print('Tenant can not be integer')
        except ValueError:
            print(Tenant)
        try:
            Number_rooms = int(input('please enter Number_rooms:'))
        except ValueError:
            print('Number_rooms can not be string')
        else:
            print(Number_rooms)
        try:
            Area = int(input('please enter Area:'))
        except ValueError:
            print('Area can not be string')
        else:
            print(Area)
        try:
            Number_classes = int(input('please enter Number_classes:'))
        except ValueError:
            print('Number_classes can not be string')
        else:
            print(Number_classes)
        Address = input('please enter Address:')
        try:
            int(Address)
            print('Address can not be integer')
        except ValueError:
            print(Address)
        try:
            Phone =int(input('please enter Phone:'))
        except ValueError:
            print('Phone can not be string')
        else:
            print(Phone)
        active = input('please enter active:')
        try:
            int(active)
            print('active can not be integer')
        except ValueError:
            print(active)
        inactive = input('please enter inactive:')
        try:
            int(inactive)
            print('inactive can not be integer')
        except ValueError:
            print(inactive)
        try:
            Mortgage_amount = int(input('please enter Mortgage_amount:'))
        except ValueError:
            print('Mortgage_amount can not be string')
        else:
            print(Mortgage_amount)
        try:
            Rent_price =  int(input('please enter Rent_price :'))
        except ValueError:
            print('Rent_price can not be string')
        else:
            print(Rent_price)
        try:
            selling_price =  int(input('please enter selling_price:'))
        except ValueError:
            print('selling_price can not be string')
        else:
            print(selling_price)
        onsale =  input('please enter onsale:')
        try:
            int(onsale)
            print('onsale can not be integer')
        except ValueError:
            print(onsale)
        try:
            Rent = int(input('please enter Rent:'))
        except ValueError:
            print('Rent can not be string')
        else:
            print(Rent)
        try:
            Yard_area = int( input('please enter Yard_area:') )
        except ValueError:
            print('Yard_area can not be string')
        else:
            print(Yard_area)

            return cls(Owner=Owner,Tenant=Tenant, Number_rooms=Number_rooms, Area=Area,
                   Number_classes=Number_classes, Address=Address, Phone=Phone,active=active,
                   inactive=inactive,Mortgage_amount=Mortgage_amount,
                   Rent_price=Rent_price,selling_price=selling_price,onsale=onsale,Rent=Rent,
                   Yard_area=Yard_area)


    def edit_Home(self):
        print('**********Get and edit the Home  class**********')
        while True:
            try:
                print("""\n 1)Owner \n 2)Tenant \n 3)Number_rooms \n 4)Area \n 5) Number_classes \n 6)Address \n 7)Phone \n
                 8)active \n 9)inactive \n 10)Mortgage_amount \n 11)Rent_price \n 12)selling_price \n 13)onsale \n 14)Rent \n 15)exit""")
                choice_number = int(input(' please enter choice : '))
                if choice_number == 1:
                    self.Owner = input('please enter new Owner : ')
                    try:
                        int(Owner)
                        print('Owner can not be integer')
                    except ValueError:
                        print(Owner)
                        return self.Owner
                if choice_number == 2:
                    self.Tenant = input('please enter new Tenant : ')
                    try:
                        int(Tenant)
                        print('Tenant can not be integer')
                    except ValueError:
                        print(Tenant)
                        return self.Tenant
                if choice_number == 3:
                    try:
                        self.Number_rooms = int(input('please enter new Number_rooms : '))
                    except ValueError:
                        print('Number_rooms  can not be string')
                    else:
                        print(Number_rooms )
                        return self.Number_rooms
                if choice_number == 4:
                    try:
                        self.Area = int(input('please enter new Area : '))
                    except ValueError:
                        print('Area  can not be string')
                    else:
                        print(Area )
                        return self.Area
                if choice_number == 5:
                    try:
                        self.Number_classes = int(input('please enter new Number_classes : '))
                    except ValueError:
                        print('Number_classes can not be string')
                    else:
                        print(Number_classes )
                        return self.Number_classes
                if choice_number == 6:
                    self.Address = input('please enter new Address: ')
                    try:
                        int(Address)
                        print('Address can not be integer')
                    except ValueError:
                        print(Address)
                        return self.Address
                if choice_number == 7:
                    try:
                        self.Phone = int(input('please enter new Phone : '))
                    except ValueError:
                        print('Phone  can not be string')
                    else:
                        print(Phone  )
                        return self.Phone
                if choice_number == 8:
                    self.active  = input('please enter new active  : ')
                    try:
                        int(active)
                        print('active can not be integer')
                    except ValueError:
                        print(active)
                        return self.active
                if choice_number == 9 :
                    self.inactive = input('please enter new inactive : ')
                    try:
                        int(inactive)
                        print('inactive can not be integer')
                    except ValueError:
                        print(inactive)
                        return self.inactive
                if choice_number == 10:
                    try:
                        self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                    except ValueError:
                        print('Mortgage_amount  can not be string')
                    else:
                        print(Mortgage_amount  )
                        return self.Mortgage_amount
                if choice_number == 11:
                    try:
                        self.Rent_price = int(input('please enter new Rent_price : '))
                    except ValueError:
                        print('Rent_price  can not be string')
                    else:
                        print(Rent_price)
                        return self.Rent_price
                if choice_number == 12:
                    try:
                        self.selling_price = int(input('please enter new selling_price : '))
                    except ValueError:
                        print('selling_price  can not be string')
                    else:
                        print(selling_price)
                        return self.selling_price
                if choice_number == 13:
                    self.onsale = input('please enter new onsale : ')
                    try:
                        int(onsale)
                        print('onsale can not be integer')
                    except ValueError:
                        print(onsale)
                        return self.onsale
                if choice_number == 14:
                    try:
                        self.Rent = int(input('please enter new Rent : '))
                    except ValueError:
                        print('Rent  can not be string')
                    else:
                        print(Rent)
                        return self.Rent
                if choice_number == 15:
                    return 'exit'
            except ValueError:
                print('please enter int')

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
        try:
            int(Owner)
            print('Owner can not be integer')
        except ValueError:
            print(Owner)
        Tenant = input('please enter Tenant:')
        try:
            int(Tenant)
            print('Tenant can not be integer')
        except ValueError:
            print(Tenant)
        try:
            Area = int(input('please enter Area:'))
        except ValueError:
            print('Area can not be string')
        else:
            print(Area)
        Address = input('please enter Address:')
        try:
            int(Address)
            print('Address can not be integer')
        except ValueError:
            print(Address)
        try:
            Phone = int(input('please enter Phone:'))
        except ValueError:
            print('Phone can not be string')
        else:
            print(Phone)
        active = input('please enter active:')
        try:
            int(active)
            print('active can not be integer')
        except ValueError:
            print(active)
        inactive = input('please enter inactive:')
        try:
            int(inactive)
            print('inactive can not be integer')
        except ValueError:
            print(inactive)
        try:
            Mortgage_amount = int(input('please enter Mortgage_amount:'))
        except ValueError:
            print('Mortgage_amount can not be string')
        else:
            print(Mortgage_amount)
        try:
            Rent_price = int( input('please enter Rent_price :'))
        except ValueError:
            print('Rent_price can not be string')
        else:
            print(Rent_price)

        try:
            selling_price =  int(input('please enter selling_price:'))
        except ValueError:
            print('selling_price can not be string')
        else:
            print(selling_price)
        onsale =  input('please enter onsale:')
        try:
            int(onsale)
            print('onsale can not be integer')
        except ValueError:
            print(onsale)
        try:
            Rent = int(input('please enter Rent:'))
        except ValueError:
            print('Rent can not be string')
        else:
            print(Rent)
            return cls(Owner=Owner,Tenant=Tenant, Area=Area,Address=Address, Phone=Phone,active=active,
                   inactive=inactive,Mortgage_amount=Mortgage_amount,Rent_price=Rent_price,selling_price=selling_price
                   ,onsale=onsale,Rent=Rent)




    def edit_Shop(self):
        print('**********Get and edit the Shop  class**********')
        while True:
            try:
                print("""\n 1)Owner \n 2)Tenant \n  3)Area \n 4)Address \n 5)Phone \n 6)active \n 7)inactive \n
                  8)Mortgage_amount \n 9)Rent_price \n 10)selling_price \n 11)onsale \n 12)Rent \n 13)exit""")
                choice_number = int(input(' please enter choice : '))
                if choice_number == 1:
                    self.Owner = input('please enter new Owner : ')
                    try:
                        int(Owner)
                        print('Owner can not be integer')
                    except ValueError:
                        print(Owner)
                        return self.Owner
                if choice_number == 2:
                    self.Tenant = input('please enter new Tenant : ')
                    try:
                        int(Tenant)
                        print('Tenant can not be integer')
                    except ValueError:
                        print(Tenant)
                        return self.Tenant
                if choice_number == 3:
                    try:
                        self.Area = int(input('please enter new Area : '))
                    except ValueError:
                        print('Area  can not be string')
                    else:
                        print(Area)
                        return self.Area
                if choice_number == 4:
                    self.Address = input('please enter new Address: ')
                    try:
                        int(Address)
                        print('Address can not be integer')
                    except ValueError:
                        print(Address)
                        return self.Address
                if choice_number == 5:
                    try:
                        self.Phone = int(input('please enter new Phone : '))
                    except ValueError:
                        print('Phone  can not be string')
                    else:
                        print(Phone)
                        return self.Phone
                if choice_number == 6:
                    self.active  = input('please enter new active  : ')
                    try:
                        int(active)
                        print('active can not be integer')
                    except ValueError:
                        print(active)
                        return self.active
                if choice_number == 7 :
                    self.inactive = input('please enter new inactive : ')
                    try:
                        int(inactive)
                        print('inactive can not be integer')
                    except ValueError:
                        print(inactive)
                        return self.inactive
                if choice_number == 8:
                    try:
                        self.Mortgage_amount = int(input('please enter new Mortgage_amount : '))
                    except ValueError:
                        print('Mortgage_amount  can not be string')
                    else:
                        print(Mortgage_amount)
                        return self.Mortgage_amount
                if choice_number == 9:
                    try:
                        self.Rent_price = int(input('please enter new Rent_price : '))
                    except ValueError:
                        print('Rent_price  can not be string')
                    else:
                        print(Rent_price)
                        return self.Rent_price
                if choice_number == 10:
                    try:
                        self.selling_price = int(input('please enter new selling_price : '))
                    except ValueError:
                        print('selling_price  can not be string')
                    else:
                        print(selling_price)
                        return self.selling_price
                if choice_number == 11:
                    self.onsale = input('please enter new onsale : ')
                    try:
                        int(onsale)
                        print('onsale can not be integer')
                    except ValueError:
                        print(onsale)
                        return self.onsale
                if choice_number == 12:
                    try:
                        self.Rent = int(input('please enter new Rent : '))
                    except ValueError:
                        print('Rent  can not be string')
                    else:
                        print(Rent)
                        return self.Rent
                if choice_number == 13:
                    return 'exit'
            except ValueError:
                print('please enter int')

    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self
''' 2) Sell / rent and search '''

'''A1)Property Consulting Class:'''
class Property_Consulting:
    pass


'''B1)Transaction class:'''

class Transaction:
    pass

# a=Address('tehran','afrariyeh','85','12345')
# print(a.__dict__)
# dict={'City_name':'fy','Street_name':'jjjj','Number_plates':'1254','Postal_code':'55000'}
# a.edit_info(**dict)
# print(a.__dict__)



Address.add_address()

person.add_person()
Apartment.add_apartment()
Home.add_Home()
Shop.add_Shop()


list=[]
with open('new.csv','r') as file:
    myfile=csv.reader(file)
    for row in myfile:
        list.append(row)
editrow = int(input('\which row would you like tochange?enter 1-' + str(len(list) - 1) + ':'))

for i in range(len(list[0])):

        new_details=input('enter new data for'+str(list[1][i]+':'))
        list[editrow][i]=new_details
print(list)








































































