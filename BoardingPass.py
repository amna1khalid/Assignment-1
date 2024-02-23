#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import Enum
from datetime import date, datetime



class Person: #Define a normal person class
    def __init__(self, first_name, last_name, age): #use a constructor to initialize an object attributes
        self.first_name = first_name #attributes like first and last name and also age
        self.last_name = last_name
        self.age = age
        

        """
        Define a getter and setter methods for the class's attributes
        While making sure to transfer the user input fo rthe attribute to the correct data type
        For example the age would be an integer so use int() encase

        """

    def get_first_name(self): #return the user first name
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = str(first_name) #first name as a string

    def get_last_name(self): #return the user last name
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = str(last_name) #last name as a string

    def get_age(self): #return the user age
        return self.age

    def set_age(self, age):
        self.age = int(age) #age as an integer


        """ Define a Passenger class with attributes Inherented from the Person class
        establishing "is-a" relationship , as Passenger "is-a"Person

        The Passnger class inherents the first_name , last_name, and age attributes with all
        of the setter and getter fuctions

        While also having another attribute of passport number since people need their passport
        to generate a boarding pass
        """

class Passenger(Person): #takes Person Class as a parent class
    def __init__(self, first_name, last_name, age, passport_number):
        super().__init__(first_name, last_name, age) #use super().__init__ to inherent attributes from the parent class
        self.passport_number = passport_number

        "define an authentication function to make sure user age and passport are valid"

    def authenticate_passenger(self):
        return self.get_age() >= 18 and len(self.passport_number) in [8, 9]
    #users should be 18=+ and have a reliable passport number length to get an electronic boarding pass
    #return True to authenticate these users


        "Setter and getter methods to set and get the passport number"

    def get_passport_number(self):
        return self.passport_number

    def set_passport_number(self, passport_number):
        self.passport_number = str(passport_number)


        """Define a Flight Class with attributes like
        flight number , departure location, destination, date of the flight, and time of the flight"""

class Flight:
    def __init__(self, flight_number, departure, destination, date, time): #initilize attributes
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.date = date
        self.time = time

        """Setter and getter functions for the Flight Class"""
    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_departure(self):
        return self.departure

    def set_departure(self, departure):
        self.departure = departure

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time


        """
        Enum classes for the Seat Class

        1-Define a enumeration seat status class for the Seat Class with two contants
        either a seat can be available or booked

        2-Define a enumerration Seat Class type with 3 contents(economy, business, first) """

