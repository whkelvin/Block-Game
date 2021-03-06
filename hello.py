import pygame
class car:
    def __init__(self, orientation, size, row, col, id):
        self.orientation = orientation
        self.size = size
        self.row = row
        self.col = col
        self.ready_to_win = False
        self.update_domain_and_range()
    def contain_point(self, pos):
        if pos[0] >= self.domain[0] and pos[0] <=  self.domain[1] and pos[1] >= self.range[0] and pos[1] <= self.range[1]:
            return True
        else:
            return False
    def update_domain_and_range(self):
        if self.orientation == "v":
            self.domain = [80*self.col, 80* self.col + 80]
            self.range = [80*self.row, 80*self.row + 80*self.size]
        elif self.orientation == "h":
            self.domain = [80*self.col, 80* self.col + 80 * self.size]
            self.range = [80*self.row, 80* self.row + 80]

class game:
    num_of_car = 1

    grid = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    def __init__(self, target_car):
        self.car_list = [target_car]
        self.win = False
        for i in range(target_car.size):
            self.grid[target_car.row][target_car.col + i] = 1

    def add_car(self, car):
        self.num_of_car = self.num_of_car + 1
        if car.orientation == "h":
            for i in range(car.size):
                self.grid[car.row][car.col + i] = 1

        elif car.orientation == "v":
            for i in range(car.size):
                self.grid[car.row + i][car.col] = 1

        self.car_list.append(car)

    def move_car(self, id, direction):

        if id < self.num_of_car:
            if self.car_list[id].orientation == "h":
                if direction == 0:
                    #left
                    #if current car had space to move to the left
                    if self.car_list[id].col != 0:
                        #if the space to the left of current car is not occupied by another car
                        if self.grid[self.car_list[id].row][self.car_list[id].col - 1] != 1:
                            #if target car is moved to the left when it was going to win but decided to moved back
                            if id == 0 and self.car_list[0].col > 5 - self.car_list[0].size:
                                self.car_list[id].col = self.car_list[id].col - 1
                                self.grid[self.car_list[id].row][self.car_list[id].col] = 1
                                if self.car_list[id].col + self.car_list[id].size - 1 < 5:
                                     self.grid[self.car_list[id].row][self.car_list[id].col +self.car_list[id].size] = 0
                            else:
                                #update car location
                                self.car_list[id].col = self.car_list[id].col - 1
                                #update grid
                                self.grid[self.car_list[id].row][self.car_list[id].col] = 1
                                self.grid[self.car_list[id].row][self.car_list[id].col + self.car_list[id].size] = 0

                        else:
                            print("the car is blocked by another car")
                    else:
                        print("cannot move car: it has reached the edge")

                elif direction == 1:
                    #right
                    if self.car_list[id].ready_to_win == True:
                        self.win = True
                        print("You've won!!!!")
                        self.grid[self.car_list[id].row][self.car_list[id].col] = 0
                    else:
                    # if current car had space to move to the right
                        if self.car_list[id].col + self.car_list[id].size - 1 != 5:
                        # if the space to the left of current car is not occupied by another car
                            if self.grid[self.car_list[id].row][self.car_list[id].col +self.car_list[id].size - 1 + 1] != 1:
                            # update car location
                                self.car_list[id].col = self.car_list[id].col + 1
                            # update grid
                                self.grid[self.car_list[id].row][self.car_list[id].col + self.car_list[id].size - 1] = 1
                                self.grid[self.car_list[id].row][self.car_list[id].col - 1] = 0
                            else:
                                print("the car is blocked by another car")
                        else:
                            #if target car moves beyond the edge
                            if id == 0:
                                self.car_list[0].col = self.car_list[0].col + 1
                                self.grid[self.car_list[0].row][self.car_list[id].col-1] = 0
                            else:
                                print("cannot move car: it has reached the edge")
            elif self.car_list[id].orientation == "v":
                if direction == 0:
                    #move up
                    # if current car had space to move to the left
                    if self.car_list[id].row != 0:
                        # if the space to the left of current car is not occupied by another car
                        if self.grid[self.car_list[id].row - 1][self.car_list[id].col] != 1:
                            # update car location
                            self.car_list[id].row = self.car_list[id].row - 1
                            # update grid
                            self.grid[self.car_list[id].row][self.car_list[id].col] = 1
                            self.grid[self.car_list[id].row + self.car_list[id].size][self.car_list[id].col] = 0
                        else:
                            print("the car is blocked by another car")
                    else:
                        print("cannot move car: it has reached the edge")
                elif direction == 1:
                    #move down
                    # if current car had space to move to the left
                    if self.car_list[id].row + self.car_list[id].size - 1 != 5:
                        # if the space to the left of current car is occupied by another car
                        if self.grid[self.car_list[id].row + self.car_list[id].size -1 + 1][self.car_list[id].col] != 1:
                            # update car location
                            self.car_list[id].row = self.car_list[id].row + 1
                            # update grid
                            self.grid[self.car_list[id].row + self.car_list[id].size - 1][self.car_list[id].col] = 1
                            self.grid[self.car_list[id].row - 1][self.car_list[id].col] = 0
                        else:
                            print("the car is blocked by another car")
                    else:
                        print("cannot move car: it has reached the edge")
            self.car_list[id].update_domain_and_range()
        else:
            print("invalid car id")

        if id == 0:
            #this is the winning car
            print(self.car_list[0].row)
            print(self.car_list[0].col)
            if self.car_list[id].row == 2 and self.car_list[id].col   == 5:
                self.car_list[id].ready_to_win = True
                print(self.car_list[id].ready_to_win)
            else:
                self.car_list[id].ready_to_win = False

    def get_car_list(self):
        return self.car_list

    def print_grid(self):
        for i in range(6):
            for j in range(6):
                print(self.grid[i][j], end = "")

            print("\n")

