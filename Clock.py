

class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, min=0, sec=0):
        self.sec = sec
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        
    def inc_sec(self, sec):
        if (sec > 59):
            self.min += 1
            self.sec = sec % 60
        else:
            self.sec = sec

    def inc_min(self, minu):
        print(minu+self.min)
        if (minu + self.min) > 59:
            self.hour += 1
            self.min = (minu+self.min) % 60
            print("if")
        else:
            self.min += minu

    def inc_hour(self, hour):
        if hour + self.hour > 23:
            self.day += 1
            self.hour = (hour+self.hour) % 24
        else:
            self.hour += hour
    
    def inc_day(self, day):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            leap = 29
        else:
            leap = 28
        if day + self.day > leap and self.month == 2:
            self.month += 1
            self.day = (self.day+day) % 28
        elif day + self.day> 30 and self.month in [4,6,9,11]:
            self.month += 1
            self.day = (self.day+day) % 30
        elif day + self.day> 31:
            self.month += 1
            self.day = (self.day+day) % 31
        else:
            self.day += day
    

    def inc_month(self, month):
        if month + self.month > 12:
            self.year += 1
            self.month = (self.month+month) % 12
        else:
            self.month += month
    

    def clock_as_string(self):
        return f'{self.day:02d}:{self.month:02d}:{self.year:02d}:{self.hour:02d}:{self.min:02d}:{self.sec:02d}'
    
    def set_clock(self, day: int, month: int, year: int, hour: int, min: int, sec: int):
        self.inc_sec(sec)
        self.inc_min(min)
        self.inc_hour(hour)
        self.inc_day(day)
        self.inc_month(month)
        self.year += year

clock = Clock()
clock.set_clock(31,12,2013,23,59,60)

print(clock.clock_as_string())

"""
def main():



if __name__ == '__main__':
    main()"""
