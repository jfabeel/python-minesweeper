from logger import *
import random

class Gameboard:
    hidden_field = ''
    game_board = ''

    width = 0
    height = 0

    bomb_count = 0

    def __init__(self, width, height, bomb_count, start_x, start_y):
	    self.width = width
	    self.height = height

	    self.bomb_count = bomb_count

	    self.generate_minesweep_matrix(start_x, start_y)
	    self.generate_playing_field()
	    self.generate_hidden_field()
        
    def print_game(self):
	    print_grid(self.width, self.height, self.hidden_field)

    def get_game_board(self):
	    return game_board

    def get_hidden_field(self):
	    return hidden_field

    def get_width(self):
	    return width

    def get_height(self):
	    return height

    def generate_minesweep_matrix(self, start_x, start_y):
        self.game_board = [[0 for i in range(self.height)] for j in range(self.width)]
        current_count = 0
        
        for i in range(self.width):
            for j in range(self.height):
                self.game_board[i][j] = 0

        while current_count < self.bomb_count:
            i = random.randint(0, self.width-1)
            j = random.randint(0, self.height-1)

            if start_x == i and start_y == j:
                continue

            if self.game_board[i][j] == 7:
                continue
            else:
                self.game_board[i][j] = 7
                current_count = current_count + 1

    def generate_playing_field(self):
        playing_field = [[0 for i in range(self.height)] for j in range(self.width)]
        
        for i in range(self.width):
            for j in range(self.height):
                if int(self.game_board[i][j]) == 7:
                    continue
                
                bomb_count = 0
                for k in range(3):
                    for h in range(3):
                        if k-1 == 0 and h-1 == 0:
                            continue
                        if (k-1) + i >= self.width or (h-1)+j >= self.height or (k-1)+i < 0 or (h-1)+j < 0:
                            continue
                        if self.game_board[i + (k-1)][j + (h-1)] == 7:
                            bomb_count = bomb_count + 1
                self.game_board[i][j] = bomb_count
                                
    def generate_hidden_field(self):
        self.hidden_field = [[0 for i in range(self.height)] for j in range(self.width)]
        
        for i in range(self.width):
            for j in range(self.height):
                self.hidden_field[i][j] = printout('O', WHITE)                

    def is_pair_existant(self, array, a, b):
    	index = 0
        
        print str(a) + ", " + str(b)

    	while index < len(array):
    		if array[index] == a and array[index + 1] == b:
    			return True
    		index = index + 2
    	return False

    def open_free_space(self, x, y, open_space):
        free_space = []

        for k in range(3):
            for h in range(3):
                x_index = x+(k-1)
                y_index = y+(h-1)

                if (x_index == 0) and (y_index == 0):
                    continue
                if x_index >= self.width or y_index >= self.height or x_index < 0 or y_index < 0:
                    continue
                if self.game_board[x_index][y_index] == 0 and open_space[x_index][y_index] == 0:
                    open_space[x_index][y_index] = 7
                    free_space.append(x_index)
                    free_space.append(y_index)
                    free_space = free_space + self.open_free_space(x_index, y_index, open_space)
                elif self.game_board[x_index][y_index] != 7 and open_space[x_index][y_index] == 0:
                    open_space[x_index][y_index] = 7
                    free_space.append(x_index)
                    free_space.append(y_index)

        return free_space
        
    def process_player_selection(self, x, y):  
        if (self.hidden_field[x][y] == printout('F', RED)):
            return
               
        self.hidden_field[x][y] = printout(str(self.game_board[x][y]), GREEN) if self.game_board[x][y] != 0 else printout(str(self.game_board[x][y]), CYAN)
        open_space = [[0 for i in range(self.width)] for j in range(self.height)]
        free_space_indices = []

        if self.game_board[x][y] == 7:
            return 'bomb'
        if self.game_board[x][y] == 0:
            free_space_indices = self.open_free_space(x, y, open_space)

        index = 0

        while index < len(free_space_indices):
            current_x = free_space_indices[index]
            current_y = free_space_indices[index + 1]

            self.hidden_field[current_x][current_y] = printout(str(self.game_board[current_x][current_y]), GREEN) if self.game_board[current_x][current_y] != 0 else printout(str(self.game_board[current_x][current_y]), CYAN)
            index = index + 2

    def place_flag(self, y, x):
        if (self.hidden_field[x][y] == printout('O', WHITE)):
            self.hidden_field[x][y] = printout('F', RED)
            return True
        else:
            print self.hidden_field[x][y]
            return False

    def remove_flag(self, y, x):        
        if (self.hidden_field[x][y] == printout('F', RED)):
            self.hidden_field[x][y] = printout('O', WHITE)
            return True
        else:
            return False

    def check_win(self):
        flag_count = 0
        
        for i in range(self.width):
            for j in range(self.height):
                if self.hidden_field[i][j] == printout('F', RED) and self.game_board[i][j] != 7:
                    return False
                elif self.hidden_field[i][j] == printout('F', RED):
                    flag_count = flag_count + 1

        return flag_count == 10
