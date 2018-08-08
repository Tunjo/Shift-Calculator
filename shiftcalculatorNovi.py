from datetime import datetime, timedelta, time as tm
import random
import json
import time
import sys


class Worker():
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def get_name_surname_id(self):
        get_name = input("Name: ")
        get_surname = input("Surname: ")
        self.name = get_name
        self.surname = get_surname
        numbers_id = random.sample(range(1000, 5000), 1)
        self.id = numbers_id[0]

        user_info = {
            "name": self.name,
            "surname": self.surname,
            "id": self.id,
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
            "total": 0,
            "money": 0,
            "night": 0,
            "weekendnights": 0
        }
        #Change smth

        list_of_dicts.append(user_info)

        user_Code.append(self.id)

        self.save_user_info(self)

    def save_user_info(self):
        with open("workshift.txt", "w+") as fp:
            fp.write(json.dumps(list_of_dicts, indent=2))
        putin = input("If you want to quit(q), \n"
              "for log in(l): ")
        if putin == "q":
            sys.exit()
        elif putin == "l":
            self.if_user_exist(self)



    def if_user_exist(self):
        with open("workshift.txt", "r") as fp:
            file = json.load(fp)
        for f in file:
            list_of_dicts.append(f)

        input_id = input("If you registered, type your ID number or (n): ")

        if input_id == "n":
            self.get_name_surname_id(self)
        else:
            for item in list_of_dicts:
                if input_id == str(item['id']):
                    print(item)
                    print(('Name: {}').format(item["name"]))
                    print(('Surename: {}').format(item["surname"]))
                    print(('Id: {}').format(item["id"]))
                    print(('Earned: {}').format(item["money"]))

                    self.calculator(self)

    def day_night(self, now, start, end):
        if start <= end:
            return start <= now < end
        else:
            return start <= now or now < end

    def calculator(self):

        time_now = datetime.now().time()

        while datetime.now().time() >= time_now:
            try:
                time_s = datetime.now().time()
                time.sleep(1)
                time_stop = datetime.now().time()
                total_work = time_stop.second - time_s.second
                working_sec = total_work
                working_min = working_sec / 60
                working_hrs = working_min / 60
                hrs_total = working_hrs

                for item in list_of_dicts:
                    if datetime.now().weekday() == 0:
                        item["monday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 1:
                        item["tuesday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 2:
                        item["wednesday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 3:
                        item["thursday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 4:
                        item["friday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 5:
                        item["saturday"] += hrs_total
                    else:
                        pass
                    if datetime.now().weekday() == 6:
                        item["sunday"] += hrs_total
                    else:
                        pass

                    item["total"] += hrs_total

                    if self.day_night(self, time_s, tm(21), tm(6)):
                        night_price = 85
                        earn = hrs_total * night_price
                        item["money"] += earn
                        item["night"] += hrs_total

                        if datetime.now().weekday() == 5 or datetime.now().weekday() == 6:
                            night_price_weekends = 105
                            earn1 = night_price_weekends * hrs_total
                            item["money"] += earn1
                            item["weekendnights"] += hrs_total

                    else:
                        day_price = 50
                        earn2 = hrs_total * day_price
                        item["money"] += earn2

            except KeyboardInterrupt:
                self.save_user_info(self)



user_Code = []
list_of_dicts = []

Worker.if_user_exist(Worker)