def draw_grid(surface, size):
    black = (150,150,150)
    for i in range(6):
        surface.fill(black, (0, i * size/6, size, 1))
        surface.fill(black, (i * size/6, 0,  1, size))

def draw_car(surface, car, color):
    white = (255, 255, 255)
    black = (255,255,255)
    if car.orientation == "h":
            surface.fill(color, ((car.col) * 80, (car.row)* 80, 80*car.size, 80))
            #border
            surface.fill(black, ((car.col) * 80, (car.row) * 80, 80*car.size, 1)) #top hor
            surface.fill(black, ((car.col) * 80, (car.row) *80 + 80, 80*car.size, 1)) #button hor
            surface.fill(black, ((car.col) * 80, (car.row) * 80, 1, 80))#left ver
            surface.fill(black, ((car.col) * 80 + 80 * car.size, (car.row) * 80, 1, 80))#right ver
    elif car.orientation == "v":
            surface.fill(color, ((car.col) * 80, (car.row) * 80, 80, 80*car.size))
            # border
            surface.fill(black, ((car.col) * 80, (car.row) * 80, 80,1))  # top hor
            surface.fill(black, ((car.col) * 80, (car.row) * 80 + 80 * car.size, 80, 1))  # button hor
            surface.fill(black, ((car.col) * 80, (car.row) * 80, 1, 80 * car.size))  # left ver
            surface.fill(black, ((car.col) * 80 + 80, (car.row) * 80, 1, 80* car.size))  # right ver

def load_carlist_from_file(filename):
    car_list = []
    f = open(filename, "r")
    i = 0
    for line in f:
        orientation, size, row, col = line.split(", ")
        orientation = str(orientation)
        row = int(row)
        col = int(col)
        size = int(size)
        car_list.append(car(orientation, size, row, col, i))
        i += 1
    f.close()
    return car_list

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.
    car_list = load_carlist_from_file("car.txt")
    game1 = game(car_list[0])

    my_font = pygame.font.SysFont("Courier", 50)

    for i in range(1,len(car_list)):
        game1.add_car(car_list[i])



    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    black = (0, 0, 0)        # A color is a mix of (Red, Green, Blue)
    green = (0, 0, 120)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = ev.dict["pos"]
            for i in range(len(car_list)):
                if car_list[i].contain_point(clicked_pos):
                    #if mouse click is right on a car
                    print(i)
                    current_car = i
        if ev.type == pygame.MOUSEBUTTONUP:
            released_pos = ev.dict["pos"]
            if car_list[current_car].orientation == "v":
                if released_pos[1] > clicked_pos[1]:
                    #move down
                    game1.move_car(current_car, 1)
                elif released_pos[1] < clicked_pos[1]:
                    #move up
                    game1.move_car(current_car, 0)
            elif car_list[current_car].orientation == "h":
                if released_pos[0] > clicked_pos[0]:
                    #move right
                    game1.move_car(current_car, 1)
                elif released_pos[0] < clicked_pos[0]:
                    #move left
                    game1.move_car(current_car, 0)


            #game1.print_grid()
            print("\n")
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        #game1.print_grid()
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((50, 50, 50))
        if not game1.win:
            draw_grid(main_surface, 480)
            if game1.win != True:
                draw_car(main_surface, game1.car_list[0], green)
            for j in range(len(car_list)):
                draw_car(main_surface, game1.car_list[j], black)
                if j == 0:
                    draw_car(main_surface, game1.car_list[0], green)

        else:
            label = my_font.render("YOU WIN!!", 1, (255, 255, 0))
            main_surface.blit(label, (110, 200))

        #display
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
