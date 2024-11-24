import curses
import time
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
# sh, sw = stdscr.getmaxyx()
sh, sw = 40,60
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Define colors
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Snake initial settings
snake_x = sw // 2
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Food settings
food = [sh // 2, sw // 4]
w.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))

key = curses.KEY_RIGHT

def draw_snake(snake):
    for y, x in snake:
        w.addch(y, x, curses.ACS_CKBOARD, curses.color_pair(4))

def display_message(msg, color_pair):
    w.clear()
    h, wmax = w.getmaxyx()
    x = wmax // 2 - len(msg) // 2
    y = h // 2
    w.addstr(y, x, msg, curses.color_pair(color_pair))
    w.refresh()

try:
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if key == ord('q'):
            break

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 1),
                    random.randint(1, sw - 1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        if (
            snake[0][0] in [0, sh] or
            snake[0][1] in [0, sw] or
            snake[0] in snake[1:]
        ):
            display_message("You lost! Press Q to quit or R to restart", 1)
            while True:
                restart_key = w.getch()
                if restart_key == ord('q'):
                    gameover = True
                    break
                elif restart_key == ord('r'):
                    snake = [
                        [snake_y, snake_x],
                        [snake_y, snake_x - 1],
                        [snake_y, snake_x - 2]
                    ]
                    food = [sh // 2, sw // 4]
                    w.clear()
                    w.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))
                    key = curses.KEY_RIGHT
                    break

        w.clear()
        draw_snake(snake)
        w.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))

        w.refresh()

finally:
    curses.endwin()
    print("Game Over")
