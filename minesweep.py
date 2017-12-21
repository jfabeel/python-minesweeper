from logger import *
import gameboard

game_over = False

print "Welcome to minesweeper."
print "At any time type 'quit' to exit the game."

game_board.print_game()

while 1:
    start_x = (raw_input("Enter starting x coordinate(1 - 10): "))
    if (start_x == 'quit'):
        exit()

    start_y = (raw_input("Enter starting y coordinate(1 - 10): "))
    if (start_y == 'quit'):
        exit()

    try:
        start_x = int(start_x)
        start_y = int(start_y)
    except ValueError:
        print "Invalid Input: coordinates must be an integer"
        continue

    if start_x > 10 or start_x < 1 or start_y > 10 or start_y < 1:
        print "Coordinate must be between 1 and 10"
        continue

    start_x = start_x - 1
    start_y = start_y - 1

    flag_count = 10

    game_board = gameboard.Gameboard(10, 10, flag_count, start_x, start_y)
    game_board.process_player_selection(start_x, start_y)
    game_board.print_game()

    break

while not game_over:
    while not game_over:
        if flag_count < 1 and game_board.check_win():
            print printout("You have won!", MAGENTA)
            exit()

        flag = raw_input("Do you want to place/remove a flag? (y/c/n): ")
        if str(flag) == 'quit':
            exit()
        if str(flag) == 'y' and flag_count > 0:
            flag_x = (raw_input("Enter the x coordinate of the flag(1 - 10) or 'cancel' to not place a flag: "))
            if (flag_x == 'quit'):
                exit()

            flag_y = (raw_input("Enter the y coordinate of the flag(1 - 10) or 'cancel' to not place a flag: "))
            if (flag_y == 'quit'):
                exit()

            if flag_x != 'cancel' and flag_y != 'cancel':
                try:
                    flag_x = int(flag_x)-1
                    flag_y = int(flag_y)-1

                except ValueError:
                    print "Invalid Input: Flag coordinates must be integers"
                    continue

                if flag_x < 0 or flag_x > 9 or flag_y < 0 or flag_y > 9:
                    print "Invalid Range for flag coordinate: must be between 1 and 10"
                    continue

                success = game_board.place_flag(flag_x, flag_y)
                if success:
                    flag_count = flag_count - 1
                    print printout("Flag placed at (" + str(flag_x+1) + ", " + str(flag_y+1) + ") with " + str(flag_count) + " flags remaining", CYAN)

                    game_board.print_game()
                else:
                    print printout("Invalid Flag Placement at (" + str(flag_x+1) + ", " + str(flag_y+1)+")", RED)

        elif flag_count < 0 and str(flag) != 'n':
            print "You are out of flags"

        elif str(flag) == 'c':
            flag_x = (raw_input("Enter the x coordinate of the flag(1 - 10) or 'cancel' to not change a flag: "))
            if (flag_x == 'quit'):
                exit()

            flag_y = (raw_input("Enter the y coordinate of the flag(1 - 10) or 'cancel' to not change a flag: "))
            if (flag_y == 'quit'):
                exit()

            elif flag_x != 'cancel' and flag_y != 'cancel':
                try:
                    flag_x = int(flag_x)-1
                    flag_y = int(flag_y)-1

                except ValueError:
                    print "Invalid Input: Flag coordinates must be integers"
                    continue

                if flag_x < 0 or flag_x > 9 or flag_y < 0 or flag_y > 9:
                    print "Invalid Range for flag coordinate: must be between 1 and 10"
                    continue

                print str(flag_x) + ", " + str(flag_y)

                success = game_board.remove_flag(flag_x, flag_y)
                if success:
                    flag_count = flag_count + 1
                    print printout("Flag removed at (" + str(flag_x+1) + ", " + str(flag_y+1) + ") with " + str(flag_count) + " flags remaining", CYAN)

                    game_board.print_game()
                else:
                    print printout("Invalid Flag Removal at (" + str(flag_x+1) + ", " + str(flag_y+1)+") : Doesn't Exist", RED)

        elif str(flag) == 'n':
            break
        elif str(flag) != 'n' or str(flag) != 'y' or str(flag) != 'c':
            print printout("Invalid Input", RED)

    while not game_over:
        x = raw_input("Enter an x coordinate(1 - 10) or 'end' to cancel: ")
        if str(x) == 'end':
            break
        if str(x) == 'quit':
            exit()
        y = raw_input("Enter an y coordinate(1 - 10) or 'end' to cancel: ")
        if str(y) == 'end':
            break
        if str(y) == 'quit':
            exit()

        try:
            x = int(x)-1
            y = int(y)-1

        except ValueError:
            print "Invalid Input: coordinates must be integers"
            continue

        if x < 0 or x > 9 or y < 0 or y > 9:
            print "Invalid Range for coordinate: must be between 1 and 10"
            continue

        bomb = game_board.process_player_selection(y, x)
        game_board.print_game()

        if bomb == 'bomb':
            print printout("Game Over you hit a bomb", YELLOW)
            game_over = True
            break

        if flag_count <= 0 and game_board.check_win():
            print printout("You have won!", MAGENTA)
            exit()
