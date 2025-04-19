# import modules
import random
import curses

# initialize the curses library to create the screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)

# get max width and height
screen_height, screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)

# allow window to receive input from the keyboard
window.keypad(1)

# set the delay for updating the screen
window.timeout(125)

# set the x,y coordinates of the initial snake's head position
snake_x = screen_width//4
snake_y = screen_height//2

# define the initial length of the snake's body
snake = [
  [snake_y,snake_x],
  [snake_y, snake_x - 1],
  [snake_y, snake_x - 2]
]

# create the food in the middle of the window
food = [screen_height//2, screen_width//2]

# add the food to the window
window.addch(food[0], food[1], curses.ACS_PI)

# set the initial direction of the snake to the right
key = curses.KEY_RIGHT

# create a game loop
while True:
  # get the next key pressed by the user
  next_key = window.getch()

  # if the user dosen't press a key, keep moving in the same      direction else key will set to next_key
  key = key if next_key == -1 else next_key

  # check if the snake hits the wall or it self 
  if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:] :

    # if it does then end the game
    curses.endwin()
    quit()

  # set the head's new position
  new_head = [snake[0][0], snake[0][1]]

  # check which key was pressed and update the head's position accordingly
  if key == curses.KEY_DOWN :
    new_head[0] += 1
  if key == curses.KEY_UP :
    new_head[0] -= 1
  if key == curses.KEY_RIGHT :
    new_head[1] += 1
  if key == curses.KEY_LEFT :
    new_head[1] -= 1
    
  # insert the new head to the snake
  snake.insert(0,new_head)

  # check if the snake eats the food
  if snake[0] == food :

    # create new food
    food = None
    while not food:
      new_food = [
        random.randint(1, screen_height - 1),
        random.randint(1, screen_width - 1)
      ]

      # if the new food is not in the snake, set the food to new_food
      food = new_food if new_food not in snake else None

    # add the new food to the window
    window.addch(food[0], food[1], curses.ACS_PI)

  else :
    # remove the last segment of the snake
    tail = snake.pop()
    window.addch(tail[0], tail[1], " ")

  # update the postion of snake on the screen
  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
  
  
  

