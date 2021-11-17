class Activity:
    """
        distance:
        duration:
        calories: based on activity level
        """

    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration
        self.count_cal = 0
        self.final_cal = 0

    @classmethod
    def add_data(cls):
        distance = int(input("enter your distance(km):"))
        duration = int(input("enter your duration (min):"))
        return cls(distance, duration)

    def calculate_cal(self):
        self.final_cal = self.count_cal * self.distance
        return self.final_cal
    
    def __repr__(self):
        return f" duration : {self.duration} , distance : {self.distance}"

class Run(Activity):
    """
    pace: (minute/kilometer)
    pace > 8:   (100 cal for each kilometer)
    5 < pace < 8: (150 cal for each kilometer)
    pace < 5:   (200 cal for each kilometer)

    """

    def __init__(self, distance, duration):
        super().__init__(distance, duration)
        self.pace = 0

    def pace(self):
        self.pace = self.duration / self.distance

        return self.pace

    def count_calory(self):
        if self.pace > 8:
            self.count_cal = 100
        elif 5 < self.pace < 8:
            self.count_cal = 150
        elif self.pace < 5:
            self.count_cal = 200
        return self.count_cal


class Ride(Activity):
    """
    speed: (kilometer/hour)
    speed < 15:     (80 cal for each kilometer)
    25 < speed < 15 (120 cal for each kilometer)
    speed > 25:     (180 cal for each kilometer)

    """

    def __init__(self, distance, duration):
        super().__init__(distance, duration)
        self.speed = 0

    def speed(self):
        self.speed = self.distance / self.duration
        return self.speed

    def count_calory(self):
        if self.speed < 15:
            self.count_cal = 80
        elif 25 < self.speed < 15:
            self.count_cal = 120
        elif self.speed > 25:
            self.count_cal = 180
        return self.count_cal


# class Swim(Activity):
#     """
#     pace:
#     """
#     pass

class Athlete:
    """
    first_name
    last_name
    add_activity
    view_log ( of all activities)
    """
    counter = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(Athlete.counter) + self.first_name
        self.activity = {}
        Athlete.counter += 1

    @classmethod
    def add_info(cls):
        first_name = input("enter your fist name:")
        last_name = input("enter your last name:")
        return cls(first_name, last_name)

    def __repr__(self):
        return f"first name:{self.first_name} ,last name;{self.last_name},id:{self.id}"


Menu = """
 register a person
 add activity
 view log of a athlete
 sort athletes (number of activites, calories burnt)
"""
user_list = []
while True:
    print("1:register a person ", "\n", "2:add activity", "\n",
          "3:view log of an athlete\n", "4:sort athletes (number of activites, calories burnt\n", "5:break")
    k = int(input("enter your number:"))
    if k == 1:
        x = Athlete.add_info()
        user_list.append(x)  
        print(x.id)  
        print(user_list)
    if k== 2:
        y=input('enetr your id ')
        for i in user_list:
            if y==i.id:
                print('1) Run', '\n', '2)Ride')
                kk=int(input('your key : '))
                if kk==1:
                    i.activity['Run']=Run.add_data()
                    print(i.activity)
    if k==3:
        break