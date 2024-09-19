
#this code for maze game 
# =intialize the all variable 
lives = 3 #player start with 3 
score = 0 #payer with score 0 
player_x, player_y = 0, 0 #player start the position
direction="down"

#desplay player current states 
def display_states(): 
    print(f"lives ;{lives}") 
    print(f"score ;{score}") 
    print(f"player position : ({player_x}, {player_y}")
    print(f"-"  * 20)

#move player and move position and score 
def move_player(direction):
    global player_y
    global player_x
    if direction == "up" :
         player_x += 1
    elif direction == "down":
         player_x -= 1 
    elif direction == "left":
         player_x -= 1
    elif direction == "right":
         player_x += 1
    else: 
         print("invalide move!")    
     
#stamulate losing a life 
def lose_life(): 
    global lives
    if lives > 0:
        lives -= 1
        print("you lose a life")
        if lives ==0: 
           print("game over !")

#stamulate gaining score (e.g., by collecting items)
def gain_score (point):
    global score 
    score += point 
    print(f"you gained {point}points!") 
    
#Main game loop exmaple
print("starting game...") 
display_states()

#exmaple player movement and action 
move_player("up")
display_states()

gain_score(10) #player collect an item worth 10 points 
display_states()

lose_life() #player hits an obstacl and loses life 
display_states()

move_player("right")
display_states()

gain_score(20) #player gains more points
display_states()

lose_life() #another aobstacl hit, losing another life 
display_states()

#check for game over 
if lives == 0: 
    print("no lives left. game over!")


