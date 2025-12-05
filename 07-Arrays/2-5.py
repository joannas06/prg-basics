# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for seat in cinema_seats:
         for sit in seat:
             total +=1
   return total

def seats_available(seats):
   available = 0
   for seat in cinema_seats:
       for sit in seat:
           if sit == 'A':
               available += 1
   return available

def seats_booked(seats):
   booked = 0
   for seat in cinema_seats:
       for sit in seat:
           if sit == 'B':
               booked += 1
   return booked

def seat_status(seats, row, place):
    if seats[row][place] == 'A':
        return "Available"
    else:
        return "Booked"

print('CINEMA INFORMATION TABLE')
print(f'Total seats:{seats_total(cinema_seats)}')
print(f'Seats available:{seats_available(cinema_seats)}')
print(f'Seats booked:{seats_booked(cinema_seats)}')
print(f'Seat in row 1, place 1:{seat_status(cinema_seats,0,0)}')
print(f'Seat in row 5, place 5:{seat_status(cinema_seats,4,4)}')
print(f'Seat in row 3, place 5:{seat_status(cinema_seats,2,4)}')