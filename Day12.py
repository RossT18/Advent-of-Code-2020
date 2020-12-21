from input_reader import *

instructions_raw = read_task_input(12).split("\n")

class Ship:
    def __init__(self):
        self.position = [0, 0]
        self.direction = 90
        self.waypoint_pos = [1, 10]

    def move_forward(self, distance):
        if (self.direction == 0):
            self.position[0] += distance
        elif (self.direction == 180):
            self.position[0] -= distance
        elif (self.direction == 90):
            self.position[1] += distance
        elif (self.direction == 270):
            self.position[1] -= distance
        else:
            print("Direction was invalid!")
            print(self.direction)

    def move_forward_to_waypoint(self, times):
        new_n = self.waypoint_pos[0] * times
        new_e = self.waypoint_pos[1] * times
        self.position = [self.position[0] + new_n, self.position[1] + new_e]

    def rotate(self, lr, degrees):
        """ Part 1 Method """
        if lr == "L":
            self.direction -= degrees
        elif lr == "R":
            self.direction += degrees
        else:
            print("LR was invalid")
            print(lr)

        self.direction = self.direction % 360

    def move_absolute(self, direction, distance):
        """ Part 1 Method """
        if direction == "N":
            self.position[0] += distance
        elif direction == "S":
            self.position[0] -= distance
        elif direction == "E":
            self.position[1] += distance
        elif direction == "W":
            self.position[1] -= distance
        
    def move_waypoint(self, direction, distance):
        if direction == "N":
            self.waypoint_pos[0] += distance
        elif direction == "S":
            self.waypoint_pos[0] -= distance
        elif direction == "E":
            self.waypoint_pos[1] += distance
        elif direction == "W":
            self.waypoint_pos[1] -= distance

    def rotate_waypoint(self, lr, degrees):
        if degrees % 180 != 0:
            # Need to swap the n and e
            temp_e = self.waypoint_pos[1]
            self.waypoint_pos[1] = self.waypoint_pos[0]
            self.waypoint_pos[0] = temp_e

            if lr == "L":
                self.waypoint_pos[1 if degrees < 180 else 0] *= -1
            elif lr == "R":
                self.waypoint_pos[0 if degrees < 180 else 1] *= -1
            else:
                print("Invalid LR", lr)
        elif degrees > 0:
            self.waypoint_pos[0] *= -1
            self.waypoint_pos[1] *= -1

        
    def give_instructions(self, instructions):
        for i in instructions:
            command = i[0]
            value = int(i[1:])
            if command == "F":
                self.move_forward_to_waypoint(value)
            elif command == "R" or command == "L":
                self.rotate_waypoint(command, value)
            else:
                self.move_waypoint(command, value)

    def get_position(self):
        return self.position

    def get_manhatten_distance(self):
        return abs(self.position[0]) + abs(self.position[1])



s = Ship()
s.give_instructions(instructions_raw)

print("Manhatten Distance:", s.get_manhatten_distance())