class SeatStatus(Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"

class SeatClass(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST = "First"


    """
    Define Seat Class with attributes since a flight has different seats a passenger would occupy

    Therefore it has an association relationship with both Passeneger and Flight Class
    A Seat Class attributes are seat number , seat class,and seat status.
    """

class Seat:
    def __init__(self, seat_number, seat_class): #constructor to inilize a seat object attributes
        self.seat_number = seat_number #data type of string as it can be in the form of "01B"
        self.seat_class = SeatClass.ECONOMY #Enum
        self.status = SeatStatus.AVAILABLE #Enum

        "Setter and Getter Functions for the seat attribute"
    def get_seat_number(self):
        return self.seat_number

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number


    def get_seat_class(self):
        return self.seat_class

    def set_seat_class(self, seat_class):
        self.seat_class = seat_class

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status



        """At this point I identified the person,passenger,flight,and seat class
        next I would use these classes to track a passenger reservation and booking to generate a boarding pass"""



        """Enum classes for the Reservation Class

        Define a enumeration reservation status class with two contents either pending or confirmed
        """

class ReservationStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"


    """
    Define Reservation Class to confirm passenger's flight and seat booking
    The class would have attributes like reservation ID (ticket id) ,
    passeneger object, flight object, seat object, and the reservtaion status
    """
class Reservation:
    def __init__(self, reservation_id, passenger, flight, seat, status=ReservationStatus.PENDING):
        self.reservation_id = reservation_id
        self.passenger = passenger #object of Passenger Class
        self.flight = flight #object of Flight Class
        self.seat = seat #object of Seat Class
        self.status =status

        """Setter and Getter methods for reservation attributes"""
    def get_reservation_id(self):
        return self.reservation_id

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def get_passenger(self):
        return self.passenger

    def set_passenger(self, passenger):
        self.passenger = passenger

    def get_flight(self):
        return self.flight

    def set_flight(self, flight):
        self.flight = flight

    def get_seat(self):
        return self.seat

    def set_seat(self, seat):
        self.seat = seat

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

        """Define a Reservation Manager Class that can confirm the Reservation
        This class have only one method since it can only confirm the reservtaion status
        while not having any attriutes that are needed for this system"""

class ReservationManager:
    def confirm_reservation(self, reservation): #define method that would take reservation object
        reservation.set_status(ReservationStatus.CONFIRMED)



        """Define a Ticket Class to create an ticket when the reservation is confirmed"""
class Ticket:
    def __init__(self, passenger, seat, ticket_number, flight): #take passenger, seat, and flight objects and also ticket number
        self.passenger = passenger
        self.seat = seat
        self.ticket_number = ticket_number
        self.flight = flight


        """getter and setter methonds to update/set and get the attributes of the Ticket class"""

    def get_passenger(self):
        return self.passenger

    def set_passenger(self, passenger):
        self.passenger = passenger

    def get_seat(self):
        return self.seat

    def set_seat(self, seat):
        self.seat = seat

    def get_ticket_number(self):
        return self.ticket_number

    def set_ticket_number(self, ticket_number):
        self.ticket_number = ticket_number

    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number


        """Define a Ticket Manager Class that can create a ticket object when reservation statues is confirmed
        This class have only one method since its only purpose is to create the ticket object
        while not having any attributes as they wont be used for this system"""


class TicketManager:
    def generate_ticket(self, reservation): #define a method to generate ticket
        if reservation.get_status() == ReservationStatus.CONFIRMED: #checks and return true if reservation is confirmed
            passenger = reservation.get_passenger() #define passenger from the reservation class object
            seat = reservation.get_seat() #define seat from the reservation class object
            flight = reservation.get_flight() #define fliht from the reservation class object
            ticket_number = f"T{reservation.get_reservation_id()}" #define Ticket ID from the reservation ID from reservation class object
            departure_city = reservation.flight.get_departure() #define departure city from reservation class object
            destination_city = reservation.flight.get_destination() #define destination city from reservation class object


            reservation.seat.set_status(SeatStatus.BOOKED) # change seat status to booked
            return Ticket(passenger, seat, ticket_number, flight) #return the created Ticket Object
        else:
            raise ValueError("Reservation is not confirmed.") #if reservation is not confirmed raise error



            """
            Define Boarding Pass Class that will display the boarding pass if passenegr is authenticated

            This class takes airline name, ticket object, departure date , departure time, arrival time,
            gate, boarding dealine time, terminal number , electronic ticket number
            """


class BoardingPass:
    def __init__(self, airline_name, ticket, date, departure_time, arrival_time, gate, boarding_deadline,
                 terminal, electronic_ticket):
        # Initialize instance variables with the provided parameters
        self.airline_name = airline_name
        self.ticket = ticket
        self.date = date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate
        self.boarding_deadline = boarding_deadline
        self.terminal = terminal
        self.electronic_ticket = electronic_ticket

    def display_boarding_pass(self):
        # Check if the passenger associated with the ticket is authenticated
        if self.ticket.passenger.authenticate_passenger():
            # Display boarding pass information
            print(f"{self.get_airline_name()}") #print airline name
            print(f"{self.ticket.seat.get_seat_class().value} Class")

            """self.ticket.seat.get_seat_class().value
            this help us print the seat class value using .value since its an enum data type
            this long line of code, direct the code to where it gets the data
            see the flow first it goes to the ticket object then the seat of the ticket object
            and use the getter method to get the seat class value"""


            print(f"Passenger Name: {self.ticket.passenger.get_first_name()} {self.ticket.passenger.get_last_name()}") #combine first and last name to get full name
            print(f"From: {self.ticket.flight.get_departure()} ,To: {self.ticket.flight.get_destination()}") #print from where the flight will departure and arrive
            print(f"Flight: {self.ticket.flight.get_flight_number()}") #print flight number throughthe ticket class object
            print(f"Date: {self.get_date()}") # get date of departure
            print(f"Time: {self.get_departure_time()} ,Arrival Time: {self.get_arrival_time()}") # time of departure and arrival
            print(f"Gate: {self.get_gate()} ,Boarding Till: {self.get_boarding_deadline()}") #gate number and boarding time deadline
            print(f"Seat: {self.ticket.seat.get_seat_number()} ,Terminal: {self.get_terminal()}") #seat number and terminal number
            print(f"Electronic Ticket: {self.get_electronic_ticket()}") #ticket number
        else:
            # Raise an error if authentication fails
            raise ValueError("Unsuccessful Authentication") #if passenger is not authenticated raise error


            """Getter and setter methods for the boarding pass attributes"""
    def get_airline_name(self):
        return self.airline_name

    def set_airline_name(self, airline_name):
        self.airline_name = airline_name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_gate(self):
        return self.gate

    def set_gate(self, gate):
        self.gate = gate

    def get_boarding_deadline(self):
        return self.boarding_deadline

    def set_boarding_deadline(self, boarding_deadline):
        self.boarding_deadline = boarding_deadline

    def get_terminal(self):
        return self.terminal

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_electronic_ticket(self):
        return self.electronic_ticket

    def set_electronic_ticket(self, electronic_ticket):
        self.electronic_ticket = electronic_ticket

    def generate_barcode(self):
        pass  #For future use to generate and return the barcode for the boarding pass used in security check.

    def validate_boarding_pass(self):
        pass  # Placed for future code writing that will  validate checks to ensure the boarding pass is valid for boarding.

# Test Cases:


# In[2]:


# Test Case 1: Successful Reservation and Boarding Pass Generation
passenger1 = Passenger("Amna", "Khalid", 25, "C1233456")
flight1 = Flight("F789", "Dubai", "Abu-Dhabi", date(2024, 4, 15), datetime(2024, 4, 15, 11, 30))
seat1 = Seat("10B", SeatClass.FIRST)
reservation1 = Reservation("R001", passenger1, flight1, seat1)
ReservationManager().confirm_reservation(reservation1)

ticket1 = TicketManager().generate_ticket(reservation1)

boarding_pass1 = BoardingPass("Airline A", ticket1, date(2024, 4, 15),datetime(2024, 4, 15, 11, 30), datetime(2024, 4, 15, 12, 0), "Gate 3", datetime(2024, 4, 15, 11, 0), "Terminal 2", "ET987654")
boarding_pass1.display_boarding_pass()


# In[3]:


# Test Case 2: UnSuccessful Authentication because of invalid age and invalid Passport number

#Case2
passenger1 = Passenger("Omar", "Said", 10, "P12345678")
flight1 = Flight("F123", "City A", "City B", date(2022, 12, 10), datetime(2022, 12, 10, 12, 30))
seat1 = Seat("05A", SeatClass.FIRST)
reservation1 = Reservation("R1", passenger1, flight1, seat1)
try:
    ReservationManager().confirm_reservation(reservation1)
    ticket1 = TicketManager().generate_ticket(reservation1)
    boarding_pass1 = BoardingPass("Airline A", ticket1, date(2022, 12, 10), datetime(2022, 12, 10, 12, 30),
                                 datetime(2022, 12, 10, 14, 0), "Gate 01", datetime(2022, 12, 10, 12, 0), "Terminal 1", "T123")
    boarding_pass1.display_boarding_pass()
except ValueError as e:
    print(f"Error: {e}")

#Case2.1
passenger1 = Passenger("Ali", "Samy", 19, "P8")
flight1 = Flight("F123", "City A", "City B", date(2022, 12, 10), datetime(2022, 12, 10, 12, 30))
seat1 = Seat("05A", SeatClass.FIRST)
reservation1 = Reservation("R1", passenger1, flight1, seat1)
try:
    ReservationManager().confirm_reservation(reservation1)
    ticket1 = TicketManager().generate_ticket(reservation1)
    boarding_pass1 = BoardingPass("Airline A", ticket1, date(2022, 12, 10), datetime(2022, 12, 10, 12, 30),
                                 datetime(2022, 12, 10, 14, 0), "Gate 01", datetime(2022, 12, 10, 12, 0), "Terminal 1", "T123")
    boarding_pass1.display_boarding_pass()
except ValueError as e:
    print(f"Error: {e}")


# In[4]:


# Case 3: Unsuccessful boarding pass generation for unconfirmed reservation
passenger3 = Passenger("Alina", "John", 28, "P56789012")
flight3 = Flight("F789", "City E", "City F", date(2022, 12, 25), datetime(2022, 12, 25, 16, 45))
seat3 = Seat("18C", SeatClass.FIRST)
reservation3 = Reservation("R3", passenger3, flight3, seat3)
try:
    ticket3 = TicketManager().generate_ticket(reservation3)
    boarding_pass3 = BoardingPass("Airline Y", ticket3, date(2022, 12, 25), datetime(2022, 12, 25, 16, 45),
                                  datetime(2022, 12, 25, 18, 30), "Gate 2", datetime(2022, 12, 25, 15, 45), "Terminal B", "ET3")
except ValueError as e:
    print(f"Error: {e}")

