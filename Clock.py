
class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, min=0, sec=0):
        self.sec = sec
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        
    def inc_sec(self, sec=1):
        self.sec += sec
        if (self.sec > 59):
            self.sec %= 60
            self.min += 1
            self.inc_min(0)

    def inc_min(self, minu=1):
        self.min += minu
        if self.min > 59:
            self.min %= 60
            self.hour += 1
            self.inc_hour(0)

    def inc_hour(self, hour=1):
        self.hour += hour
        if hour + self.hour > 23:
            self.hour %= 24
            self.day += 1
            self.inc_day(0)
    
    def inc_day(self, day=1):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            leap = 29
        else:
            leap = 28

        self.day += day

        if self.day > leap and self.month == 2:
            self.day %= leap
            self.month += 1
        elif self.day> 30 and self.month in [4,6,9,11]:
            self.day %= 30
            self.month += 1
        elif self.day> 31:
            self.day %= 31
            self.month += 1
        self.inc_month(0)
    

    def inc_month(self, month=1):
        self.month += month
        if month + self.month > 12:
            self.month %= 12
            self.year += 1

    def inc_year(self, year=1):
        self.year += year
    

    def clock_as_string(self):
        return f'{self.day:02d}:{self.month:02d}:{self.year:04d}:{self.hour:02d}:{self.min:02d}:{self.sec:02d}'
    
    def set_clock(self, day: int, month: int, year: int, hour: int, min: int, sec: int):
        self.inc_sec(sec)
        self.inc_min(min)
        self.inc_hour(hour)
        self.inc_day(day)
        self.inc_month(month)
        self.year += year

