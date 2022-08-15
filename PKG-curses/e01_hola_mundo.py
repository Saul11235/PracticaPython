import curses

scr = curses.initscr()
scr.keypad(0)
curses.noecho()

scr.addstr("Hola Mundo")
scr.refresh()
scr.getch()

curses.endwin()
