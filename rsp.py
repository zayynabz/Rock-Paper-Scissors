import random
choices=["rock", "paper", "scissors"]

#players:
n=int(input("how many players will play? "))
players=[]
for i in range(n):
    player_name=input(f"enter name of player {i+1}: ")
    players.append(player_name)

#scores
scores={player:0 for player in players}
score_computer=0

def scoreboard(scores,score_computer):
    print("SCOREBOARD")
    sorted_scores=sorted(scores.items(),key=lambda x:x[1],reverse=True)
    for player,score in sorted_scores:
        print(f"{player}:{score}")
    print(f"computer:{score_computer}")
    print("------------------\n")

def score_update(scores, active_player):
    scores[active_player]+=1

#pick a random player
active_player=random.choice(players)
print(f"it's {active_player}'s turn")

def valid_choice(player_name):
    while True:
        valid=input(f"{player_name} enter either rock, paper or scissors: ").lower()
        if valid in choices:
            return valid
        print("invalid choice. try again.")

def yes_or_no(p):
    while True:
        yn=input(p).strip().lower()
        if yn in ("yes","y"):
            return True
        if yn in ("no","n"):
            return False
        print("invalid input. type yes or no.")

while players:
    #lets validate the choice first
    player_choice=valid_choice(active_player)      
    computer_choice=random.choice(choices)

    if player_choice==computer_choice:
        print("It's a tie")
    elif ((player_choice=="rock" and computer_choice=="scissors") or 
          (player_choice=="paper" and computer_choice=="rock") or 
          (player_choice=="scissors" and computer_choice=="paper")):
        print("it's a win")
        print("computer chose ",computer_choice)
        score_update(scores,active_player)
    else:
        print("it's a loss")
        print("computer chose ",computer_choice)
        score_computer+=1

    #round result    
    print(f"{active_player} {scores[active_player]}-{score_computer} computer")
 
    #continue?
    if not yes_or_no("do you want to continue? yes or no: "):
        print(f"end of game for {active_player}.\nFinal score:{active_player} {scores[active_player]}-{score_computer} computer")
        players.remove(active_player)

        if players: #MOVE TO THE NEXT PLAYER
            active_player=random.choice(players)
            print(f"now it's {active_player}'s turn")
        else:
            print("no players left")
            scoreboard(scores,score_computer)
            break
        
