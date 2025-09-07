<<<<<<< HEAD
import os,random,time
import threading

rows,cols=8,8
no_obstacles=11
obstacle_refresh_time=2

grid=[[' ' for _ in range(cols)] for _ in range(rows)]

start_position=(0,0)
grid[start_position[0]][start_position[1]]='S'

end_position=((rows-1),(cols-1))
grid[end_position[0]][end_position[1]]='E'

lock=threading.Lock()  #to prevent the race conditions

def place_random_score():
    while True:
        r,c=random.randint(0,rows-1),random.randint(0,cols-1)
        if grid[r][c]==' ':
            grid[r][c]='1'
            return(r,c)
        

def place_randome_obstacles():
    with lock:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="#":
                    grid[r][c]=' '
        placed=0
        while placed<no_obstacles:
            r,c=random.randint(0,rows-1),random.randint(0,cols-1)
            if grid[r][c]==' ':
                grid[r][c]='#'
                placed+=1

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def print_grid(curr_grid ,player_position,score):
    clear_screen()
    display_grid=[row[:] for row in curr_grid]
    r,c=player_position
    display_grid[r][c]='p'
    for row in display_grid:
        print(' '.join(row))
    print(f"\nScore:{score}")

def moves():
    valid_movs={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    while True:
        move=input("Enter your move (u, d, l, r): ").lower().strip()
        if move in valid_movs:
            return valid_movs[move]
        
def obstacle_refresher():
    while not game_over:
        time.sleep(obstacle_refresh_time)
        place_randome_obstacles()
    
player_poss=[start_position[0],start_position[1]]
score=0
game_over=False
score_poss=place_random_score()
place_randome_obstacles()

threading.Thread(target=obstacle_refresher,daemon=True).start()

print("Welcome to the Timed Grid Game!")
print("Navigate from 'S' to 'E'.")
print("Collect '1's for points. Avoid '#' obstacles.")
print(f"Obstacles change automatically every {obstacle_refresh_time} seconds!")
input("Press Enter to start...")


while not game_over:
    print_grid(grid,player_poss,score)

    r,c=moves()
    n_row,n_col=player_poss[0]+r,player_poss[1]+c
    with lock:
        if not(0<=n_row<rows and 0<=n_col<cols):
            print("You can't move off the grid!")
            continue
    cell=grid[n_row][n_col]

    if cell=='#':
        print("You hit an obstacle! Move blocked.")
        continue

    if (player_poss[0],player_poss[1])!=start_position:
        grid[player_poss[0]][player_poss[1]]=' '

    player_poss=[n_row,n_col]
    if cell == '1':
        score+=1
        print("You found a point! Score +1.")
        grid[n_row][n_col] = ' '
        score_pos = place_random_score()

    if score==10:
            game_over = True
            print_grid(grid, player_poss, score)
            print("\nCongratulations! You reached the goal!")
            print(f"Your final score is: {score}")
            print("Game Over.")
            break

    if cell=='E':
        game_over =True
        print_grid(grid, player_poss, score)
        print("\nCongratulations! You reached the end!")
        print(f"Your final score is: {score}")
        print("Game Over.")
=======
import os,random,time
import threading

rows,cols=8,8
no_obstacles=11
obstacle_refresh_time=2

grid=[[' ' for _ in range(cols)] for _ in range(rows)]

start_position=(0,0)
grid[start_position[0]][start_position[1]]='S'

end_position=((rows-1),(cols-1))
grid[end_position[0]][end_position[1]]='E'

lock=threading.Lock()  #to prevent the race conditions

def place_random_score():
    while True:
        r,c=random.randint(0,rows-1),random.randint(0,cols-1)
        if grid[r][c]==' ':
            grid[r][c]='1'
            return(r,c)
        

def place_randome_obstacles():
    with lock:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="#":
                    grid[r][c]=' '
        placed=0
        while placed<no_obstacles:
            r,c=random.randint(0,rows-1),random.randint(0,cols-1)
            if grid[r][c]==' ':
                grid[r][c]='#'
                placed+=1

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def print_grid(curr_grid ,player_position,score):
    clear_screen()
    display_grid=[row[:] for row in curr_grid]
    r,c=player_position
    display_grid[r][c]='p'
    for row in display_grid:
        print(' '.join(row))
    print(f"\nScore:{score}")

def moves():
    valid_movs={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    while True:
        move=input("Enter your move (u, d, l, r): ").lower().strip()
        if move in valid_movs:
            return valid_movs[move]
        
def obstacle_refresher():
    while not game_over:
        time.sleep(obstacle_refresh_time)
        place_randome_obstacles()
    
player_poss=[start_position[0],start_position[1]]
score=0
game_over=False
score_poss=place_random_score()
place_randome_obstacles()

threading.Thread(target=obstacle_refresher,daemon=True).start()

print("Welcome to the Timed Grid Game!")
print("Navigate from 'S' to 'E'.")
print("Collect '1's for points. Avoid '#' obstacles.")
print(f"Obstacles change automatically every {obstacle_refresh_time} seconds!")
input("Press Enter to start...")


while not game_over:
    print_grid(grid,player_poss,score)

    r,c=moves()
    n_row,n_col=player_poss[0]+r,player_poss[1]+c
    with lock:
        if not(0<=n_row<rows and 0<=n_col<cols):
            print("You can't move off the grid!")
            continue
    cell=grid[n_row][n_col]

    if cell=='#':
        print("You hit an obstacle! Move blocked.")
        continue

    if (player_poss[0],player_poss[1])!=start_position:
        grid[player_poss[0]][player_poss[1]]=' '

    player_poss=[n_row,n_col]
    if cell == '1':
        score+=1
        print("You found a point! Score +1.")
        grid[n_row][n_col] = ' '
        score_pos = place_random_score()

    if score==10:
            game_over = True
            print_grid(grid, player_poss, score)
            print("\nCongratulations! You reached the goal!")
            print(f"Your final score is: {score}")
            print("Game Over.")
            break

    if cell=='E':
        game_over =True
        print_grid(grid, player_poss, score)
        print("\nCongratulations! You reached the end!")
        print(f"Your final score is: {score}")
        print("Game Over.")
>>>>>>> 7e01e2e388143c3aeecd62e0b9083e0dcdc87b2e
        break