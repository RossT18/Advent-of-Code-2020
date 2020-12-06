from input_reader import *
import math

seat_data = read_task_input(5).split("\n")

# Not sure a SeatCode class was relevant but I wanted to do it this way
class SeatCode:
    def __init__(self, raw):
        self.raw = raw
        self.row = -1
        self.col = -1
        self.seat_id = -1
        self.find_seat()

    def pick_half(self, lower, upper, choice):
        start = lower
        end = upper
        
        if choice == 'F' or choice == 'L':
            mid = math.floor((upper - lower) / 2)
            end -= mid + 1
        elif choice == 'B' or choice == 'R':
            mid = math.ceil((upper - lower) / 2)
            start += mid
        else:
            print("Invalid Choice")

        return [start, end]

    def find_seat(self):
        row_low, row_upp = 0, 127
        for ltr in self.raw[:-3]:
            row_low, row_upp = self.pick_half(row_low, row_upp, ltr)

        self.row = row_low
        col_low, col_upp = 0, 7
        for ltr in self.raw[-3:]:
            col_low, col_upp = self.pick_half(col_low, col_upp, ltr)
        self.col = col_low


    def calculate_seat_id(self):
        self.seat_id = self.row * 8 + self.col
        return self.seat_id

    def get_seat_id(self):
        return self.calculate_seat_id()

    def get_raw(self):
        return self.raw

    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col


seats = [SeatCode(raw) for raw in seat_data]
seat_ids = [s.get_seat_id() for s in seats]

for i in range(0, 1000):
    if i not in seat_ids:
        if i + 1 in seat_ids and i - 1 in seat_ids:
            print("Your Seat: " + str(i)) # The correct answer will have no +1 and -1 value

# Could use max function on seat_ids instead
current_max = seats[0]
for s in seats:
    if s.get_seat_id() > current_max.get_seat_id():
        current_max = s

print(  current_max.get_raw() +
        ", row: " + str(current_max.get_row()) +
        ", col: " + str(current_max.get_col()) +
        ", id: " + str(current_max.get_seat_id()))