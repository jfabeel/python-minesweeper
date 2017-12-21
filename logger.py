import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False 
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False

def printout(text, colour=WHITE):
	if has_colours(sys.stdout):
		seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
		return seq
	else:
		return text

def print_grid(width, height, matrix):    
        sys.stdout.write("      ")
	for i in range(width):
		sys.stdout.write(printout(str(i+1), MAGENTA) + " ")
	sys.stdout.write("\n")
	for i in range(width):
		sys.stdout.write(printout(str(i +1), MAGENTA) + '    [') if i + 1 < 10 else sys.stdout.write(printout(str(i + 1), MAGENTA) + '   [')
		for j in range(height):
			sys.stdout.write(str(matrix[i][j]) + " ")
    		sys.stdout.write("]\n")