from datetime import datetime

class Flight :
    def __init__(self, flight_number: str, departure_time: datetime, arrival_time: datetime):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def get_flight_time(self):
        return (self.arrival_time - self.departure_time).total_seconds() // 60

    def get_flight_number(self):
        return self.flight_number
    
    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, year: int, month: int, day: int, hour: int, minute: int):
        self.departure_time = datetime(year, month, day, hour, minute)
    
    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, year: int, month: int, day: int, hour: int, minute: int):
        self.arrival_time = datetime(year, month, day, hour, minute)

class Itinerary :
    def __init__(self, flights: list):
        self.flights = flights
        self.flights.sort(key = self.departure_sort)

    def departure_sort(self, flight: Flight):
        return flight.get_departure_time()

    def get_total_flight_time(self):
        total_flight_time = 0
        for i in self.flights:
            total_flight_time += i.get_flight_time()
        
        return total_flight_time
    
    def get_total_travel_time(self):
        return (self.flights[len(self.flights)-1].get_departure_time() - 
            self.flights[0].get_departure_time()).total_seconds() // 60


def main():

    flights = []

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))

   

    itinerary = Itinerary(flights)

    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())

main()