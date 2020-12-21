import copy
from input_reader import *

seat_layout_raw = read_task_input(11).split("\n")

class Seat:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state
    
    def state_change(self, adjacents) -> bool:
        """Changes the state of the seat.
        Returns whether the state was changed or not."""
        #Part 2 - Adjacents will have 8 seats, but will be the next seat (or None)
        # in that direction

        # Part 1 - elif condition should end with occupied_count >= 4

        # This is perform a "round"
        # If adjacents doesn't contain # and state is L, set state to #
        # Else If adjacents has 4+ # in and state is #, set state to L
        occupied_count = 0
        for a in adjacents:
            if a is not None and a.get_state() == '#':
                occupied_count += 1

        if (self.state == 'L' and occupied_count == 0):
            self.state = '#'
            return True
        elif (self.state == '#' and occupied_count >= 5):
            self.state = 'L'
            return True
        else:
            return False

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state


class SeatingArea:
    def __init__(self, raw):
        self.layout = self.convert_layout_to_seats(raw)

    def convert_layout_to_seats(self, raw):
        seat_layout_raw_2d = [list(s) for s in raw]
        seat_layout = [[]]
        for row_i in range(len(seat_layout_raw_2d)):
            for col_i in range(len(seat_layout_raw_2d[row_i])):
                seat_layout[row_i].append(Seat(seat_layout_raw_2d[row_i][col_i]))
            
            if row_i != len(seat_layout_raw_2d) - 1:
                    seat_layout.append([])

        return seat_layout

    def change_states(self, n=1):
        for _ in range(n):
            unchanged_layout = copy.deepcopy(self.layout)
            change_count = 0

            for row_i in range(len(self.layout)):
                for col_i in range(len(self.layout[row_i])):
                    # PART 1
                    #N, NE, E, SE, S, SW, W, NW
                    """compass = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
                    adjacents = [None, None, None, None, None, None, None, None]

                    for compass_point_i in range(len(compass)):
                        new_row_i = row_i + compass[compass_point_i][0]
                        new_col_i = col_i + compass[compass_point_i][1]

                        # new_row_i and new_col_i will be each adjacent seat
                        row_in_bounds = 0 <= new_row_i < len(self.layout)
                        col_in_bounds = 0 <= new_col_i < len(self.layout[row_i])
                        if row_in_bounds and col_in_bounds:
                            adj = unchanged_layout[new_row_i][new_col_i]
                            adjacents[compass_point_i] = adj

                    seat_changed = self.layout[row_i][col_i].state_change(adjacents)
                    if seat_changed:
                        change_count += 1"""

                    # PART 2
                    compass = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
                    next_seats = [None, None, None, None, None, None, None, None]

                    for compass_point_i in range(len(compass)):
                        new_row_i = row_i + compass[compass_point_i][0]
                        new_col_i = col_i + compass[compass_point_i][1]

                        while   (0 <= new_row_i < len(self.layout) and
                                 0 <= new_col_i < len(self.layout[row_i]) and
                                 unchanged_layout[new_row_i][new_col_i].get_state() == '.'):
                            # While we're looking at floor, keep moving in the direction
                            # until either reaching the edge or a L or #

                            new_row_i += compass[compass_point_i][0]
                            new_col_i += compass[compass_point_i][1]

                        # Here, either unchanged[r][c] is out of bounds or it's a seat
                        if (0 <= new_row_i < len(self.layout) and 0 <= new_col_i < len(self.layout[row_i])):
                            next_seats[compass_point_i] = unchanged_layout[new_row_i][new_col_i]

                    seat_changed = self.layout[row_i][col_i].state_change(next_seats)
                    if seat_changed:
                        change_count += 1

            if change_count == 0:
                return False
        return True
            
    def count_seats(self, type):
        count = 0
        for row in self.layout:
            for s in row:
                if s.get_state() == type:
                    count += 1
        return count

    def get_layout(self):
        return self.layout

    def __str__(self):
        final_str = ""
        for row in self.layout:
            for s in row:
                final_str += s.get_state()
            final_str += "\n"
        return final_str.strip()

    def __repr__(self):
        final_str = ""
        for row in self.layout:
            for s in row:
                final_str += s.get_state()
            final_str += "\n"
        return final_str.strip()
    

waiting_area = SeatingArea(seat_layout_raw)

print("Original Waiting Area:")
print(waiting_area)
print("")

c = 0
stabilized = not waiting_area.change_states()
while not stabilized:
    c += 1
    print("Chaning State")
    stabilized = not waiting_area.change_states()

print("Stabilized!")
print("New Waiting Area (after " + str(c) + " changes):")
print(waiting_area)
print("")

print("Occupied Seats:", waiting_area.count_seats('#'))
print("Uncccupied Seats:", waiting_area.count_seats('L'))
print("Floor:", waiting_area.count_seats('.'))
